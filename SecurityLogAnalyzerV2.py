logs = [
    {
        "ip": "192.168.1.10",
        "status": "success"
    },
    {
        "ip": "192.168.1.20",
        "status": "failed"
    },
    {
       "ip": "192.168.1.30",
       "status": "failed"
    },
    {
        "ip": "192.168.1.40",
        "status": "success"
    }
]
for log in logs:
    print("IPS : ",log["ip"])

for log in logs:
    if log["status"] == "failed":
        print("Failed IPS : ",log["ip"])

print("Total Failed Attempts : ",len(log))

unique_ips = set()
for log in logs :
    unique_ips.add(log["ip"])
print("Unique IPS : ",unique_ips)
print("Total Unique IPS : ",len(unique_ips))

for log in logs:
    print(f"{log["ip"]} -> {log["status"].upper()}")