#8. Given a n-digit number. Find the sum of its digits.
sum = 0
number = int(input("enter numbers : "))
list_of_numbers = list(str(number))
for number in list_of_numbers:
    sum+=int(number)
    print("sum is", sum)
    