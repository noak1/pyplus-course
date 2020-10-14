from netmiko import ConnectHandler

net_connect = ConnectHandler(
    host="cisco3.lasthop.io",
    username="pyclass",
    password="88newclass",
    device_type="cisco_nxos",
)

output = net_connect.send_command("show version")

with open('ex3_output.txt', 'w') as f:
    print(output, file=f)
