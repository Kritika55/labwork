#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR".
age = int(input("Enter your age : "))
gender = input("Enter m or f): ")
if gender == 'f':
    print("You will work only in urban areas ")
elif gender == 'm' and (age >20 and age<= 40):
    print("You can work anywhere ")
elif gender == 'm' and (age > 40 and age<= 60):
    print("You will work in urban areas only ")
else:
    print("ERROR")