import pandas as pd


def detect_outliers(data_file):
    # Load the data from the CSV file
    df = pd.read_csv(data_file)

    # Clean the price column by removing dollar signs and commas, and converting to float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Calculate Q1 (25th percentile) and Q3 (75th percentile) for price
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1

    # Define the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]

    return outliers, lower_bound, upper_bound