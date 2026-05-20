file = open("weather_multi.txt", "w")
file.write("\nWeather for Multiple Cities\n")
file.close()


file=open("weather_multi.txt","r")
print(file.read())
file.close()

import requests
from datetime import datetime

def get_weather(city):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    data = response.json()
    current = data["current_condition"][0]
    
    temp_f = current["temp_F"]
    feels_like = current["FeelsLikeF"]
    humidity = current["humidity"]
    description = current["weatherDesc"][0]["value"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""{city} Weather Report
Generated: {now}
---------------------
Temperature: {temp_f}°F
Feels Like: {feels_like}°F
Humidity: {humidity}%
Conditions: {description}

"""
    return report

combined = get_weather("Bellingham")
combined += get_weather("Denver")
combined += get_weather("Salt_Lake_City")

file = open("weather_multi.txt", "w")
file.write(combined)
file.close()

print("Report saved.")