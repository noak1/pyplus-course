from netmiko import ConnectHandler
from pprint import pprint

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios"
}

net_connect = ConnectHandler(**device1)
output = net_connect.send_command_timing('ping', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
net_connect.disconnect()

pprint(output)
