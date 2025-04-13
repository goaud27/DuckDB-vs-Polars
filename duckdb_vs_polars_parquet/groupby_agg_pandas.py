import pathlib
import pandas as pd

def groupby_agg_pandas(file_path):

	p = pathlib.Path('.')
	files = p.glob(file_path)

	dfs = []
	for file in files:
		df_ = pd.read_parquet(file)
		dfs.append(df_)

	df = pd.concat(dfs, ignore_index=True)
	return df.groupby(['VendorID', 'payment_type']) \
	.agg({'total_amount': ['sum', 'mean', 'min', 'max']})

if __name__ == '__main__':
    print(groupby_agg_pandas('data/yellow_tripdata_*.parquet'))