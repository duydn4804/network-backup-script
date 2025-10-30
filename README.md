# Network Configuration Backup Script

This is a Python script using the Netmiko library to automatically Telnet into Cisco IOS network devices and back up their running-config.

## Lab Environment

- Emulation: EVE-NG
- Devices: 1 Cisco IOS Router, 2 VPCS, 1 Cloud to connect to the Internet
- Topology: VPCS <--> Router <--> Cloud (Internet)

  <img width="400" height="475" alt="Topology" src="https://github.com/user-attachments/assets/d98d0a62-6cdd-48c7-bd41-a1a949502a54" />

- Script Connection: The router's internal IP is accessed from the host machine (Ubuntu) via Telnet to fetch the running configuration.

## Setup

1. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

2. Install Netmiko
pip install netmiko

3. Run the script
python backup_configs.py

## Run the script

1. Activate the virtual environment (if not already):
source venv/bin/activate

2. Run the backup script:
python backup_configs.py

3. Results
The script will connect to all devices listed in the devices list.
Backup files will be saved in the backups/ folder with the device IP and timestamp, e.g.: 192.168.139.143_running_config_20251030_193123.txt

