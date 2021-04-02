import requests
import json

def fact_search(mainSite, search):
    fact_data = ""

    if search == "random":
        endpoint = "/random/trivia"
        url = mainSite + endpoint
        query = {"fragment": "true", "json": "true"}
        headers = {
            'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
            'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }
        response = requests.get(url, headers = headers, params = query)
        json_data = json.loads(response.text)
        fact_data = "```" + json_data['text'] + " : "
        fact_data += str(json_data['number']) + "```"
        
    else:
        try:
            num_or_year = int(search)
            endpoint = "/" + str(num_or_year) + "/year"
            url = mainSite + endpoint
            query = {"fragment": "true", "json": "true"}
            headers = {
                'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42",
                'x-rapidapi-host': "numbersapi.p.rapidapi.com"
            }
            response = requests.get(url, headers = headers, params = query)
            json_data = json.loads(response.text)
            fact_data = "```" + json_data['text'] + " : "
            fact_data += str(json_data['number']) + "```"
        except ValueError:
            fact_data = "```Invalid Input........```\n"
    return fact_data

def fact_result(search):
    mainSite = "https://numbersapi.p.rapidapi.com"

    fact_data = ""

    try:
        fact_data = fact_search(mainSite, search)
    except:
        print("Server doesn't respond to requests........")

    return fact_data