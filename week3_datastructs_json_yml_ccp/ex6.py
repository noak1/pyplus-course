from pprint import pprint
import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    yaml_out = yaml.safe_load(f)

cisco4 = yaml_out["cisco4"]
net_connect = ConnectHandler(**cisco4)
run_config = net_connect.send_command('show run')

run_config = run_config.splitlines()

conf_obj = CiscoConfParse(run_config)

interfaces = conf_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

print()
for intf in interfaces:
    print("Interface Line: {}".format(intf.text))
    ip_address = intf.re_search_children(r"ip address")[0].text
    print("IP Address Line: {}".format(ip_address))
    print()
print()