# WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction,
# more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
sub1 = float(input("enter marks obtained in math"))
sub2 = float(input("enter marks obtained in english"))
sub3 = float(input("enter marks obtained in nepali"))
sub4 = float(input("enter marks obtained in computer"))
sum = sub1 + sub2 + sub3 + sub4
if (sum > 70 ):
    print("distinction")
elif (sum > 60 ):
    print("first")
elif (sum > 40 ):
    print("pass")
else:
    print("fail")
    
    
    


