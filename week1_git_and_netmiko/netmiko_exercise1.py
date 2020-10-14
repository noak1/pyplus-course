from netmiko import ConnectHandler

net_connect = ConnectHandler(
    host="nxos1.lasthop.io",
    username="pyclass",
    password="88newclass",
    device_type="cisco_nxos",
)

print(net_connect.find_prompt())
net_connect.disconnect()