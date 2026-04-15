# api-scaling-assignment

Task 1 — Fetch and Load API Data

Call the Open-Meteo API for any city of your choice using the endpoint below. Parse the JSON response and load the hourly temperature_2m and windspeed_10m values into a Pandas DataFrame.

https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m,windspeed_10m
Your DataFrame must have:

A time column (from the response)
A temperature_2m column
A windspeed_10m column
Print the first 5 rows using .head().


------------------------Task 2---------------------------------------

Task 2 — Apply Feature Scaling

Using the DataFrame from Task 1:

Apply MinMaxScaler to the temperature_2m column and StandardScaler to the windspeed_10m column. Add the results as two new columns: temp_normalized and wind_standardized.
Print the updated DataFrame's first 5 rows.
In a markdown cell, write 2–3 sentences explaining why you chose MinMaxScaler for temperature and StandardScaler for wind speed.