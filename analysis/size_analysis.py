import pandas as pd

def analyze_size_by_beds_baths(file_path):
    df = pd.read_csv(file_path)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Group by beds and baths
    beds_group = df.groupby('beds').agg({
        'area': ['mean', 'median', 'min', 'max']
    })

    baths_group = df.groupby('baths').agg({
        'area': ['mean', 'median', 'min', 'max']
    })

    print("Size Analysis by Bedrooms:\n", beds_group)
    print("Size Analysis by Bathrooms:\n", baths_group)

    # Save the analysis to CSV files
    beds_group.to_csv('data/size_by_beds.csv')
    baths_group.to_csv('data/size_by_baths.csv')
