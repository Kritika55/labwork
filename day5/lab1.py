#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
for i in range (1500,2701):
    if(i%5 == 0 and i%7 == 0):
        print(f"The number {i} is both divided by 5 and 7")
    else:
        print(f"The number {i} is not divided by 5 and 7")