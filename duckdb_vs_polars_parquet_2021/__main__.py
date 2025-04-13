import importlib
import pathlib
import time
from visualize_output import visualize_output

def main():
    file_path = 'data/yellow_tripdata_2021-*.parquet'
    outputs = []
    this_dir = pathlib.Path(__file__).parent

    exts = ['*duckdb.py', '*polars.py', '*pandas.py']
    libs = []
    for ext in exts:
        libs.extend(this_dir.glob(ext))

    for benchmark in sorted(libs):
        module_name = func_name = benchmark.with_suffix('').name
        module = importlib.import_module(module_name)
        benchmark_function = getattr(module, func_name)
        query_type = '_'.join(func_name.split('_')[:-1])
        library = func_name.split('_')[-1]

        start = time.time()
        benchmark_function(file_path)
        end = time.time()
        seconds = round(end - start, 2)
        print(func_name, seconds)

        output = [seconds, query_type, library]
        outputs.append(output)
    
    visualize_output(outputs)

if __name__ == '__main__':
    main()