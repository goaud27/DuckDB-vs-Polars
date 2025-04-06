import pandas as pd

def agg_pandas(file_path):
	df = pd.read_csv(file_path)
	return df.agg({'total_amount': ['sum', 'mean', 'min', 'max']})

if __name__ == '__main__':
    print(agg_pandas('data/2021_Yellow_Taxi_Trip_Data.csv'))