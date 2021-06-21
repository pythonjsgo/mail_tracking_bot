from datetime import datetime

import pytz
from isodate import FixedOffset
from pochta import tracking

import config

Tracking = tracking.SingleTracker(config.pochta_api_login, config.pochta_api_password)

history = Tracking.get_history('LC626892332CN')

from_country = history[0]["AddressParameters"]["CountryFrom"]["NameRU"]
# print(history[0]["AddressParameters"])
dest_country = history[0]["AddressParameters"]["MailDirect"]["NameRU"]

index = history[0]["AddressParameters"]["DestinationAddress"]["Index"]
index_description  =  history[0]["AddressParameters"]["DestinationAddress"]["Description"]
dest_name = history[0]["UserParameters"]["Rcpn"]
from_name = history[0]["UserParameters"]["Sndr"]
print("Откуда: " + from_country + " Куда: " + dest_country, index, "\n", dest_name, "\n", from_name)




import pytz

local_tz = pytz.timezone('Europe/Moscow')

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt) # .normalize might be unnecessary

def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z')




print(aslocaltimestr(datetime(2021, 6, 9, 16, 33, 52)))