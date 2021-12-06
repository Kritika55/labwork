#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
no_of_classes_held = int(input("Enter the number of classes held : "))
no_of_classes_attended = int(input("Enter the number of classes attended : "))
percentage = (no_of_classes_attended/no_of_classes_held)*100
if percentage > 75:
    print("You are allowed to sit in exam")
else:
    print("You are not allowed to sit in exam")

