import json
from pprint import pprint

filename = "json_data2.json"
with open(filename) as f:
    json_data = json.load(f)

arp_dict = {}

for neighbors in json_data['ipV4Neighbors']:
    ip_addr = neighbors['address']
    hw_addr = neighbors['hwAddress']
    arp_dict[ip_addr] = hw_addr

pprint(arp_dict)