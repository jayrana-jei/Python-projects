password = "123"
attempts = 3
for i in range(attempts):
    pas = input("Enter the password : ")
    if password == pas:       
        print("Correct Password")
        break
    else:
        print("Incorrect Password")
