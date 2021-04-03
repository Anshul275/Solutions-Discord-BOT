option = [":one:", ":two:", ":three:", ":four:", ":five:",
		   ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:"]


def filter_poll_data(data):
    temp_list = data.split("'")
    question = ""
    seconds = 0
    options = []
    try: 
        seconds = int(temp_list[1])
        try:
            question = temp_list[3]
            if len(temp_list) > 5:
                i = 5
                while(i < len(temp_list)):
                    options.append(temp_list[i])
                    i += 2
        except:
            question = ""
    except:
        seconds = -1

    return seconds, question, options

def getOptions(data):
    options = ""
    for i in range(0, len(data)):
        options += "\n" + option[i] + " " + data[i]
    return options