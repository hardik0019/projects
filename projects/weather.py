import requests
import json

city_name = "Zirakpur"
API_key = "093446554f7d4cf8a9414a2fc7b43f12"
response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=metric")

data = response.json()

with open("response.json", "w") as file:
    json.dump(data, file, indent=4)

print(f"Today's temperature is: {data['list'][0]['main']['temp']}")


 