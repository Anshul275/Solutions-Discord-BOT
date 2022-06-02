import requests
import json
import random

API_KEY = "zEVaIxFAhZhWzPakjs9XsN0xdmZ3vDJg"

def trend_sticker(mainSite):
    endpoint = "/v1/stickers/trending"
    url = mainSite + endpoint
    query = {'api_key': API_KEY, 'limit': 20}

    response = requests.get(url, params = query)
    json_data = json.loads(response.text)
    
    sticker_list = json_data['data']

    sticker = ""
    if len(sticker_list) >= 1:
        sticker_data = random.choice(sticker_list)
        sticker = sticker_data['images']['original']['url']
    else:
        sticker = "```No related sticker on Giphy........```\n"

    return sticker

def search_sticker(mainSite, search):
    endpoint = "/v1/stickers/search"
    url = mainSite + endpoint
    query = {'q': search, 'api_key': API_KEY}

    response = requests.get(url, params = query)
    json_data = json.loads(response.text)
    
    sticker_list = json_data['data']

    sticker = ""
    if len(sticker_list) >= 1:
        sticker_data = random.choice(sticker_list)
        sticker = sticker_data['images']['original']['url']
    else:
        sticker = "```No related gif on Tenor........```\n"

    return sticker


def sticker_image(search):
    mainSite = "https://api.giphy.com"

    stickr = ""

    if search == "trend":
        try:
            stickr = trend_sticker(mainSite)
        except:
            print("Server doesn't respond to requests........")
    else:
        try:
            stickr = search_sticker(mainSite, search)
        except:
            print("Server doesn't respond to requests........")

    return stickr