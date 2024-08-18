import pandas as pd

def analyze_price_by_beds_baths(file_path):
    df = pd.read_csv(file_path)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Group by beds and baths
    beds_group = df.groupby('beds').agg({
        'price': ['mean', 'median', 'min', 'max']
    })

    baths_group = df.groupby('baths').agg({
        'price': ['mean', 'median', 'min', 'max']
    })

    print("Price Analysis by Bedrooms:\n", beds_group)
    print("Price Analysis by Bathrooms:\n", baths_group)

    # Save the analysis to CSV files
    beds_group.to_csv('data/price_by_beds.csv')
    baths_group.to_csv('data/price_by_baths.csv')
