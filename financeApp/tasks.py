import yfinance as yf
from datetime import datetime
import json

def fetch_and_store_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="10y")
        hist.index = hist.index.tz_localize(None)

        hist.index = hist.index.strftime('%Y-%m-%d')

        json_data = hist.reset_index().to_dict(orient='records')

        print(f"Data fetched from Yahoo Finance and converted to JSON for {ticker}:")
        print(json.dumps(json_data[:5], indent=2))  # Print the first 5 records to check

        print(f"Fetched and converted historical data at {datetime.now()}")

        return json_data
    except Exception as e:
        print(f"Error in fetch_and_store_data for {ticker}: {e}")
        return None
