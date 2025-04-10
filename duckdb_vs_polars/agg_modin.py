import os

os.environ["MODIN_ENGINE"] = "dask"

import modin.pandas as pd

def agg_modin(file_path):
	df = pd.read_csv(file_path)
	return df.agg({'total_amount': ['sum', 'mean', 'min', 'max']})

if __name__ == '__main__':
    print(agg_modin('data/2021_Yellow_Taxi_Trip_Data.csv'))