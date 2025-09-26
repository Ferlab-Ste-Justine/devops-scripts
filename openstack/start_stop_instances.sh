#!/bin/bash

USAGE="Usage: $0 {start|stop} [--include NAME] [--exclude NAME]"

if [[ $# -lt 1 ]]; then
    echo "$USAGE"
    exit 1
fi

ACTION="$1"
shift

if [[ "$ACTION" == "start" ]]; then
    INSTANCES=$(openstack server list --status SHUTOFF -c Name -f value)
elif [[ "$ACTION" == "stop" ]]; then
    INSTANCES=$(openstack server list --status ACTIVE -c Name -f value)
else
    echo "Error: First argument must be 'start' or 'stop'."
    echo "Usage: $0 {start|stop} [--include NAME] [--exclude NAME]"
    exit 1
fi

while [[ $# -gt 0 ]]; do
    case "$1" in
        --include)
            INCLUDE="$2"
            shift 2
            ;;
        --exclude)
            EXCLUDE="$2"
            shift 2
            ;;
        *)
            echo "$USAGE"
            exit 1
            ;;
    esac
done

if [[ -n "$INCLUDE" ]]; then
    INSTANCES=$(echo "$INSTANCES" | grep "$INCLUDE")
fi

if [[ -n "$EXCLUDE" ]]; then
    INSTANCES=$(echo "$INSTANCES" | grep -v "$EXCLUDE")
fi

if [ -z "$INSTANCES" ]; then
    echo -e "\nNo instances are matching. Exiting."
    exit 0
fi

echo -e "\nThe following instances will be stopped:"
echo "$INSTANCES"
echo

read -rp "Do you want to stop these instances? [Y/n]: " CONFIRM

if [[ "$CONFIRM" != "Y" ]]; then
    echo "Exiting."
    exit 0
fi

echo

for INSTANCE in $INSTANCES; do
    echo "Stopping instance '$INSTANCE'..."
    openstack server "$ACTION" "$INSTANCE"
done

echo -e "\nDone."
