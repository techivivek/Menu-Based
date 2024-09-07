#!/usr/bin/env python3

import cgi
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import json
import os

# Set content type
print("Content-Type: text/plain")
print()

# Create a form instance
form = cgi.FieldStorage()

# Retrieve form data
instance_id = form.getvalue("instanceId")

# Validate form data
if not instance_id:
    print("Error: Instance ID is required.")
    exit()

# Create AWS session and EC2 client using environment variables
try:
    # AWS credentials are retrieved from environment variables
    session = boto3.Session()
    ec2_client = session.client('ec2')

    # Get metrics (example: describe instance status)
    response = ec2_client.describe_instance_status(InstanceIds=[instance_id])
    metrics = response['InstanceStatuses']

    # Return metrics in JSON format
    print(json.dumps(metrics, indent=2))

except NoCredentialsError:
    print("Error: Invalid AWS credentials. Ensure that environment variables are set correctly.")
except PartialCredentialsError:
    print("Error: Incomplete AWS credentials. Ensure that environment variables are set correctly.")
except Exception as e:
    print(f"Error: {str(e)}")
