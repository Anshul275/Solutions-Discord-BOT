import requests
import json
import random

def filter_href(data):
    link = ""
    for ch in data:
        if ch == ' ':
          link += "%20"
        else :
          link += ch
    return link

def search_nasa(url, search):
    query = {'q': search}
    response = requests.get(url, params = query)
    json_data = json.loads(response.text)

    image_list = json_data['collection']['items']
    
    nasa_text = ""
    nasa_image = ""
    if len(image_list) >= 1:
        image = random.choice(image_list)
        nasa_text = image['data'][0]['description'] + "\n"
        nasa_image = filter_href(image['links'][0]['href'])
    else:
        nasa_image = "```No related images from NASA........```\n"

    return nasa_text, nasa_image


def nasa_image(search):
    mainSite = "https://images-api.nasa.gov/"
    endpoint = "/search"

    url = mainSite + endpoint
    nasa_text = ""
    nasa_image = ""

    try:
        nasa_text, nasa_image = search_nasa(url, search)
    except:
        print("Server doesn't respond to requests........")

    return nasa_text, nasa_image