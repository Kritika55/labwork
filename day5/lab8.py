"""
Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it
"""
previous = 0
last_previous = 0
for i in range(50):
     fibonacci = previous + last_previous
     if i == 0:
        last_previous = 1
     else:
        last_previous = previous
     previous =  fibonacci
     print( fibonacci,end=",")