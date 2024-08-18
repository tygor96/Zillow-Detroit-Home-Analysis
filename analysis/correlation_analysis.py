import pandas as pd


def analyze_correlations(data_file):
    # Load the data from the CSV file
    df = pd.read_csv(data_file)

    # Clean the data, converting price to a numeric type
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['price_per_sqft'] = df['price'] / df['area']

    # Select only numeric columns for correlation analysis
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()

    print("Correlation Matrix:\n", correlation_matrix)

    return correlation_matrix