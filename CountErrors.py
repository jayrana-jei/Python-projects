logs = [
    "INFO: User logged in",
    "ERROR: Login failed",
    "INFO: File opened",
    "ERROR: Permission denied"
]
count = 0
for log in logs:
    if "ERROR" in log:
        count += 1
print("Total Errors :",count)