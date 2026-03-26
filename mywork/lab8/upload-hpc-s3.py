import os
import glob
import logging
import argparse
import boto3

# Initiating logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(message)s'))

logging.basicConfig(level=logging.DEBUG, handlers=[console_handler])

logging.info('Initializing upload from UVA HPC to AWS S3...')

logger = logging.getLogger(__name__)

# Parse args function
def parse_args():
    parser = argparse.ArgumentParser(description = 'Upload results*.csv files from a folder to an S3 bucket/prefix.')
    parser.add_argument('input_folder', help = 'Folder with results*.csv files.')
    parser.add_argument('destination', help = 'S3 destination in format bucket/prefix/')
    args = parser.parse_args()
    return args.input_folder, args.destination

def upload(input_folder, destination):
    try:
        s3 = boto3.client('s3', region_name = 'us-east-1')
        bucket_prefix = destination.split('/', 1)
        bucket_name = bucket_prefix[0]
        prefix_name = bucket_prefix[1]

        files = glob.glob(os.path.join(input_folder, 'results*.csv'))

        for file in files:
            logger.info(f"Uploading {file} to s3://{bucket_name}/{prefix_name}")
            filename = os.path.basename(file)
            response = s3.put_object(
                Body = file,
                Bucket = bucket_name,
                Key = os.path.join(prefix_name, filename).replace('\\', '/')
            )
        return True
    except Exception as e:
        logger.error(f'Upload failed: {e}')
        return False
            

def main():
    input_folder, destination = parse_args()
    success = upload(input_folder, destination)

    if success:
        logger.info('All files uploaded successfully.')
    else:
        logger.error('One or more uploads failed.')

if __name__ == "__main__":
    main()