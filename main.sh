#!/bin/bash

interface=$1 # Argument 1 is the interface name
new_mac=$2 # Argument 2 is the new mac address or the word random

if [ $new_mac == "random" ]; then # Checks to see if the givin input was the word random or not
    new_mac=$(printf '02:%02X:%02X:%02X:%02X:%02X\n' $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256))) # Generates a random mac address with the first 2 digits being "02" to make sure it will work

mac_address=$(ifconfig $interface | grep -oE '([[:xdigit:]]{2}(:|-)){5}[[:xdigit:]]{2}') # Gets the old mac address
echo "Old MAC Address of $interface: $mac_address" # Ouputs it

sudo ip link set $interface down # Take the interface down
sudo ip link set $interface address $new_mac # Sets the new mac
sudo ip link set $interface up #brings it back online

mac_address=$(ifconfig $interface | grep -oE '([[:xdigit:]]{2}(:|-)){5}[[:xdigit:]]{2}') # Gets the new one once it's changed

echo "New MAC Address of $interface: $mac_address" # Outputs the new address 