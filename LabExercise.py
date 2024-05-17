import os
from jinja2 import Environment, FileSystemLoader

# Define router details
routers = [
    {
        "hostname": "R1",
        "loopback": {"ip": "150.1.1.1", "netmask": "255.255.255.255"},
        "ospf_router_id": "150.1.1.1",
        "interfaces": [
            {"name": "GigabitEthernet1.12", "ip": "155.1.12.1", "netmask": "255.255.255.0", "network": "155.1.12.1", "wildcard": "0.0.0.0"},
            {"name": "GigabitEthernet1.13", "ip": "155.1.13.1", "netmask": "255.255.255.0", "network": "155.1.13.1", "wildcard": "0.0.0.0"},
            {"name": "GigabitEthernet1.14", "ip": "155.1.14.1", "netmask": "255.255.255.0", "network": "155.1.14.1", "wildcard": "0.0.0.0"}
        ]
    },
    {
        "hostname": "R2",
        "loopback": {"ip": "150.1.2.2", "netmask": "255.255.255.255"},
        "ospf_router_id": "150.1.2.2",
        "interfaces": [
            {"name": "GigabitEthernet1.12", "ip": "155.1.12.2", "netmask": "255.255.255.0", "network": "155.1.12.2", "wildcard": "0.0.0.0"}
        ]
    },
    {
        "hostname": "R3",
        "loopback": {"ip": "150.1.3.3", "netmask": "255.255.255.255"},
        "ospf_router_id": "150.1.3.3",
        "interfaces": [
            {"name": "GigabitEthernet1.13", "ip": "155.1.13.3", "netmask": "255.255.255.0", "network": "155.1.13.3", "wildcard": "0.0.0.0"}
        ]
    },
    {
        "hostname": "R4",
        "loopback": {"ip": "150.1.4.4", "netmask": "255.255.255.255"},
        "ospf_router_id": "150.1.4.4",
        "interfaces": [
            {"name": "GigabitEthernet1.14", "ip": "155.1.14.4", "netmask": "255.255.255.0", "network": "155.1.14.4", "wildcard": "0.0.0.0"}
        ]
    }
]

# Load Jinja2 template
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('LabExercise.j2')

# Generate configuration files
output = template.render(routers=routers)

# Save to file
with open("router_configs.txt", "w") as config_file:
    config_file.write(output)

print("Router configurations have been generated and saved to router_configs.txt")
