#7. Given a positive real number, print its fractional part. 
number = float(input("Enter any positive real number : "))
frictional_number = number%(number/number)
print(f"Frictional part of {number//number} is : {frictional_number}")

