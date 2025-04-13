import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_output(data):
    
    sns.set_style(style=None)
    df = pl.DataFrame(data, schema=['time in seconds', 'query type', 'library'])
    plt.figure(figsize=(20, 9))
    ax = sns.barplot(
        df,
        x='query type', 
        y='time in seconds', 
        hue='library', 
        errorbar=None, 
        #palette=['#FFF208', '#760066', '#075AFE', '#C49E85']
        palette=['#c9cba3', '#ffe1a8', '#e26d5c', '#723d46']#, '472d30']
    )
    
    for container in ax.containers:
        ax.bar_label(container)

    ax.set(xlabel='', ylabel='Time in Seconds')
    plt.title('DuckDB vs Modin[Ray] vs Pandas vs Polars - Speed Comparison (Parquet)')
    plt.savefig('output_parquet_2021.png')
    plt.show()