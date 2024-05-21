import argparse
import time
import urllib3
from minio import Minio

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='Compare Files MinIO')
parser.add_argument('-se', '--srcendpoint', help='set source endpoint', required=True)
parser.add_argument('-sc', '--srccertcheck', help='set source cert check', required=False, default='true')
parser.add_argument('-sa', '--srcaccesskey', help='set source access key', required=True)
parser.add_argument('-ss', '--srcsecretkey', help='set source secret key', required=True)
parser.add_argument('-de', '--dstendpoint', help='set destination endpoint', required=True)
parser.add_argument('-dc', '--dstcertcheck', help='set destination cert check', required=False, default='true')
parser.add_argument('-da', '--dstaccesskey', help='set destination access key', required=True)
parser.add_argument('-ds', '--dstsecretkey', help='set destination secret key', required=True)
parser.add_argument('-b', '--bucket', help='set bucket', required=True)
parser.add_argument('-p', '--prefix', help='set prefix', required=False)
args = parser.parse_args()


def list_files(client, bucket, prefix):
    files = []
    objects = client.list_objects(bucket, prefix=prefix, recursive=True)
    for obj in objects:
        files.append(obj.object_name)
    return files

def compare_files(src_files, dst_files):
    return [file for file in src_files if file not in dst_files]


if __name__ == '__main__':
    src_client = Minio(
        args.srcendpoint,
        cert_check=args.srccertcheck.lower() != "false",
        access_key=args.srcaccesskey,
        secret_key=args.srcsecretkey,
    )
    dst_client = Minio(
        args.dstendpoint,
        cert_check=args.dstcertcheck.lower() != "false",
        access_key=args.dstaccesskey,
        secret_key=args.dstsecretkey
    )

    start = time.time()

    print("\nListing files...")
    src_files = list_files(src_client, args.bucket, args.prefix)
    dst_files = list_files(dst_client, args.bucket, args.prefix)

    files_missing = compare_files(src_files, dst_files)
    if files_missing:
        print("\nFiles in source but not in destination:")
        for file in files_missing:
            print(file)
    else:
        print("\nNo file is present in source but not in destination.")

    print(f"\nSource files: {len(src_files)}\nDestination files: {len(dst_files)}")

    duration = (time.time() - start)
    print(f"\nThe script took {duration:.2f} second(s) to run.")
