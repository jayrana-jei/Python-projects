logs = [
    "INFO: User panda logged in",
    "ERROR: Failed login from 192.168.1.10",
    "INFO: File accessed",
    "ERROR: Failed login from 10.0.0.5",
    "WARRNING : Multiple attempts detected"
]
count = 0
for log in logs:
    if "ERROR" in log:
        print(log)
        count += 1
print("Total Errors :",count)    
        