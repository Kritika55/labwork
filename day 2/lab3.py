#Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
minutes_passed = float(input("Enter minutes passed since midnight : "))
hour = int(minutes_passed//60)
minutes = int(minutes_passed%60)
print(f"{minutes_passed} minutes passed since midnight is : {hour}:{minutes}")
