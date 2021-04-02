import requests
import json
import random

def filter_data(data):
    image = ""
    if len(data) >= 1:
        image = random.choice(data)
    else:
        image = "```Couldn't find related images........```\n"
    return image

def web_search(search):
    mainSite = "https://contextualwebsearch-websearch-v1.p.rapidapi.com"
    endpoint = "/api/Search/ImageSearchAPI"

    url = mainSite + endpoint
    query = {
        "q": search,
        "pageNumber": "1",
        "pageSize": "20",
        "autoCorrect":"true"
    }
    headers = {
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers = headers, params = query)

    image_data = []
    json_data = json.loads(response.text)
    images = json_data['value']
    for image in images:
        image_data.append(image['url'])
    
    return image_data

def bing_search(search):
    mainSite = "https://bing-image-search1.p.rapidapi.com"
    endpoint = "/images/search"

    url = mainSite + endpoint
    query = {'q': search, "count":"20"}
    headers = {
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
    }

    response = requests.get(url, headers = headers, params = query)

    image_data = []
    if response.status_code == 200:
        json_data = json.loads(response.text)
        images = json_data['value']
        for image in images:
            image_data.append(image['contentUrl'])
            
        if len(image_data) == 0:
            image_data = web_search(search)
    else:
        image_data = web_search(search)

    return image_data

def img_result(search):
    image_data = []
    try:
        image_data = bing_search(search)
    except:
        print("Server doesn't respond to requests........")
    
    formatted_data = filter_data(image_data)

    return formatted_data