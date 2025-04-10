import os

os.environ["MODIN_ENGINE"] = "dask"

import modin.pandas as pd

def read_csv_modin(file_path):
	df = pd.read_csv(file_path)
	return df

if __name__ == '__main__':
    print(read_csv_modin('data/2021_Yellow_Taxi_Trip_Data.csv'))