attempt = 0
while attempt < 3:
    user = input("Please Enter User")
    password = input("please Enter Password:")
    attempt += 1
    
    if password != "Python123" and user !="johndoe":
        print("Access Denied")
    else:
        print("Access Granted")
        break
else:
    print("Account Locked")
