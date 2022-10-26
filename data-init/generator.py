import random
import pandas as pd
from os import getcwd

# Generating weather data based on city and date

weather_values = ["hot", "cold"]
location_values = ["London", "NYC"]

year_dates = pd.date_range('2022-10-25', '2023-10-24', freq='D')

weather = [random.choice(weather_values) for _ in range(len(year_dates))]
location = [random.choice(location_values) for _ in range(len(year_dates))]


df = pd.DataFrame(list(zip(weather, location, year_dates)), columns =['Weather', 'Location', 'Date'])

cwd = getcwd()
path = cwd + '/data.csv'
df.to_csv(path, index=False)
