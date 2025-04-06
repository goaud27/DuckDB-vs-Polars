import pandas as pd

def join_pandas(file_path):
	base_df = pd.read_csv(file_path)
	base_df['pickup_month'] = pd.to_datetime(base_df['tpep_pickup_datetime'] \
	, format='%m/%d/%Y %I:%M:%S %p').dt.month

	join_df = base_df.groupby(['VendorID', 'payment_type', 'pickup_month']) \
	.agg({'total_amount': 'sum'})

	return base_df.merge(join_df,
	on=['VendorID', 'payment_type', 'pickup_month'],
	how='inner')

if __name__ == '__main__':
    print(join_pandas('data/2021_Yellow_Taxi_Trip_Data.csv'))