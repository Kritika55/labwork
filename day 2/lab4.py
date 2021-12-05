#N students take K apples and distribute them among each other evenly. The remaining
#(the indivisible) part remains in the basket. How many apples will each single student
#get? How many apples will remain in the basket? The program reads the numbers N and
#K. It should print the two answers for the questions above.
    #1: Take Input For Number of Students and Number of Apples
    #2: Divide Number os students with number of apples
    #3: Remainder is in basket rest is with students
    
number_of_students = int(input("Enter the number of students : "))
number_of_apples = int(input("Enter the number of apples : "))
each_student_gets = number_of_apples//number_of_students
baskets = number_of_apples - (each_student_gets*number_of_students)
if number_of_apples < number_of_students:
        print("the apple is insuffecient")
else:
        print(f"each student gets {each_student_gets} apples and {baskets} remains in baskets ")
    
    
    