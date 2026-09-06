logs = [
    "INFO: User logged in",
    "ERROR: Login failed",
    "INFO: File opened",
    "ERROR: Permission denied"
]
for log in logs:
    if "ERROR" in log:
        print(log)           