morning_ips = {"192.168.1.10","192.168.1.20","192.168.1.30"}
evening_ips = {"192.168.1.10","192.168.1.90","192.168.1.40"}

all_ips = morning_ips | evening_ips
print("All IPS : ",all_ips)

common_ips = morning_ips & evening_ips
print("Common IPS : ",common_ips)

print("New IPS In Morning : ",morning_ips - evening_ips)
print("New IPS In Evening : ",evening_ips - morning_ips)