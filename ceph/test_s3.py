import argparse
import boto3
import requests
from botocore.exceptions import ClientError

def upload_file(s3, bucket, key, content):
    try:
        s3.put_object(Bucket=bucket, Key=key, Body=content)
        print(f"INFO: Uploaded '{key}' to bucket '{bucket}'")
        return True
    except ClientError as err:
        print(f"ERROR: Upload failed: {err}")
        return False

def list_files(s3, bucket, prefix):
    try:
        resp = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
        keys = [obj['Key'] for obj in resp.get('Contents', [])]
        print(f"INFO: Objects under '{prefix}': {keys}")
        return keys
    except ClientError as err:
        print(f"ERROR: List failed: {err}")
        return []

def download_file(s3, bucket, key):
    try:
        resp = s3.get_object(Bucket=bucket, Key=key)
        data = resp['Body'].read()
        print(f"INFO: Downloaded '{key}' ({len(data)} bytes)")
        return data
    except ClientError as err:
        print(f"ERROR: Download failed: {err}")
        return None

def object_exists(s3, bucket, key):
    try:
        s3.head_object(Bucket=bucket, Key=key)
        print(f"INFO: Object '{key}' exists in bucket '{bucket}'")
        return True
    except ClientError as err:
        if err.response.get('Error', {}).get('Code') == '404':
            print(f"INFO: Object '{key}' does not exist in bucket '{bucket}'")
            return False
        print(f"ERROR: Error checking existence: {err}")
        return False

def delete_file(s3, bucket, key):
    try:
        s3.delete_object(Bucket=bucket, Key=key)
        print(f"INFO: Deleted '{key}' from bucket '{bucket}'")
        return True
    except ClientError as err:
        print(f"ERROR: Delete failed: {err}")
        return False

def generate_presigned_url(s3, bucket, key, method):
    try:
        url = s3.generate_presigned_url(
            ClientMethod=method,
            Params={'Bucket': bucket, 'Key': key},
            ExpiresIn=60
        )
        print(f"INFO: Generated presigned URL ({method})")
        return url
    except ClientError as err:
        print(f"ERROR: Presigned URL generation failed: {err}")
        return None

def put_presigned(url, content):
    try:
        resp = requests.put(url, data=content, timeout=10)
        if resp.status_code == 200:
            print("INFO: PUT presigned URL succeeded")
            return True
        print(f"ERROR: PUT presigned URL failed: {resp.status_code} {resp.text}")
        return False
    except requests.RequestException as err:
        print(f"ERROR: PUT request error: {err}")
        return False

def get_presigned(url, expected):
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200 and resp.content == expected:
            print("INFO: GET presigned URL succeeded")
            return True
        print(f"ERROR: GET presigned URL failed: {resp.status_code}, content mismatch")
        return False
    except requests.RequestException as err:
        print(f"ERROR: GET request error: {err}")
        return False

def run_tests(s3, bucket):
    TEST_KEY = 'test-folder/hello.txt'
    TEST_CONTENT = b'Hello! This is a test file.'

    print("==================")
    print("   Run S3 Tests   ")
    print("==================")

    # 1 Upload
    if not upload_file(s3, bucket, TEST_KEY, TEST_CONTENT):
        return

    # 2 Existence
    if not object_exists(s3, bucket, TEST_KEY):
        return

    # 3 List
    if TEST_KEY not in list_files(s3, bucket, prefix='test-folder/'):
        print("ERROR: List test failed: key not found")
        return

    # 4 Download
    if download_file(s3, bucket, TEST_KEY) != TEST_CONTENT:
        print("ERROR: Download content mismatch")
        return

    # 5 Delete
    delete_file(s3, bucket, TEST_KEY)
    if object_exists(s3, bucket, TEST_KEY):
        print("ERROR: Delete verification failed")
        return

    # 6 Presign PUT/GET
    put_url = generate_presigned_url(s3, bucket, TEST_KEY, 'put_object')
    if not put_url or not put_presigned(put_url, TEST_CONTENT):
        return
    get_url = generate_presigned_url(s3, bucket, TEST_KEY, 'get_object')
    if not get_url or not get_presigned(get_url, TEST_CONTENT):
        return

    # 7 Delete
    delete_file(s3, bucket, TEST_KEY)
    if object_exists(s3, bucket, TEST_KEY):
        print("ERROR: Delete verification failed")
        return

    print("==================")
    print(" All Tests Passed ")
    print("==================")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run S3 Tests')
    parser.add_argument('-e', '--endpoint', help='set endpoint', required=True)
    parser.add_argument('-a', '--accesskey', help='set access key', required=True)
    parser.add_argument('-s', '--secretkey', help='set secret key', required=True)
    parser.add_argument('-b', '--bucket', help='set bucket', required=True)
    args = parser.parse_args()

    s3 = boto3.client(
        's3',
        aws_access_key_id=args.accesskey,
        aws_secret_access_key=args.secretkey,
        endpoint_url=args.endpoint
    )

    run_tests(s3, args.bucket)
