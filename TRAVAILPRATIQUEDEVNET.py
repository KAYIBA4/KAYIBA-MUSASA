from netmiko import ConnectHandler
cisco1 = {
    "device_type": "cisco_nxos",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345"
}

net_connect = ConnectHandler(**cisco1)
a = net_connect.send_command("show running-config")
b = net_connect.send_command("show ip int brief up")
c = net_connect.send_command("show ip interface brief down")
d = net_connect.send_command("show ip route")
print(a, b, c, d)
net_connect.disconnect()
