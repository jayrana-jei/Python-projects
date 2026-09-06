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
    },
    {
        "ip": "192.168.1.20",
        "status": "failed"
    }
]
def count_logs(logs):
    return len(logs)
print("Total Logs : ",count_logs(logs))

def count_failed_logs(logs):
    count = 0

    for log in logs:
        if log["status"] == "failed":
            count += 1

    return count
result = count_failed_logs(logs)
print("Failed Logs : ",result)

def get_failed_ips(logs):
    return [log["ip"] for log in logs if log["status"] == "failed"]
print("Failed IPS : ",get_failed_ips(logs))

def get_unique_ips(logs):
    return list({log["ip"] for log in logs})
print("Unique IPS : ",get_unique_ips(logs))
