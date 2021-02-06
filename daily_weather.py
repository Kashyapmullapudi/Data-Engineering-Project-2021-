from pymongo import MongoClient
import requests
client = MongoClient('mongodb+srv://admin:raichu554@cluster0.iwukc.mongodb.net/weather_climate?retryWrites=true&w=majority')
db_name = client.weather_climate
collection = db_name.daily_weather

forecast = f'https://api.openweathermap.org/data/2.5/onecall?lat=49.4883&lon=8.4647&exclude=minutely&appid=e989c1652907feb4f3b7ce8ade5977b0'
response = requests.get(forecast).json()
print(response)

results = response['daily']
for result in results:
    collection.insert_one(result)