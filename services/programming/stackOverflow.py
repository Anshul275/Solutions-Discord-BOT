import requests
import json

def filter_data(data):
    stack_data = ""
    if len(data) == 0:
        stack_data = "```No info related to given topic found on StackOverflow........```\n"
    else:
        stack_data = "Some useful info from StackOverflow......\n"
        for item in range(len(data)):
            stack_data += str(item + 1)
            stack_data += ".    " + data[item]['title'] + "\n"
            stack_data += data[item]['link'] + "\n"
            stack_data += " `  Author  -  " + data[item]['author'] + "  `\n\n"
            
    return stack_data

def search_title(url, search):
    title = {'title': search}

    response = requests.get(url, params = title)
    json_data = json.loads(response.text)

    search_list = json_data['items']
    
    data_send = []
    for i in range(min(len(search_list), 5)):
        obj = {}
        obj['title'] = search_list[i]['title']
        obj['link'] = search_list[i]['link']
        obj['author'] = search_list[i]['owner']['display_name']
        data_send.append(obj)

    return data_send

def search_question(url, search):
    question = {'q': search}

    response = requests.get(url, params = question)
    json_data = json.loads(response.text)

    search_list = json_data['items']
    
    data_send = []
    for i in range(min(len(search_list), 5)):
        obj = {}
        obj['title'] = search_list[i]['title']
        obj['link'] = search_list[i]['link']
        obj['author'] = search_list[i]['owner']['display_name']
        data_send.append(obj)

    return data_send

def stackOverflow_result(search):
    mainSite = "https://api.stackexchange.com"
    endpoint = "/2.2/search/advanced?order=desc&sort=activity&accepted=True&answers=1&site=stackoverflow"

    url = mainSite + endpoint
    stack_data = []

    try:
        stack_data = search_title(url, search)
        if len(stack_data) == 0:
            stack_data = search_question(url, search)
    except:
        print("Server doesn't respond to requests........")
    
    # Return the string after filtering stack_data
    formatted_data = filter_data(stack_data)

    return formatted_data