#!/bin/bash

disk_paths=("$@")

declare -A disk_total_bytes
pools=$(virsh pool-list --all --name)

echo -e "LIST OF POOLS WITH VOLUMES\nName - Path - Total volumes size\n--------------------------------"
for pool in $pools; do
    pool_path=$(virsh pool-dumpxml "$pool" | grep -oP '(?<=<path>).*?(?=</path>)')

    volumes=$(virsh vol-list "$pool" 2>/dev/null | awk 'NR>2 {print $1}' | grep -v '^$') || continue

    total_bytes=0

    for vol in $volumes; do
        vol_bytes=$(virsh vol-info "$vol" --pool "$pool" --bytes | awk '/Capacity/ {print $2}')
        total_bytes=$(echo "$total_bytes + $vol_bytes" | bc)

        for path in "${disk_paths[@]}"; do
            if [[ $pool_path == $path* ]]; then
                disk_total_bytes["$path"]=$(( ${disk_total_bytes["$path"]:0} + vol_bytes ))
            fi
        done
    done

    total_gib=$(echo "$total_bytes / 1024 / 1024 / 1024" | bc)
    echo "$pool - $pool_path - ${total_gib} GiB"
done

echo -e "\nLIST OF SPECIFIED DISKS\nPath - Total volumes size\n-------------------------"
for path in "${disk_paths[@]}"; do
    disk_total_gib=$(echo "${disk_total_bytes[$path]:-0} / 1024 / 1024 / 1024" | bc)
    echo "$path - ${disk_total_gib} GiB"
done
