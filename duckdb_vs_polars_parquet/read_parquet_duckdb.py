import duckdb

def read_parquet_duckdb(file_path):
    query = f'''
        select * from "{file_path}";
    '''
    return duckdb.sql(query).arrow()

if __name__ == '__main__':
    print(read_parquet_duckdb('data/yellow_tripdata_*.parquet'))