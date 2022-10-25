import random
import pandas as pd
from os import getcwd

# Generating weather data based on city and date

weather_values = ["hot", "cold"]
location_values = ["London", "NYC"]

year_dates = pd.date_range('2021-01-01', '2021-12-31', freq='D')

weather = [random.choice(weather_values) for i in range(len(year_dates))]
location = [random.choice(location_values) for i in range(len(year_dates))]


df = pd.DataFrame(list(zip(weather, location, year_dates)), columns =['Weather', 'Location', 'Date'])

cwd = getcwd()
path = cwd + '/data.csv'
df.to_csv(path, index=False)
