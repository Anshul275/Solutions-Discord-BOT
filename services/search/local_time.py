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

def localTime(url, search):
    local_time = ""
    search = filter_search_query(search)
    query = {
        'q': search
    }
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42"
    }
    response = requests.get(url, headers = headers, params = query)
    json_data = json.loads(response.text)

    local_data = json_data['location']

    local_time += "Location : **" + local_data['name'] 
    if (local_data['region'] != ""):
        local_time += ", " + local_data['region']
    
    if (local_data['country'] != ""):
        local_time += ", " + local_data['country']

    local_time += "**\n"

    local_time += "Longitude : **" + str(local_data['lon']) + "**        Latitude : **" + str(local_data['lat']) + "**\n"

    local_time += "```Local Time : " + local_data['localtime'] + "```\n"

    return local_time

def local_time_result(search):
    url = "https://weatherapi-com.p.rapidapi.com/timezone.json"
    local_time = ""

    try:
        local_time = localTime(url, search)
    except:
        print("Server doesn't respond to requests........")

    return local_time