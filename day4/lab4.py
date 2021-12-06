#Write a program to print absolute value of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1
number = int(input("Enter any number : "))
if number < 0:
    number = number*-1
    print(" the absolute number is",number)
else:
    print("the number is", number)


