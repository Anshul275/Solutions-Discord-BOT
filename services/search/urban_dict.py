import requests
import json


def dict_search(search):

    definition = ""

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term": search}

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42"
    }

    try:
        response = requests.get(url, headers = headers, params = querystring)

        json_data = json.loads(response.text)
        result = json_data['list']
        
        idx = []
        for i in range(0, len(result)):
            ele1 = result[i]['thumbs_up']
            ele2 = result[i]['thumbs_down']
            ans = 0.0
            if (ele2 == 0):
                ans = ele1
            else:
                ans = ele1 / ele2
            idx.append(ans)

        j = -1
        c = 0

        for i in range(0,min(2, len(result))):
            maxi = -1
            max_ptr = -1
            for i in range(len(result)):
                if(idx[i] > maxi and i != j):
                    maxi = idx[i]
                    max_ptr = i

            definition += "```Word " + str(c+1) + " : " + result[max_ptr]['word'] + "```\n"
            definition += "```" + result[max_ptr]['definition'] + "```\n"
            definition += "Example : \n" + result[max_ptr]['example'] + "\n\n"

            c += 1
            j = max_ptr

    except:
        definition = ""

    return definition