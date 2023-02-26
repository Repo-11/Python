import requests
from twilio.rest import Client

account_sid = "AC29b90230f83ecb2ec40116cb5de7e16c"
auth_token = "099104ede72c293d42b7c5aba809853b"
LAT = 46.155816
LON = 22.382693
api_Key = "61ca813000ed65d8b6cc375ac288fabf"
weather_params = {
    "lat" : LAT,
    "lon" : LON,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_Key,


}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12] #[:position] this is a slicing technique to slice data till that position

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code<700:
        will_rain = True

if will_rain :
    client = Client(account_sid,auth_token)
    message = client.messages \
            .create(
            body = "It's going to rain today . Remember to an umbrella ☂️",
            from_='+16812532298',
            to='+919135989874'


    )


