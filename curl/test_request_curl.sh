#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Argument missing. Exiting."
    exit 1
fi

interval_s=5
timeout_s=10
timeout_ms=$((timeout_s*1000))

while true; do
    start=$(date +%s%N)
    curl -s -o /dev/null --max-time $timeout_s "$1"
    end=$(date +%s%N)
    duration_ms=$(((end-start)/1000000))

    if [ $duration_ms -lt $timeout_ms ]; then
        echo "CURL command executed in $duration_ms milliseconds."
    else
        echo "CURL command timed out after $timeout_s second(s)."
    fi

    sleep $interval_s
done
