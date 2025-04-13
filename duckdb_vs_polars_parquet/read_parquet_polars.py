import polars as pl

def read_parquet_polars(file_path):
    lf = pl.scan_parquet(file_path)
    return lf.collect()

if __name__ == '__main__':
    print(read_parquet_polars('data/yellow_tripdata_*.parquet'))