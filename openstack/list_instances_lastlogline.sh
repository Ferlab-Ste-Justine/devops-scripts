#!/bin/bash

if [ -n "$1" ]; then
    instance_names=$(openstack server list --sort name:asc --name "$1" -c Name -f value)
else
    instance_names=$(openstack server list --sort name:asc -c Name -f value)
fi

echo -e "INSTANCE NAME\t\t\t\tLAST LOG LINE"

down_instances=()
for name in $instance_names
do
    log=$(timeout 5 openstack console log show "$name")
    if [ $? -eq 124 ]; then
        down_instances+=("$name")
    else
        last_line_log=$(echo "$log" | tail -n 1)
        echo -e "$name\t\t\t\t$last_line_log" | tr '\n' '\t'
        echo ""
    fi
done

echo -e "\nInstances that appear to be down (can't retrieve their logs):"
for instance in "${down_instances[@]}"
do
    echo "$instance"
done
