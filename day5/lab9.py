#9. Write a program to find the factorial of a number.
num = int(input("Enter any number: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
    print(factorial)