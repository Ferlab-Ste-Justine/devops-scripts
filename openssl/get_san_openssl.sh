#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Argument missing. Exiting."
    exit 1
fi

cert=$(echo | openssl s_client -connect "$1":443 2>/dev/null)

san=$(echo "$cert" | openssl x509 -noout -text | grep -A1 "Subject Alternative Name")

if [ -n "$san" ]; then
    echo "$san"
else
    echo "No 'Subject Alternative Name' found in the certificate."
fi
