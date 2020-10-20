from pprint import pprint

from netmiko import ConnectHandler

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}
net_connect = ConnectHandler(**device1)

output1 = net_connect.send_command("show version", use_textfsm=True)
output2 = net_connect.send_command("show lldp neighbors", use_textfsm=True)

#pprint(output1)

print(output2[0]['neighbor_interface'])