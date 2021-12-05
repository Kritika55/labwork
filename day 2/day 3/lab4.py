#Given three integers, print the smallest one. (Three integers should be user input) 
int1 = int(input("Enter first number"))
int2 = int(input("Enter second number"))
int3 = int(input("Enter third number"))
if int1 < int2 < int3:
    print("{int1} is the smallest one")
elif int2 < int1 < int3:
    print("{int2} is the smallest one")
else:
    print("{int3} is the smallest one")
    
