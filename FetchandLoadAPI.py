import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m,windspeed_10m"

#FetchData
response = requests.get(url)
data = response.json()

#ExtractRequireData
time = data['hourly']['time']
temperature = data['hourly']['temperature_2m']
windspeed = data['hourly']['windspeed_10m']

#LoadData
df = pd.DataFrame({
    'time': time,
    'temperature_2m': temperature,
    'windspeed_10m': windspeed
})

#Convert time to datetime format
df['time'] = pd.to_datetime(df['time'])

print(df.head())