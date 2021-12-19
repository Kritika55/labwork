#Write a Python program to count the number of even and odd numbers from a series of numbers.
first = int(input("Enter the first number to start count : "))
last = int(input("Enter the last number to end count : "))
odd_count = 0
even_count = 0
for i in range(first,last+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"The total odd numbers are, {odd_count} \n The total even numbers are, {even_count} ")

    
