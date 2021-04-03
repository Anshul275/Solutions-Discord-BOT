import discord
import os
from datetime import datetime, timedelta
from discord.ext.commands import Cog
from discord.ext.commands import Bot as bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from run_forever.server_alive import keep_alive

from services.programming.stackOverflow import stackOverflow_result
from services.fun.poll import filter_poll_data
from services.fun.poll import getOptions
from services.fun.remind import filter_reminder_data
from services.search.google import google_result
from services.search.web_search import web_result
from services.space.nasa_search import nasa_image
from services.fun.img_search import img_result
from services.fun.fact_search import fact_result
from services.fun.gif_search import gif_image
from services.fun.stickr_search import stickr_image
from services.nsfw.nsfw import nsfw_search
from services.nsfw.nsfw import nsfw_result
from services.nsfw.nsfw import nsfw_images

scheduler = AsyncIOScheduler()

TOKEN = "ODIwNzE5Mjk0MzA3NTAwMDQy.YE5QZw.vYq_nrSbquJw_Lgy5tNcjLtIjRA"


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as ----- {0.user}'.format(client))


option_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣",
		   "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

polls = []

async def final_resPoll(channel_id, message_id, author_id):
    msg = await client.get_channel(channel_id).fetch_message(message_id)

    most_voted = max(msg.reactions, key=lambda r: r.count)

    poll_results = "***Result of POLL conducted by : " + "<@" + str(author_id) + ">\n"
    poll_results += f"The Poll Results   :  Option  {most_voted.emoji} won by {most_voted.count} votes...........***"
    await msg.channel.send(poll_results)

    scheduler.shutdown()

async def remind_user(channel_id, message_id, reminder):
    msg = await client.get_channel(channel_id).fetch_message(message_id)

    send = "Hello " + "<@" + str(msg.author.id) + ">  :slight_smile:  :slight_smile:" + "\n"
    send += "```It's time for : " + reminder + "```"
    await msg.channel.send(send)

    scheduler.shutdown()


@client.event
async def on_message(message):
    #if message.author == client.user:
    if message.author.bot:
        return

    # Message Content
    msg_content = message.content
    
    if msg_content.startswith('-stack'):
        msg_content = msg_content.split('-stack ', 1)
        if len(msg_content) == 2:
            content = stackOverflow_result(msg_content[1])
            greet = "\nHope this helps, HaPPy CoDing!\n"
            await message.channel.send(content + greet)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")
    
    elif msg_content.startswith('-poll'):
        msg_content = msg_content.split('-poll ', 1)
        if len(msg_content) == 2:
            seconds, question, options = filter_poll_data(msg_content[1])
            if seconds == -1:
                await message.channel.send("```Time not provided(in secs) or format wrong....```")
            elif question == "":
                await message.channel.send("```Please provide a 📢POLL question....```")
            elif len(options) < 1:
                await message.channel.send("```At least provide one option....```")
            elif len(options) > 10:
                await message.channel.send("```Max 10 options allowed....```")
            else:
                embed = discord.Embed(title = "📢    POLL",
                            description = question,
                            colour = message.author.colour,
                            timestamp = datetime.utcnow()
                        )

                poll_author = message.author

                option_str = getOptions(options)

                fields = [("Options", option_str, False),
                            ("Instructions", "Choose an option!", False)]

                for name, value, inline in fields:
                    embed.add_field(name = name, value = value, inline = inline)

                message = await message.channel.send(embed = embed)
                for emoji in option_emojis[:len(options)]:
                    await message.add_reaction(emoji)
                polls.append((message.channel.id, message.id))
                
                scheduler.start()
                scheduler.add_job(final_resPoll, 
                                        "date", 
                                        run_date = datetime.now() + timedelta(seconds = seconds),
                                        args = [message.channel.id, message.id, poll_author.id]
                                    )
        else:
            await message.channel.send("```Error Input.........```")
    
    elif msg_content.startswith('-remind'):
        msg_content = msg_content.split('-remind ', 1)
        if len(msg_content) == 2:
            seconds, reminder = filter_reminder_data(msg_content[1])
            if seconds == -1:
                await message.channel.send("```Time not provided(in secs) or format wrong....```")
            elif reminder == "":
                await message.channel.send("```Please enter a REMINDER to be notified....```")
            else:
                scheduler.start()
                scheduler.add_job(remind_user, 
                                        "date", 
                                        run_date = datetime.now() + timedelta(seconds = seconds),
                                        args = [message.channel.id, message.id, reminder]
                                    )
        else:
            await message.channel.send("```Error Input.........```")

    elif msg_content.startswith('-google'):
        msg_content = msg_content.split('-google ', 1)
        if len(msg_content) == 2:
            content = google_result(msg_content[1])
            greet = "\nHope this helps!\n"
            await message.channel.send(content + greet)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")
    
    elif msg_content.startswith('-web'):
        msg_content = msg_content.split('-web ', 1)
        if len(msg_content) == 2:
            content = web_result(msg_content[1])
            greet = "\nHope this helps!\n"
            await message.channel.send(content + greet)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")

    elif msg_content.startswith('-nasa'):
        msg_content = msg_content.split('-nasa ', 1)
        if len(msg_content) == 2:
            content_text, content_image = nasa_image(msg_content[1])
            if(content_text):
                await message.channel.send(content_text)
            if(content_image):
                await message.channel.send(content_image)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")
    
    elif msg_content.startswith('-img'):
        msg_content = msg_content.split('-img ', 1)
        if len(msg_content) == 2:
            content = img_result(msg_content[1])
            await message.channel.send(content)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")

    elif msg_content.startswith('-fact'):
        msg_content = msg_content.split('-fact ', 1)
        if len(msg_content) == 2:
            content = fact_result(msg_content[1])
            await message.channel.send(content)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")

    elif msg_content.startswith('-gif'):
        msg_content = msg_content.split('-gif ', 1)
        if len(msg_content) == 2:
            content = gif_image(msg_content[1])
            await message.channel.send(content)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")
    
    elif msg_content.startswith('-stkr'):
        msg_content = msg_content.split('-stkr ', 1)
        if len(msg_content) == 2:
            content = stickr_image(msg_content[1])
            await message.channel.send(content)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")
    
    elif msg_content.startswith('-nsfw'):
        msg_content = msg_content.split('-nsfw ', 1)
        if len(msg_content) == 2:
            data = nsfw_search(msg_content[1])
            porn = nsfw_result(data)
            images = nsfw_images(data)
            await message.channel.send(porn)
            for image in images:
                await message.channel.send(image)
        else:
            await message.channel.send("```Error Input or Nothing to search.........```")

    # (To check ping...........)
    elif msg_content.startswith('-ping'):
        await message.channel.send(f'```{round(client.latency * 1000)}ms```')



@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id in (poll[1] for poll in polls):
        msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
        for reaction in msg.reactions:
            if (not payload.member.bot 
                and payload.member in await reaction.users().flatten()
                and reaction.emoji != payload.emoji.name):
                await msg.remove_reaction(reaction.emoji, payload.member)
            elif (reaction.emoji not in option_emojis):
                await msg.remove_reaction(payload.emoji, payload.member)            


keep_alive()
client.run(TOKEN)