#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Argument missing. Exiting."
    exit 1
fi

while true; do
    timeout 10s ssh "$1" exit
    if [ $? -eq 0 ]; then
        echo "SSH connection ESTABLISHED."
    else
        echo "SSH connection FAILED."
    fi
    sleep 5
done
