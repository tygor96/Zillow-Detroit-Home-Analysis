from analysis import (
    get_basic_statistics,
    analyze_price_by_beds_baths,
    analyze_size_by_beds_baths,
    analyze_correlations,
    visualize_price_trends,
    detect_outliers
)

def main():
    # Load the data
    data_file = 'data/zillow_listings.csv'

    # Perform basic statistics analysis
    get_basic_statistics(data_file)

    # Perform price analysis
    analyze_price_by_beds_baths(data_file)

    # Perform size analysis
    analyze_size_by_beds_baths(data_file)

    # Perform correlation analysis
    analyze_correlations(data_file)

    # Visualize price trends
    visualize_price_trends(data_file)

    # Detect outliers
    detect_outliers(data_file)

if __name__ == "__main__":
    main()