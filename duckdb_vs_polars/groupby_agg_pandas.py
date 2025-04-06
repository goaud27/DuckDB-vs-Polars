import pandas as pd

def groupby_agg_pandas(file_path):
	df = pd.read_csv(file_path)
	return df.groupby(['VendorID', 'payment_type']) \
	.agg({'total_amount': ['sum', 'mean', 'min', 'max']})

if __name__ == '__main__':
    print(groupby_agg_pandas('data/2021_Yellow_Taxi_Trip_Data.csv'))