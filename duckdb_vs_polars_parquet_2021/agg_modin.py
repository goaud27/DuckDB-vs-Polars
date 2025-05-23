import os

os.environ["MODIN_ENGINE"] = "ray"

import pathlib
import modin.pandas as pd

def agg_modin(file_path):
	
	p = pathlib.Path('.')
	files = p.glob(file_path)

	dfs = []
	for file in files:
		df_ = pd.read_parquet(file)
		dfs.append(df_)

	df = pd.concat(dfs, ignore_index=True)
	return df.agg({'total_amount': ['sum', 'mean', 'min', 'max']})

if __name__ == '__main__':
    print(agg_modin('data/yellow_tripdata_2021-*.parquet'))