from flask import Flask, render_template, jsonify
import pandas as pd
from analysis import (
    get_basic_statistics,
    analyze_price_by_beds_baths,
    analyze_size_by_beds_baths,
    analyze_correlations,
    visualize_price_trends,
    detect_outliers
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/analysis', methods=['GET'])
def get_analysis():
    data_file = 'data/zillow_listings.csv'
    df = pd.read_csv(data_file)

    basic_stats = get_basic_statistics(data_file)
    price_analysis = analyze_price_by_beds_baths(data_file)
    size_analysis = analyze_size_by_beds_baths(data_file)
    correlations = analyze_correlations(data_file)
    visualize_price_trends(data_file)
    outliers = detect_outliers(data_file)

    result = {
        "basic_statistics": basic_stats.to_dict(),
        "price_analysis": price_analysis.to_dict(),
        "size_analysis": size_analysis.to_dict(),
        "correlations": correlations.to_dict(),
        "outliers": outliers.to_dict()
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
