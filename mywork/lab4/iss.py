#!/usr/bin/env python3
# Purpose: build ETL pipeline to extract ISS location data, transform into clean format, and load into CSV file.


# Imports
import sys
import os
import logging
import requests
import pandas as pd


# Initializing logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(message)s'))

logging.basicConfig(level=logging.DEBUG, handlers=[console_handler])

logging.info("Initializing ISS locator...")

logger = logging.getLogger(__name__)

# Extract function: downloads JSON data; returns parsed JSON data
def extract():
    url = "http://api.open-notify.org/iss-now.json"

    try:
        logger.info("Extracting location...")
        response = requests.get(url)
        response.raise_for_status
        data = response.json()
        
        logger.info("Extract successful.")
        
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Extract failed: {e}")
        sys.exit(1)


# Transform function: turns JSON data to single row Pandas df
def transform(data):
    try:
        logger.info("Transforming raw data...")
        timestamp = data["timestamp"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        time = pd.to_datetime(timestamp, unit = "s")

        df = pd.DataFrame({"timestamp": [timestamp], "datetime": [time], "latitude": [latitude], "longitude": [longitude]})

        logger.info("Transform successful.")

        return df
    except Exception as e:
        logger.error(f"Transform failed: {e}")
        sys.exit(1)



# Load function: appends transformed data to specified file
def load(df, filename):
    try:
        logger.info("Loading ISS data...")
        exists = os.path.exists(filename)
        df.to_csv(filename, mode = "a", header = not exists, index = False)
        logger.info(f"Load successful. Data saved to {filename}.")
    except Exception as e:
        logger.error(f"Load failed: {e}")
        sys.exit(1)

# Main function: performs ETL functions
def main():
    if len(sys.argv) != 2:
        logger.error("Usage: python iss.py output.csv")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        iss_data = extract()
        iss_df = transform(iss_data)
        load(iss_df, filename)

if __name__ == "__main__":
    main()