#Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero.
int1 = int(input("enter first integer : "))
int2 = int(input("enter second integer : "))
int3 = int(input("enter third integer : "))

if (int1==int2==int3 or int1==int2 or int2==int3 or int3==int1):
    sum=0
else:
    sum=int1+int2+int3
print(f"the sum is {sum}")

    