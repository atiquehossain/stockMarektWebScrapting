import yfinance as yf
from datetime import datetime
import pandas as pd
import json

def fetch_and_store_data():
    try:
        aapl = yf.Ticker('AAPL')
        hist = aapl.history(period="5y")
        hist.index = hist.index.tz_localize(None)

        # Convert the index (which is the date) to a string format
        hist.index = hist.index.strftime('%Y-%m-%d')

        # Convert DataFrame to JSON format
        json_data = hist.reset_index().to_dict(orient='records')

        # Debugging print statements
        print("Data fetched from Yahoo Finance and converted to JSON:")
        print(json.dumps(json_data[:5], indent=2))  # Print the first 5 records to check

        print(f"Fetched and converted historical data at {datetime.now()}")

        # Return the JSON data
        return json_data
    except Exception as e:
        print(f"Error in fetch_and_store_data: {e}")
        return None
