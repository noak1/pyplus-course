import os
from datetime import datetime

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios"
}

net_connect = ConnectHandler(**device)

print()

set_cmds = ["ip name-server 1.1.1.1",
            "ip name-server 1.0.0.1",
            "ip domain-lookup"]

fast_cli_bool = [True, False]

for flag in fast_cli_bool:
    net_connect.fast_cli = flag
    execution_start = datetime.now()
    net_connect.send_config_set(set_cmds)
    execution_end = datetime.now()
    print("Time to execute with Fast_CLI set to: {}".format(flag))
    print("Execution Time: {}".format(execution_end - execution_start))

print()
net_connect.disconnect()