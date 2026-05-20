import requests
from datetime import datetime

response = requests.get("https://wttr.in/Seattle?format=j1")
data = response.json()

current = data["current_condition"][0]

temp_f = current["temp_F"]
feels_like = current["FeelsLikeF"]
humidity = current["humidity"]
description = current["weatherDesc"][0]["value"]

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = f"""Seattle Weather Report
Generated: {now}
---------------------
Temperature: {temp_f}°F
Feels Like: {feels_like}°F
Humidity: {humidity}%
Conditions: {description}
"""

file = open("weather_report.txt", "w")
file.write(report)
file.close()

print("Weather report saved to weather_report.txt")