import argparse
import time
from minio import Minio
from minio.commonconfig import CopySource
from minio.error import S3Error
from urllib3.exceptions import MaxRetryError

parser = argparse.ArgumentParser(description='Copy Files MinIO')
parser.add_argument('-me', '--minioendpoint', help='set minio endpoint', required=True)
parser.add_argument('-ma', '--minioaccesskey', help='set minio access key', required=True)
parser.add_argument('-ms', '--miniosecretkey', help='set minio secret key', required=True)
parser.add_argument('-sb', '--sourcebucket', help='set source bucket', required=True)
parser.add_argument('-sp', '--sourceprefix', help='set source prefix', required=True)
parser.add_argument('-rb', '--remotebucket', help='set remote bucket', required=True)
args = parser.parse_args()

TEMP_OBJECT_NAME = "temp_" + args.sourcebucket


def copy_objects(client):
    objects = client.list_objects(args.sourcebucket, prefix=args.sourceprefix, recursive=True)
    total_objects_succeeded = 0
    total_objects_failed = 0

    print(f"Copying each object from '{args.sourcebucket}/{args.sourceprefix}' to a temp object named '{args.remotebucket}/{TEMP_OBJECT_NAME}' ...")
    print("\nUnable to copy the following objects:")

    for o in objects:
        try:
            client.copy_object(args.remotebucket, TEMP_OBJECT_NAME, CopySource(args.sourcebucket, o.object_name))
            total_objects_succeeded += 1
        except MaxRetryError:
            print(f"{o.object_name} [PROBABLY CORRUPTED]")
            total_objects_failed += 1
            continue
        except S3Error:
            print(f"{o.object_name} [PROBABLY OVER 5GB]")
            total_objects_failed += 1
            continue
        except Exception as e:
            print(f"{o.object_name} [UNEXPECTED EXCEPTION: {e}]")
            total_objects_failed += 1
            continue
    
    print(f"\nTOTAL:\t\t{total_objects_succeeded + total_objects_failed}")
    print(f"SUCCEEDED:\t{total_objects_succeeded}")
    print(f"FAILED:\t\t{total_objects_failed}")
    

if __name__ == '__main__':
    client = Minio(
        args.minioendpoint,
        access_key=args.minioaccesskey,
        secret_key=args.miniosecretkey
    )

    start = time.time()

    copy_objects(client)

    duration = (time.time() - start) / 60
    print(f"\nThe script took {duration:.2f} minute(s) to run.")
