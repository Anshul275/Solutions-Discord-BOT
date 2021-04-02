import requests
import json
import random

API_KEY = "5J5ZUI3MBTKL"

def trend_gif(mainSite):
    endpoint = "/v1/trending"
    url = mainSite + endpoint
    query = {'key': API_KEY, 'limit': 10, 'media_filter': "minimal"}

    response = requests.get(url, params = query)
    json_data = json.loads(response.text)
    
    gif_list = json_data['results']

    gif = ""
    if len(gif_list) >= 1:
        gif_data = random.choice(gif_list)
        gif = gif_data['media'][0]['gif']['url']
    else:
        gif = "```No trending gif on Tenor........```\n"

    return gif

def search_gif(mainSite, search):
    endpoint = "/v1/search"
    url = mainSite + endpoint
    query = {'q': search, 'key': API_KEY, 'limit': 10, 'media_filter': "minimal"}

    response = requests.get(url, params = query)
    json_data = json.loads(response.text)
    
    gif_list = json_data['results']

    gif = ""
    if len(gif_list) >= 1:
        gif_data = random.choice(gif_list)
        gif = gif_data['media'][0]['gif']['url']
    else:
        gif = "```No related gif on Tenor........```\n"

    return gif


def gif_image(search):
    mainSite = "https://g.tenor.com"

    gif_image = ""

    if search == "trend":
        try:
            gif_image = trend_gif(mainSite)
        except:
            print("Server doesn't respond to requests........")
    else:
        try:
            gif_image = search_gif(mainSite, search)
        except:
            print("Server doesn't respond to requests........")

    return gif_image