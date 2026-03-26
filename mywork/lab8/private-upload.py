import boto3
import sys

s3 = boto3.client('s3', region_name = 'us-east-1')

local_file = sys.argv[1]
bucket_name = sys.argv[2]
make_public = False

if len(sys.argv) > 3:
    if sys.argv[3] == 'public':
        make_public = True

if make_public:
    response = s3.put_object(
        Body = local_file,
        Bucket = bucket_name,
        Key = local_file,
        ACL = 'public-read'
    )
    print('File uploaded with public-read access.')
    print(f'Public url: https://{bucket_name}.s3.us-east-1.amazonaws.com/{local_file}')
else:
    response = s3.put_object(
        Body = local_file,
        Bucket = bucket_name,
        Key = local_file,
    )
    print('File uploaded with private access.')