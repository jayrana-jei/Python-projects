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

def is_failed(log):
    return log["status"] == "failed"
result = is_failed(logs[1])
print("IP Is Failed : ",result)


failed_attempts = 0
def count_failed(log):
    if log["status"] == "failed":
        return 1
    return 0
for log in logs:
    failed_attempts += count_failed(log)

print("Total Failed Attempts : ",failed_attempts)


def get_failed_ips(log):
    failed_ips = []
    for log in logs:
        if log["status"] == "failed":
            failed_ips.append(log["ip"])
    return failed_ips
failed_list = get_failed_ips(logs)
print("Failed IPS : ", failed_list)    

