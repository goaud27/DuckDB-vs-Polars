import pathlib
import pandas as pd

def window_func_pandas(file_path):
	
	p = pathlib.Path('.')
	files = p.glob(file_path)

	dfs = []
	for file in files:
		df_ = pd.read_parquet(file)
		dfs.append(df_)

	df = pd.concat(dfs, ignore_index=True)

	df_window = pd.DataFrame()
	
	df_window['avg_fare_per_vendor'] = df.groupby('VendorID')['fare_amount'].transform('mean')
	df_window['ttl_amt_rank_per_pay_type'] = df.groupby('payment_type')['total_amount'] \
	.rank(method='dense', ascending=False)
	
	return df_window

if __name__ == '__main__':
    print(window_func_pandas('data/yellow_tripdata_2021-*.parquet'))