import polars as pl 

def agg_polars(file_path):
    lf = pl.scan_parquet(file_path)
    return (
        lf
        .select(
            sum=pl.col('total_amount').sum(),
            avg=pl.col('total_amount').mean(),
            min=pl.col('total_amount').min(),
            max=pl.col('total_amount').max()
        )
        .collect()
    )

if __name__ == '__main__':
    print(agg_polars('data/yellow_tripdata_2021-*.parquet'))