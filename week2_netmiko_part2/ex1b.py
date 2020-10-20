from pprint import pprint

from netmiko import ConnectHandler

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)
output = net_connect.send_command("ping", expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += net_connect.send_command("ip", expect_string=r"Target IP", strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r"5", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"100", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"2", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"n", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"n", strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)
net_connect.disconnect()

pprint(output)
