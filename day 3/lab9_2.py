username = input("Enter your username")
password = input("Enter your password")
for i in range(0, 3):
    username1 = input("Enter username")
    password1 = input("Enter password")
    if username == username1 and password == password1:
        print("You are logged in successfully")
        break
    elif i<3:
        if username != username1 and password != password1 and 1<3:
            print("Invalid credentials Try again")
    else:
        print("Attempt finished")
        