import requests
from twilio.rest import Client

account_sid = 'ACc265df6b95b0895c5b482c26ead576c2'
auth_token = 'ecc8aef2db6d87525db42a06944368b6'
client = Client(account_sid, auth_token)

open_weather_end = "https://api.openweathermap.org/data/2.5/weather"

api_key = "5392e8d8236ee11526d7a2a3eb9a321a"
parameter = {
    "lat": 28.25,
    "lon": 77.1667,
    "appid": api_key
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
