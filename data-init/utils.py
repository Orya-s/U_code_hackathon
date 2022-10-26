import pandas as pd

# Define data

def pull_data(csv_path):	
	df = pd.read_csv(csv_path, sep=',')
	print(df)
	tuples = [tuple(x) for x in df.values]
	return tuples

#pull_data('./data.csv')