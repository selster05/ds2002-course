#!/usr/bin/env python3
# Purpose: build ETL pipeline to extract ISS location data, transform into clean format, and load into CSV file.


# Imports
import sys
import os
import logging
import requests
import pandas as pd
import mysql.connector

# db connection
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "iss"

db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)

cursor = db.cursor()


# Initializing logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(message)s'))

logging.basicConfig(level=logging.DEBUG, handlers=[console_handler])

logging.info("Initializing ISS locator...")

logger = logging.getLogger(__name__)

# Register reporter function: checks if reporter_id exists and inserts new record if it does not
def register_reporter(table, reporter_id, reporter_name):
	# Check if reporter already exists
	check_sql = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
	cursor.execute(check_sql, (reporter_id,))
	result = cursor.fetchone()

	# Insert new reporter if result is none
	if result is None:
		insert_sql = f"""INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)"""
		cursor.execute(insert_sql, (reporter_id, reporter_name))
		db.commit()
		print("Reporter inserted.")
	else:
		print("Reporter already exists.")

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
		
		df = pd.DataFrame({"timestamp": [timestamp], "datetime": [time], "latitude": [latitude], "longitude": [longitude], "message": [data["message"]]})
		logger.info("Transform successful.")
		
		return df
	except Exception as e:
		logger.error(f"Transform failed: {e}")
		sys.exit(1)



# Load function: appends transformed data to MySQL database
def load(df, db, table, reporter_id):
	try:
		logger.info("Loading ISS data into database...")
		insert_sql = f"""INSERT INTO {table} (message, latitude, longitude, timestamp, reporter_id) VALUES (%s, %s, %s, %s, %s)"""
		
		for _, row in df.iterrows():
			cursor.execute(insert_sql, (row["message"], row["latitude"], row["longitude"], row["datetime"], reporter_id))
		
		db.commit()
		cursor.close()

		logger.info(f"Load successful. Data inserted into database.")
	
	except Exception as e:
		logger.error(f"Load failed: {e}")
		sys.exit(1)

# Main function: performs ETL functions
def main():
	try:
		logger.info("Starting ISS pipeline...")
		reporter_id = "sny8gv"
		reporter_name = "Sara Elster"
		register_reporter("reporters", reporter_id, reporter_name)
		iss_data = extract()
		iss_df = transform(iss_data)
		load(iss_df, db, "locations", reporter_id)
		logger.info("ISS pipeline successful.")
	except Exception as e:
		logger.error(f"Main failed: {e}")
		sys.exit(1)
	finally:
		db.close()
		logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
