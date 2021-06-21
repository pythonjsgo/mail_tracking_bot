from datetime import datetime
import pytz
from pochta import tracking

import config

Tracking = tracking.SingleTracker(config.pochta_api_login, config.pochta_api_password)




def short_report(departure_id):
    try:
        history = Tracking.get_history(departure_id)
    except:
        return "Трек код не найден"

    last_event_num = len(history) - 1

    from_country = history[0]["AddressParameters"]["CountryFrom"]["NameRU"]
    # print(history[0]["AddressParameters"])
    dest_country = history[0]["AddressParameters"]["MailDirect"]["NameRU"]

    index = history[0]["AddressParameters"]["DestinationAddress"]["Index"]



    last_event_date = str(history[last_event_num]["OperationParameters"]["OperDate"])[0:16]
    last_event_description = str(history[last_event_num]["OperationParameters"]["OperAttr"]["Name"])



    return f"""
Откуда: {from_country}
Куда: {dest_country} , {index}
    
Последнее событие:
    {last_event_date}  {last_event_description}
    """

def full_report(departure_id):
    try:
        history = Tracking.get_history(departure_id)
    except:
        return "Трек код не найден"

    from_country = history[0]["AddressParameters"]["CountryFrom"]["NameRU"]
    # print(history[0]["AddressParameters"])
    dest_country = history[0]["AddressParameters"]["MailDirect"]["NameRU"]

    index = history[0]["AddressParameters"]["DestinationAddress"]["Index"]
    index_description = history[0]["AddressParameters"]["DestinationAddress"]["Description"]
    dest_name = history[0]["UserParameters"]["Rcpn"]
    from_name = history[0]["UserParameters"]["Sndr"]


    return_string = ""
    for event in history:
        if not str(event["OperationParameters"]["OperAttr"]["Name"]) == "None":
            return_string = return_string  + str(event["OperationParameters"]["OperDate"])[0:16] + "\n"
            return_string = return_string + str(event["OperationParameters"]["OperAttr"]["Name"]) + "\n\n"

            print(return_string)

    return f"""
Откуда: {from_country}
Куда: {dest_country} , {index} , {index_description}
От кого: {from_name}
Кому: {dest_name}

    
События:
{return_string}"""