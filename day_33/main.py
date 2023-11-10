import requests
import datetime as dt

# iss code
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# print(response.json())
# print(response.json()["iss_position"])



# sunrise ans sunset code
MY_LAT = "22.572645"
MY_LAN = "88.363892"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LAN,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
# print(sunrise,sunrise)
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
time_now = dt.datetime.now()
print(time_now)












