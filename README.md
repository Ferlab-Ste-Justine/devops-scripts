# About

This repo purpose is to gather useful scripts for different sporadic DevOps operations.

# MinIO

The MinIO Python SDK is needed, see: [Install the MinIO Python SDK](https://github.com/minio/minio-py?tab=readme-ov-file#install-the-minio-python-sdk)

## compare_files_minio.py

This script is to compare files by listing the ones not present in a cluster (destination) but present in another one (source).

It takes 7 mandatory arguments:
- MinIO Source Endpoint
- MinIO Source Access Key
- MinIO Source Secret Key
- MinIO Destination Endpoint
- MinIO Destination Access Key
- MinIO Destination Secret Key
- Bucket

And 3 optional arguments:
- MinIO Source Cert Check (default to True)
- MinIO Destination Cert Check (default to True)
- Prefix (no default so the whole bucket is considered)

## copy_files_minio.py

This script is to copy files by listing the ones unable to be copied.

It takes 6 mandatory arguments:
- MinIO Endpoint
- MinIO Access Key
- MinIO Secret Key
- Source Bucket
- Source Prefix
- Remote Bucket

# OpenStack

## list_instances_flavor-hostid.sh

This script is to list instances with the following information:
- Instance Name
- Host Id
- Instance Flavor
- Flavor Properties

It can take 1 argument representing a regular expression to match instance names. If no argument is given, all instances are shown.

## list_instances_lastlogline.sh

This script is to list instances with the following information:
- Instance Name
- Last Log Line

It can take 1 argument representing a regular expression to match instance names. If no argument is given, all instances are shown.

## start_stop_instances.sh

This script is to start or stop instances.

It can take 3 arguments:
- Action, either `start` or `stop` (mandatory)
- Instance names to include with `--include` (optional)
- Instance names to exclude with `--exclude` (optional)

# SSH

## test_connection_ssh.sh

This script is to establish a ssh connection to confirm it works under 10 seconds. It does so every 5 seconds.

It takes 1 mandatory argument:
- Username with Hostname/IP (separated by a `@`)

# CURL

## test_request_curl.sh

This script is to execute a curl command to see its duration and if it's under 10 seconds. It does so every 5 seconds.

It takes 1 mandatory argument:
- URL

# OpenSSL

## get_san_openssl.sh

This script is to execute an openssl command to show the `Subject Alternative Name` values of a domain server certificate.

It takes 1 mandatory argument:
- Domain

# GitHub License Checker

## github_license_checker.py

This script is designed to check and ensure that repositories within specified GitHub organizations have the appropriate license file, specifically the Apache License 2.0. If a repository lacks a license, the script can add one, based on user input.

It requires the following environment variables and libraries:
- `GITHUB_TOKEN` environment variable for authenticating with GitHub API.
- Python libraries: `os`, `base64`, `csv`, `requests`, and `datetime`.

### Key Functions
- **Get Organization Repositories**: Fetches the list of repositories for each specified organization.
- **Check Repository License**: Checks if a repository has a recognized license or if it's missing.
- **Add License**: Adds the Apache License 2.0 to a repository if it lacks one, based on user input.
- **Generate Report**: Generates a report on the license status of each repository, optionally adding missing licenses.

### Usage
- Run the script and `python check_licenses.py` follow the prompts to either generate a report only or also add missing licenses.
- The script creates two output files:
  - `license_check_logs.txt`: Detailed log of the license check process.
  - `license_check_report.csv`: CSV report of repositories and their license statuses.