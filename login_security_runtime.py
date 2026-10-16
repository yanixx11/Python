registered_user = input("Please Create Username: ")
registered_password = input("Please Create Password: ")

attempts = 0

while attempts < 3:
    username = input("Please Enter Username: ")
    password = input("Please Enter Password: ")
   
    attempts +=1
    
    
    if username != registered_user or password != registered_password:
    
        print("Failed Login")
    else: 
        print("Login Successful")
        break
else: "Account Locked"
