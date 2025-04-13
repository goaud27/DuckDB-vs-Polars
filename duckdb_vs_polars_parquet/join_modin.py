import os

os.environ["MODIN_ENGINE"] = "ray"

import pathlib
import modin.pandas as pd

def join_modin(file_path):
	
	p = pathlib.Path('.')
	files = p.glob(file_path)

	dfs = []
	for file in files:
		df_ = pd.read_parquet(file)
		dfs.append(df_)

	base_df = pd.concat(dfs, ignore_index=True)
	#base_df['pickup_month'] = pd.to_datetime(base_df['tpep_pickup_datetime'] \
	#, format='%m/%d/%Y %I:%M:%S %p').dt.month
	base_df['pickup_month'] = base_df['tpep_pickup_datetime'].dt.month

	join_df = base_df.groupby(['VendorID', 'payment_type', 'pickup_month']) \
	.agg({'total_amount': 'sum'})

	return base_df.merge(join_df,
	on=['VendorID', 'payment_type', 'pickup_month'],
	how='inner')

if __name__ == '__main__':
    print(join_modin('data/yellow_tripdata_*.parquet'))