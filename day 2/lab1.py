# convert seconds to day, hours, minutes and seconds
second = int(input("enter the value for second:"))
day = (((second/60)/60) /24)
print(f"total day for given seconds: {day}")
hour = ((second/60)/60)
print(f"total hours for given seconds: {hour}")
minute = (second/60)
print(f"total minute for given seconds: {second}")



