import pandas as pd
import matplotlib.pyplot as plt

def visualize_price_trends(file_path):
    df = pd.read_csv(file_path)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Price trend by number of bedrooms
    plt.figure(figsize=(10, 6))
    df.groupby('beds')['price'].mean().plot(kind='bar', color='skyblue')
    plt.title('Average Price by Number of Bedrooms')
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Average Price ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('data/price_by_beds.png')
    plt.show()

    # Price trend by number of bathrooms
    plt.figure(figsize=(10, 6))
    df.groupby('baths')['price'].mean().plot(kind='bar', color='salmon')
    plt.title('Average Price by Number of Bathrooms')
    plt.xlabel('Number of Bathrooms')
    plt.ylabel('Average Price ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('data/price_by_baths.png')
    plt.show()

    # Scatter plot for Price vs Area
    plt.figure(figsize=(10, 6))
    plt.scatter(df['area'], df['price'], alpha=0.5, color='green')
    plt.title('Price vs Area')
    plt.xlabel('Area (sqft)')
    plt.ylabel('Price ($)')
    plt.tight_layout()
    plt.savefig('data/price_vs_area.png')
    plt.show()
