import requests

response = requests.get("https://wttr.in/seattle?format=j1")

print(response.status_code)
print(type(response))

data = response.json()

print(type(data))
print(data.keys())

current = data["current_condition"][0]

temp_f = current["temp_F"]
feels_like = current["FeelsLikeF"]
humidity = current["humidity"]
description = current["weatherDesc"][0]["value"]


print(f"Seattle Weather Right Now:")
print(f"Temperature: {temp_f}°F")
print(f"Feels Like: {feels_like}°F")
print(f"Humidity: {humidity}%")
print(f"Conditions: {description}")

                                        
