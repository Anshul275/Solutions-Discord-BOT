import requests
import json

def filter_search_query(search) :
    mod_search = ""
    for ch in search:
        if ch == ' ':
            mod_search += "%20"
        else :
            mod_search += ch;
    return mod_search

def filter_data_gsearch(data):
    google_data = ""
    if len(data) == 0:
        google_data = "```No info related to given topic found on Google........```\n"
    else:
        google_data = "Some useful info from Google......\n"
        for item in range(len(data)):
            google_data += str(item + 1)
            google_data += ".    " + data[item]['title'] + "\n"
            google_data += data[item]['description'] + "\n"
            google_data += "***Link*** - " + data[item]['link'] + "\n\n"
            
    return google_data

def search_google(url, search):
    search = filter_search_query(search)
    url += "q="+ search + "&num=100"
    headers = {
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }
    response = requests.get(url, headers = headers)
    json_data = json.loads(response.text)

    search_list = json_data['results']

    data_send = []
    for i in range(min(len(search_list), 5)):
        obj = {}
        obj['title'] = search_list[i]['title']
        obj['description'] = search_list[i]['description']
        obj['link'] = search_list[i]['link']
        data_send.append(obj)

    return data_send

def google_result(search):
    mainSite = "https://google-search3.p.rapidapi.com"
    endpoint = "/api/v1/search/"

    url = mainSite + endpoint
    google_data = []

    try:
        google_data = search_google(url, search)
    except:
        print("Server doesn't respond to requests........")

    # Return the string after filtering google_data
    formatted_data = filter_data_gsearch(google_data)

    return formatted_data

def search_google_images(url, search):
    search = filter_search_query(search)
    url += "q=" + search
    headers = {
        'x-rapidapi-host': "google-search3.p.rapidapi.com",
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42"
    }

    response = requests.request("GET", url, headers=headers)
    json_data = json.loads(response.text)

    search_list = json_data['image_results']
    
    data_send = []

    for ele in range(min(len(search_list), 10)):
        data_send.append(search_list[ele]['image']['src'])

    return data_send

def google_image_result(search):
    mainSite = "https://google-search3.p.rapidapi.com"
    endpoint = "/api/v1/images/"

    url = mainSite + endpoint
    images_data = []

    try:
        images_data = search_google_images(url, search)
    except:
        print("Server doesn't respond to requests........")

    return images_data

def filter_data_gnews(data):
    news_data = ""
    if len(data) == 0:
        news_data = "```No info related to given topic found on Google........```\n"
    else:
        news_data = "Top News on Google......\n"
        for item in range(len(data)):
            news_data += str(item + 1)
            news_data += ".    **" + data[item]['title'] + "**\n"
            news_data += "Link - " + data[item]['link'] + "\n\n"

    return news_data

def news_google(url, search):
    search = filter_search_query(search)
    url += "q="+ search + "&num=100"
    headers = {
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }
    response = requests.get(url, headers = headers)
    json_data = json.loads(response.text)

    search_list = json_data['entries']

    data_send = []
    for i in range(min(len(search_list), 5)):
        obj = {}
        obj['title'] = search_list[i]['title']
        obj['link'] = search_list[i]['link']
        data_send.append(obj)

    return data_send

def google_news_result(search):
    mainSite = "https://google-search3.p.rapidapi.com"
    endpoint = "/api/v1/news/"

    url = mainSite + endpoint
    news_data = []

    try:
        news_data = news_google(url, search)
    except:
        print("Server doesn't respond to requests........")

    # Return the string after filtering google_data
    formatted_data = filter_data_gnews(news_data)

    return formatted_data