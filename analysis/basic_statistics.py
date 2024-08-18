import pandas as pd

def get_basic_statistics(file_path):
    df = pd.read_csv(file_path)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    stats = df.describe()
    print("Basic Statistics:\n", stats)

    # Save the statistics to a CSV file
    stats.to_csv('data/basic_statistics.csv')
