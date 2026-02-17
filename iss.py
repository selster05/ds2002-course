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

logging.basicConfig(level=logging.DEBUG, handlers=[console_handler]

logging.info("Locating ISS...")


# Extract function: downloads JSON data; returns parsed JSON data



# Transform function



# Load function
