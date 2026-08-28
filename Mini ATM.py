account={
    "name":"Jei",
    "pin":"123",
    "balance":5000,
    "type":"Travel Account"
}

pin=input("Enter the pin :")

if pin == pin:
    while True:
        print("----MINI ATM----")
        print("1. Check balance")
        print("2. Deposite money")
        print("3. Withdraw money")
        print("4. Account details")
        print("5. Exit")

        choice = int(input("Enter the choice :"))

        if choice == 1:
            print("Your balance is",account["balance"])

        elif choice == 2:
            amount = int(input("Enter your amount :"))

            if amount > 0:
                account["balance"] = account["balance"] + amount
                print("Money deposited succesfully")
                print("New balance",account["balance"])
            else:
                print("Invalid amount")
        
        elif choice == 3:
            amount = int(input("Enter the amount :"))

            if amount<=0:
                print("Invalid amount")
            elif amount > account["balance"]:
                print("Insuffitent amount")
            else:
                print("Withdrawed succesfully")
                print("New balance",account["balance"] - amount)
        
        elif choice == 4:
            
            print("Name :",account["name"])
            print("Balance :",account["balance"])
            print("Type :",account["type"])

else:
    print("Invalid pin")
    print("Access denied")