import platform
sys_info = platform.system()
pc_name = platform.node()
processor = platform.processor()
py_version = platform.version()
answer = 0
info_choice = 0
 
while answer !=2:
     print("======= System Information Tool =======")
     print("1. View system information")
     print("2. Exit ")
     answer = int(input("Select 1 or 2: "))
     
     while answer != 1 and answer != 2:
         print ("Invalid Choice")
         answer = int(input("Select 1 or 2: "))

     if answer == 1:
        print (" 1. Operating System")
        print (" 2. Computer Name")
        print (" 3. Procesor")
        print (" 4. Python")
        info_choice = int(input("What would you like to View: "))
        
        if answer == 1:
            print(sys_info)
        elif answer == 2:
            print(pc_name)
        elif answer == 3:
            print(processor)
        elif answer == 4:
            print(py_version)
   
     elif answer == 2:
        print("Exiting...")
