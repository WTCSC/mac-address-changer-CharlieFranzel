import subprocess
# "enp0s3"
adapter = input("Adapter Name: ")
new_mac_address = ("00:11:22:33:44:55")
def get_mac_address(interface):
    result = subprocess.run(
        f"ifconfig {interface} | awk '/ether/ {{print $2}}'", 
        shell=True, capture_output=True, text=True, check=True
    )
    return result.stdout.strip()

old_mac_address = get_mac_address(adapter)
print(old_mac_address)
subprocess.run(
    subprocess.run(f"sudo ip link set {adapter} down", shell=True, check=True),
    subprocess.run(f"sudo ip link set {adapter} address {new_mac_address}", shell=True, check=True),
    subprocess.run(f"sudo ip link set {adapter} up", shell=True, check=True)
)
print(new_mac_address)
