import os
from datetime import datetime

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos"
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos"
}


for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    net_connect.send_config_from_file("vlans.cfg")
    net_connect.save_config()
    output = net_connect.send_command("show vlan", use_textfsm=True)
    print(output)
