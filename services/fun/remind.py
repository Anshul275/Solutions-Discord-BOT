def filter_reminder_data(data):
    temp_list = data.split("'")
    reminder = ""
    seconds = 0
    try: 
        seconds = int(temp_list[1])
        try:
            reminder = temp_list[3]
        except:
            reminder = ""
    except:
        seconds = -1
    
    return seconds, reminder