import requests
import config
from twilio.rest import Client


client = Client(config.account_sid, config.auth_token)

open_weather_end = "https://api.openweathermap.org/data/2.5/weather"


parameter = {
    "lat": 28.25,
    "lon": 77.1667,
    "appid": config.api_key
}
response = requests.get(url=open_weather_end, params=parameter)
get = response.json()
temp_details = get["main"]
answer = temp_details["temp_max"]
final_answer = round(answer - 272.15, 2)
print(final_answer)
if 32 >= final_answer >= 27:
    message = client.messages.create(
        messaging_service_sid='MGd7f0da829b3b71ad063ceb891c036828',
        body='Today weather would be good not much heat 👋',
        to='+919643703213'
    )
elif 32 < final_answer <= 40:
    message = client.messages.create(
        messaging_service_sid='MGd7f0da829b3b71ad063ceb891c036828',
        body='Today weather would be hot 👋 ',
        to='+919643703213'
    )
elif final_answer >= 40:
    message = client.messages.create(
        messaging_service_sid='MGd7f0da829b3b71ad063ceb891c036828',
        body='Today weather would be extremely hot 👋 Prevent going out',
        to='+919643703213'
    )
else:
    message = client.messages.create(
        messaging_service_sid='MGd7f0da829b3b71ad063ceb891c036828',
        body='Today weather would be extremely hot 👋 Prevent going out',
        to='+919643703213'
    )

print(message.sid)
# apilist.fun
