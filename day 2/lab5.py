# A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks
   # that can be purchased.
    #The program should read three integers: the number of students in each of the three
   # classes, a, b and c respectively.
    #Logic : Take 3 Inputs of Total Number Of STudents of Each Class Respectively
            # and check if each one of them is exactly divisible by 2 , if it
            # is divisible by 2 , number_of_students/2 is chairs needed else
           #  (number_of_students//2) + 1 is chairs needed

first_class = int(input("enter the number of student in first class : "))
second_class = int(input("enter the number of student in second class : "))
third_class = int(input("enter the number of student in third class : "))
if first_class %2 == 0:
    first_class_chairs = first_class/2
else:
     first_class_chairs = (first_class//2)+ 1
if second_class %2 == 0:
          second_class_chairs = second_class/2
else:
     second_class_chairs = (second_class//2)+ 1
if third_class %2 == 0:
    third_class_chairs = third_class/2
else:
     third_class_chairs = (third_class//2)+ 1
     print(f"First Class Needs {first_class_chairs} Chairs\nSecond Class Needs {second_class_chairs} Chairs\nThird Class Needs {third_class_chairs} Chairs\nIn Total We Need {first_class_chairs+second_class_chairs+third_class_chairs} Additional Chairs ")
