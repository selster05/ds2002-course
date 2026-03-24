#!/bin/bash

#Assigning arguments
FILENAME=$1
BUCKET_NAME=$2
EXPIRATION=$3

#Uploading file to s3
echo "Uploading $FILENAME to s3://$BUCKET_NAME/$FILENAME..."
aws s3 cp "$FILENAME" "s3://$BUCKET_NAME/$FILENAME"

#Generating presigned URL
echo "Generating presigned url. Expires in $EXPIRATION seconds..."
PRESIGNED_URL=$(aws s3 presign --expires-in "$EXPIRATION" "s3://$BUCKET_NAME/$FILENAME")

#Output
echo "Upload complete!"
echo "Presigned url: $PRESIGNED_URL"
