#!/bin/bash

if [ -n "$1" ]; then
    instance_ids=$(openstack server list --sort name:asc --name "$1" -c ID -f value)
else
    instance_ids=$(openstack server list --sort name:asc -c ID -f value)
fi

echo -e "INSTANCE FLAVOR\t\t\t\t\tHOST ID\t\t\t\t\t\t\t\tINSTANCE NAME\t\t\tFLAVOR PROPERTIES"

for id in $instance_ids
do
    command1=$(openstack server show "$id" -c flavor -c hostId -c name -f value)
    flavor_name=$(echo "$command1" | head -1 | awk '{print $1}')
    command2=$(openstack flavor show "$flavor_name" -c properties -f value 2>/dev/null)
    echo -e "$command1\t\t$command2" | tr '\n' '\t'
    echo ""
done
