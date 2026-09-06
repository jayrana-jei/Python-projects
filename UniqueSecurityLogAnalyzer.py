logs = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.10",
    "192.168.1.30",
    "192.168.1.20",
    "192.168.1.40"
]
print(logs)
unique_ip = set(logs)
print("Unique IPS : ",unique_ip)
print("Length : ",len(unique_ip))

if "192.168.1.30" in logs:
    print("IP Address Found")

if "192.168.1.90" not in logs:
    print("IP Address Not Found")
