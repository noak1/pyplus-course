from pprint import pprint
import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

filename = 'bgp.cfg'

conf_obj = CiscoConfParse(filename)

# Result of find_objects_w_parents will be the child objects
bgp_peers = []
neighbors = conf_obj.find_objects_w_parents(
    parentspec=r"router bgp", childspec=r"neighbor"
)
for neighbor in neighbors:
    _, neighbor_ip = neighbor.text.split()
    for child in neighbor.children:
        if "remote-as" in child.text:
            _, remote_as = child.text.split()
    bgp_peers.append((neighbor_ip, remote_as))

print()
print("BGP Peers: ")
pprint(bgp_peers)
print()