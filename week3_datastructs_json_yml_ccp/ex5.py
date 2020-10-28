import yaml
from pprint import pprint
from netmiko import ConnectHandler

filename = "/home/thana/.netmiko.yml"
with open(filename) as f:
    yaml_data = yaml.load(f)

device_info = yaml_data['cisco3']

net_connect = ConnectHandler(**device_info)
pprint(net_connect.find_prompt())
net_connect.disconnect()