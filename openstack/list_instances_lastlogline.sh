#!/bin/bash

if [ -n "$1" ]; then
    instance_names=$(openstack server list --sort name:asc --name "$1" -c Name -f value)
else
    instance_names=$(openstack server list --sort name:asc -c Name -f value)
fi

echo -e "INSTANCE NAME\t\t\tLAST LOG LINE"

for name in $instance_names
do
    command=$(timeout 5 openstack console log show "$name" | tail -n 1)
    echo -e "$name\t\t$command" | tr '\n' '\t'
    echo ""
done
