#Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)
choose = int(input("Enter 1 to convert celcius into fahrenhite or 2 to convert fahrenhite into celcius: "))
if choose == 1:
    c = float(input("Enter the temperature in celcius: "))
    f = (9/5*c) + 32.
    print(f"{c} is equal to {f} fahrenhite" )
else:
    f = float(input("Enter the temperature in fahrenhite: "))
    c = (5/9) * (f-32)
    print(f"{f} is equal to {c} celcius: ")
    