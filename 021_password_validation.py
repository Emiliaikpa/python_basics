password = "python123"

while True:
    user_input = input("Enter password: ")

    
    if user_input == password:
        print("Access Granted")
        break

    else:print("Wrong Password, try again!")
