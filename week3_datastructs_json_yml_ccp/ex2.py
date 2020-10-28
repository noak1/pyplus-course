import yaml

device_list = [
    {"device_name": "cisco3", "host": "cisco3.lasthop.io", "username": "test", "password": "pass"},
    {"device_name": "cisco1", "host": "cisco1.lasthop.io", "username": "test", "password": "pass"},
    {"device_name": "cisco2", "host": "cisco2.lasthop.io", "username": "test", "password": "pass"},
    {"device_name": "cisco4", "host": "cisco4.lasthop.io", "username": "test", "password": "pass"}
]


with open("my_devices.yml", "w") as f:
    yaml.dump(device_list, f, default_flow_style=False)