#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
   # of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
   # run to university. You jog the first mile at 7mph; then run the next two at15mph; before
   # jogging the last at 7mph again. Will this be quicker or slower than the bus?

distance_from_home = 4 
speed_of_bus = 25
time_spent_by_bus_on_the_way = 2*10
time_taken_without_stopping = (distance_from_home/speed_of_bus)*60
total_time_taken = time_spent_by_bus_on_the_way + time_taken_without_stopping
first_mile = 7
second_and_third = 15
last_mph = 7
total_time_taken_by_jogging = ((1/7)+(1/15)+(1/15)+(1/7))*60
print(f"bus takes {total_time_taken} minutes while jogging takes {total_time_taken_by_jogging}minutes . Thus jogging is faster")