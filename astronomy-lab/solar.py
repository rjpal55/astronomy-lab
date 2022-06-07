#!/usr/bin/env python3
import requests
import json
from pprint import pprint
from datetime import date, timedelta

dt=date.today()
next_day=timedelta(1)
next_day=dt + next_day

aid="6bcbd9f0-ce29-4a40-bd20-85c133141253"
asecret="4087804616dbb520cd3997d549b1cdb6300af0888d94925a5988bb32ea241a65ce246b5f777ee03b5f3dd5d143fd032139bbd1c2efd5f1bf8fbf236b5058281581d52391cc4d878c0679aa810bf04ae2a29723073f75ee396f45c6bee8855202b7ef02968a3a6b83e642adb303bbaa6a"

def get_location():
    r = requests.get('http://ip-api.com/json/136.184.80.77')
    data = r.json()
    lat = data['lat']
    lon = data['lon']
    return lat, lon

loc=get_location()
lat=None
lon=None
try:
    if loc:
        lat=loc[0]
        lon=loc[1]
except Exception as e:
    print(e)

# print(lat,lon)

def get_sun_position(latitude,longitude):
    # global dt,asecret,next_day
    url = f"https://api.astronomyapi.com/api/v2/bodies/positions/sun"
    param = {
        "latitude":latitude,
        "longitude":longitude,
        "from_date":dt,
        "to_date":next_day,
        "elevation":"2",
        "time":"08:00:00"
    }
    headers = {
        "Authorization":"Basic {hash}"
    }
    r=requests.get(url, auth=(aid,asecret), params=param, headers=headers)
    location = r.json()
    # pprint(location)
    for i,data in enumerate(location["data"]["table"]['rows']):
        if location["data"]["table"]['rows'][i]["cells"][0]['id'] == "sun":
            azi = location["data"]["table"]['rows'][i]["cells"][0]['position']['horizonal']['azimuth']['degrees']
            alt = location["data"]["table"]['rows'][i]["cells"][0]['position']['horizonal']['altitude']['degrees']
        return azi, alt
try:
    sun=get_sun_position(lat,lon)
    # print(sun)
except Exception as e:
    print(f'Unable to index {e}')

sun=get_sun_position(lat,lon)
azi=sun[0]
alt=sun[1]
    
def print_sun_position(lat,lon):
    # return f'The sun in currently at {azi} degress azimuth, {alt} degress altitude.'
    print (f'The sun in currently at {azi} degress azimuth, {alt} degress altitude.')

print_sun_position(azi,alt)
# res = print_sun_position(azi,alt)
# print(res)



