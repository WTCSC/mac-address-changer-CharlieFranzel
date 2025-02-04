import subprocess

adapter = input("Adapter Name: ").strip() # Get network adapter name from user
new_mac_address = input("New Mac Address: ").strip() # Get new mac from user

def get_mac_address(interface):
    try:
        result = subprocess.run(
            f"ip link show {interface} | awk '/ether/ {{print $2}}'", # Command that retrives the mac address from the interface
            shell=True, capture_output=True, text=True, check=True
        )
        return result.stdout.strip() or "ERROR" # Returns a clean version or an error depending
    except subprocess.CalledProcessError:
        return "Error retrieving MAC address"

old_mac_address = get_mac_address(adapter) # Gets the old MAC address

if old_mac_address == "ERROR": # If the function returned that the address could not be retrived it returns an error
    print("Error: Invalid network adapter")
else: # Runs the 3 commands to change the mac
    subprocess.run(f"sudo ip link set {adapter} down", shell=True, check=True)
    subprocess.run(f"sudo ip link set {adapter} address {new_mac_address}", shell=True, check=True)
    subprocess.run(f"sudo ip link set {adapter} up", shell=True, check=True)

    new_mac_address = get_mac_address(adapter)


    print(f"Mac address successfully changed from {old_mac_address} to {new_mac_address}") # Gives the user the old mac address and the one it was changed to
