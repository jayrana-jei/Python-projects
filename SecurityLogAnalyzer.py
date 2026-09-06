logs = [
    "login successful",
    "login failed",
    "file accessed",
    "login failed",
    "connection closed",
    "login successful"
]
print(logs)
for log in logs:
    if "login failed" in log:
        print(log)

print("Total failed attempts :",logs.count("login failed"))
