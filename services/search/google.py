import requests
import json

def filter_data(data):
    google_data = ""
    if len(data) == 0:
        google_data = "```No info related to given topic found on Google........```\n"
    else:
        google_data = "Some useful info from Google......\n"
        for item in range(len(data)):
            google_data += str(item + 1)
            google_data += ".    " + data[item]['title'] + "\n"
            google_data += data[item]['link'] + "\n\n"
            
    return google_data

def search_google(url, search):
    query = {'q': search}
    headers = {
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
        'x-rapidapi-host': "google-search5.p.rapidapi.com"
    }
    response = requests.get(url, headers = headers, params = query)
    json_data = json.loads(response.text)

    search_list = json_data['data']['results']['organic']
    
    data_send = []
    for i in range(min(len(search_list), 5)):
        obj = {}
        obj['title'] = search_list[i]['title']
        obj['link'] = search_list[i]['url']
        data_send.append(obj)

    return data_send

def google_result(search):
    mainSite = "https://google-search5.p.rapidapi.com"
    endpoint = "/google-serps/"

    url = mainSite + endpoint
    google_data = []

    try:
        google_data = search_google(url, search)
    except:
        print("Server doesn't respond to requests........")
    
    # Return the string after filtering google_data
    formatted_data = filter_data(google_data)

    return formatted_data