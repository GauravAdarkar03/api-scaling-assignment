from sklearn.preprocessing import StandardScaler, MinMaxScaler 
from FetchandLoadAPI import df

#ScalerInitializer
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

df['temp_normalized'] = min_max_scaler.fit_transform(df[['temperature_2m']]) 
df['wind_standardized'] = standard_scaler.fit_transform(df[['windspeed_10m']])

# Display updated DataFrame
df.head()

print(df.columns)