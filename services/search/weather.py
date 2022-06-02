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


def weather(url, search):
    weather_data = ""
    image = ""

    search = filter_search_query(search)
    query = {
        'q': search,
        'days': '3'
    }
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42"
    }
    response = requests.get(url, headers = headers, params = query)
    json_data = json.loads(response.text)

    location = json_data['location']
    current = json_data['current']

    image = "https:" + current['condition']['icon']

    weather_data += "`" + current['last_updated'] + "`\n"
    weather_data += "Location : ***" + location['name']
    if(location['region']):
        weather_data += ", " + location['region']
    weather_data += ", " + location['country'] + "***\n"
    weather_data += "Longitude : **" + str(location['lon']) + "**        Latitude : **" + str(location['lat']) + "**\n"
    weather_data += "Temperature : **" + str(current['temp_c']) + "°C** / **" + str(current['temp_f']) + "°F**\n";
    weather_data += "Feels Like : **" + str(current['feelslike_c']) + "°C** / **" + str(current['feelslike_f']) + "°F**\n";
    weather_data += "Weather Condition : **" + current['condition']['text'] + "**\n"
    weather_data += "Humidity : **" + str(current['humidity']) + "%**\n"
    weather_data += "Cloud : **" + str(current['cloud']) + "%**\n"
    weather_data += "Precipitation : **" + str(current['precip_mm']) + " mm**\n"
    weather_data += "Wind Speed : **" + str(current['wind_kph']) + " kph " + current['wind_dir'] + "**\n"
    weather_data += "Visibility : **" + str(current['vis_km']) + " km**\n"
    weather_data += "UV : **" + str(current['uv']) + "**"

    return weather_data, image

def weather_result(search):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    weather_data = ""
    image = ""
    try:
        weather_data, image = weather(url, search)
    except:
        print("Server doesn't respond to requests........")

    return weather_data, image

def forecast(url, search):
    place = ""
    images = []
    forecast_data = []
    
    search = filter_search_query(search)
    query = {
        'q': search,
        'days': '3'
    }
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42"
    }
    response = requests.get(url, headers = headers, params = query)
    json_data = json.loads(response.text)

    location = json_data['location']
    forecast_info = json_data['forecast']['forecastday']

    place = "```"
    place += location['name']
    if(location['region']):
        place += ", " + location['region']
    place += ", " + location['country'] + "```"

    for data in forecast_info:
        day = data['day']

        image = "https:" + day['condition']['icon']
        images.append(image)

        forecast_text = "`" + data['date'] + "`\n"
        forecast_text += "Max Temperature : **" + str(day['maxtemp_c']) + "°C** / **" + str(day['maxtemp_f']) + "°F**\n"
        forecast_text += "Min Temperature : **" + str(day['mintemp_c']) + "°C** / **" + str(day['mintemp_f']) + "°F**\n"
        forecast_text += "Weather Condition : **" + day['condition']['text'] + "**\n"
        forecast_text += "Humidity : **" + str(day['avghumidity']) + "%**\n"
        forecast_text += "Will it rain? ***"
        if(day['daily_will_it_rain']):
            forecast_text += "Yes***\n"
        else:
            forecast_text += "No***\n"
        forecast_text += "Precipitation Chances : **" + str(day['daily_chance_of_rain']) + "%**\n"
        forecast_text += "Will it snow? ***"
        if(day['daily_will_it_snow']):
            forecast_text += "Yes***\n"
        else:
            forecast_text += "No***\n"
        forecast_text += "Snow Chances : **" + str(day['daily_chance_of_snow']) + "%**\n"

        forecast_data.append(forecast_text)
        

    return place, images, forecast_data


def forecast_result(search): 
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    place = ""
    images = []
    forecast_data = []

    try:
        place, images, forecast_data = forecast(url, search)
    except:
        place = ""
        images = []
        forecast_data = []
        print("Server doesn't respond to requests........")

    return place, images, forecast_data

def hourly_forecast(url, search):
    place = ""
    images = []
    hourly_data = []
    
    search = filter_search_query(search)
    query = {
        'q': search,
        'days': '3'
    }
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "9297d52a67mshf8a0356ac53e64bp1ce086jsn7c5c250a4f42"
    }
    response = requests.get(url, headers = headers, params = query)
    json_data = json.loads(response.text)

    location = json_data['location']
    hourly_info = json_data['forecast']['forecastday'][0]['hour']

    place = "```"
    place += location['name']
    if(location['region']):
        place += ", " + location['region']
    place += ", " + location['country'] + "```"

    for data in hourly_info:
        image = "https:" + data['condition']['icon']
        images.append(image)

        hourly = "`" + data['time'] + "`\n"
        hourly += "Temperature : **" + str(data['temp_c']) + "°C** / **" + str(data['temp_f']) + "°F**\n"
        hourly += "Feels Like : **" + str(data['feelslike_c']) + "°C** / **" + str(data['feelslike_f']) + "°F**\n";
        hourly += "Weather Condition : **" + data['condition']['text'] + "**\n"
        hourly += "Humidity : **" + str(data['humidity']) + "**\n"
        hourly += "Wind Speed : **" + str(data['wind_kph']) + " kph " + data['wind_dir'] + "**\n"
        hourly += "Precipitation Chances : **" + str(data['chance_of_rain']) + "%**\n"
        hourly += "Snow Chances : **" + str(data['chance_of_snow']) + "%**\n"
        hourly += "Visibility : **" + str(data['vis_km']) + "km**\n"
        hourly += "UV : **" + str(data['uv']) + "**\n"

        hourly_data.append(hourly)

    return place, images, hourly_data

def hourly_forecast_result(search):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    place = ""
    images = []
    hourly_data = []

    try:
        place, images, hourly_data = hourly_forecast(url, search)
    except:
        place = ""
        images = []
        hourly_data = []
        print("Server doesn't respond to requests........")

    return place, images, hourly_data