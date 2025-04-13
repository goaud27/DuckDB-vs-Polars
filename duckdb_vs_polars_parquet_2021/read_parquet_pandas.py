import pathlib
import pandas as pd

def read_parquet_pandas(file_path):
	
	p = pathlib.Path('.')
	files = p.glob(file_path)

	dfs = []
	for file in files:
		df_ = pd.read_parquet(file)
		dfs.append(df_)

	df = pd.concat(dfs, ignore_index=True)
	return df

if __name__ == '__main__':
    print(read_parquet_pandas('data/yellow_tripdata_2021-*.parquet'))