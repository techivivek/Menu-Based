import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import argparse

def create_s3_bucket(bucket_name, region=None):
    try:
        s3_client = boto3.client('s3')
        if region:
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        else:
            s3_client.create_bucket(Bucket=bucket_name)
        print(f'Bucket "{bucket_name}" created successfully.')
    except (NoCredentialsError, PartialCredentialsError):
        print("Error: AWS credentials not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create an S3 bucket.')
    parser.add_argument('bucket_name', help='The name of the S3 bucket to create.')
    parser.add_argument('--region', default=None, help='The region in which to create the bucket.')

    args = parser.parse_args()

    create_s3_bucket(args.bucket_name, args.region)
