from netmiko import ConnectHandler
from datetime import datetime
import os

devices = [
    {
        'device_type': 'cisco_ios_telnet',
        'host': '192.168.139.143',
        'username': 'admin',
        'password': 'cisco',
        'secret': '',
    },
]

backup_dir = "backups"
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

for device in devices:
    print(f"Connecting to {device['host']} via Telnet...")
    try:
        net_connect = ConnectHandler(**device)
        running_config = net_connect.send_command("show running-config")

        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{backup_dir}/{device['host']}_running_config_{now}.txt"
        with open(filename, 'w') as f:
            f.write(running_config)

        print(f"Backup of {device['host']} saved to {filename}")
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect {device['host']}: {e}")
