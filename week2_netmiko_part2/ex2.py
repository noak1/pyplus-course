from netmiko import ConnectHandler
from pprint import pprint
from datetime import datetime

device = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
    "global_delay_factor": 2
}

net_connect = ConnectHandler(**device)

task1_start = datetime.now()
output1 = net_connect.send_command("show lldp neighbors detail")
task1_end = datetime.now()
execution_time1 = task1_end - task1_start
#pprint(output1)
print("Execution time of task1: ")
print(execution_time1)

task2_start = datetime.now()
output2 = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
task2_end = datetime.now()
execution_time2 = task2_end - task2_start
#pprint(output2)
print("Execution time of task2: ")
print(execution_time2)

