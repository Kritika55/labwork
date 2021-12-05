#Take username and password from user and check it again for the three times whether the user has entered the right
#username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".
correct_username = "december"
correct_password = "cat"

tries = 3
for i in range(3):
    
  if i == 0 :
    print("No more attempts left")
  username = input("Enter username : ")
  password = input("Enter password : ")
  if username == correct_username and password == correct_password:
    print("logged in successfully")
    break
else:
    tries-=1
    print(f"Invalid credentials : you now have {tries} attempts left")
    