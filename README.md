# About

This repo purpose is to gather useful scripts for different sporadic DevOps operations.

# MinIO

## copy_files_minio.py

This script is to copy files by listing the ones unable to be copied.

The MinIO Python SDK is needed, see: [Install the MinIO Python SDK](https://github.com/minio/minio-py?tab=readme-ov-file#install-the-minio-python-sdk)

It take 6 mandatory arguments:
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

# SSH

## test_connection_ssh.sh

This script is to establish a ssh connection to confirm it works under 10 seconds. It does so every 5 seconds.

It take 1 mandatory argument:
- Username with Hostname/IP (separated by a `@`)
