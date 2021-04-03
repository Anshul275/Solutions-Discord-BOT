import requests
import json

def filter_data(data):
    web_data = ""
    if len(data) == 0:
        web_data = "```No info related to given topic found on Web........```\n"
    else:
        web_data = "Some useful info from the Web......\n"
        for item in range(len(data)):
            web_data += str(item + 1)
            web_data += ".    " + data[item]['title'] + "\n"
            web_data += data[item]['link'] + "\n\n"
            
    return web_data

def web_search(url, search):
    query = {"q": search, "pageNumber": "1", "pageSize": "5", "autoCorrect": "true"}
    headers = {
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers = headers, params = query)
    json_data = json.loads(response.text)
    
    search_list = json_data['value']

    data_send = []
    for i in range(min(len(search_list), 5)):
        obj = {}
        obj['title'] = search_list[i]['title']
        obj['link'] = search_list[i]['url']
        data_send.append(obj)

    return data_send

def web_result(search):
    mainSite = "https://contextualwebsearch-websearch-v1.p.rapidapi.com"
    endpoint = "/api/Search/WebSearchAPI"

    url = mainSite + endpoint
    web_data = []

    try:
        web_data = web_search(url, search)
    except:
        print("Server doesn't respond to requests........")
    
    # Return the string after filtering google_data
    formatted_data = filter_data(web_data)
    return formatted_data