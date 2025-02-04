[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tp86o73G)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17814203)

MAC Address changer

Arguments: Takes two arguments:

interface - The network interface name.
new_mac - The new MAC address or the word "random" to generate a random one.
Random MAC Generation: If "random" is provided as new_mac, the script generates a random, valid MAC address with the first byte set to 02.

Example input

main.sh eth0 "11:22:33:44:55:66"
main.sh eth1 "random"

Retrieve Current MAC: Uses ifconfig to extract and display the current MAC address of the specified interface.

Change MAC Address:

Brings the network interface down.
Sets the new MAC address using ip link set.
Brings the interface back up.
Confirm Changes: Retrieves and displays the new MAC address to confirm the change.

Returns errors for invalid mac addresses