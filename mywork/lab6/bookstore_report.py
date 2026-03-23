#!/usr/bin/env python3

# importing libraries
import os
import pymongo

# Get MONGODB connection
MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

# Main function: 
def main():
    # Creating connection string
    connection_string = f"mongodb+srv://{MONGODB_ATLAS_USER}:{MONGODB_ATLAS_PWD}@{MONGODB_ATLAS_URL}"

    # Connecting to Mongo DB atlas
    client = pymongo.MongoClient(connection_string)

    # Selecting the database and collection
    db = client["bookstore"]
    authors = db["authors"]

    # Creating bookstore report
    print("Bookstore Author Report:\n")

    total_authors = authors.count_documents({}) # Total author count
    print(f"Total number of authors: {total_authors}\n")

    print("Authors:") # List of authors
    for author in authors.find({}):
        name = author["name"]
        nationality = author["nationality"]
        bio_short = author["bio"]["short"]

        print(f"Name: {name}")
        print(f"Nationality: {nationality}")
        print(f"Biography: {bio_short}\n\n")
    
    # Close connection
    client.close()


# Calling main
if __name__ == "__main__":
    main()