#3. Write a Python program to guess a number between 1 to 9.
import random
to_guess = random.randint(1,10)

your_guess = int(input("Enter number between 1-9 : "))
if your_guess == to_guess:
    print("Well guessed")
elif your_guess > 9 or your_guess < 1 :
    print("Please select number between 1 to 9")
else:
    print("Invalid guess please try again")
while your_guess != to_guess:
    your_guess = int(input("Enter number between 1-9:")) 
if your_guess == to_guess:
    print("Well guessed ")
elif your_guess > 9 or your_guess <1:
    print("Please select numbers between 1-9")
else:
    print("Invalid guess please try again ")
      