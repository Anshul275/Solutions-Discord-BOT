import requests
import json


def iplookup_result(search):
    url = "https://weatherapi-com.p.rapidapi.com/ip.json"
    ip_data = ""

    try:
        query = {
            'q': search
        }
        headers = {
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
            'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42"
        }
        response = requests.get(url, headers = headers, params = query)
        json_data = json.loads(response.text)

        ip_data += "**Provided IP's info** ------>\n"
        ip_data += "```"
        if(json_data['city']):
            ip_data += "City : " + json_data['city'] + "\n"
        if(json_data['region']):
            ip_data += "Region : " + json_data['region'] + "\n"
        if(json_data['country_name']):
            ip_data += "Country : " + json_data['country_name'] + "\n"
        if(json_data['continent_name']):
            ip_data += "Continent : " + json_data['continent_name'] + "\n"
        if(json_data['localtime']):
            ip_data += "Local Time : " + json_data['localtime'] + "\n"
        if(json_data['lon']):
            ip_data += "Longitude : " + str(json_data['lon']) + "\n"
        if(json_data['lat']):
            ip_data += "Latitude : " + str(json_data['lat'])
        ip_data += "```"

    except:
        ip_data = ""
        print("Server doesn't respond to requests........")

    return ip_data