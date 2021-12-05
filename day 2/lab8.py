#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
   # of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
   # run to university. You jog the first mile at 7mph; then run the next two at15mph; before
   # jogging the last at 7mph again. Will this be quicker or slower than the bus?

distance_from_home = 4 
speed_of_bus = 25
time_spent_while_stopping = 2*10
time_spent_on_the_way = (4/25)*60
total_time_spent = time_spent_while_stopping + time_spent_on_the_way
mile1 = 7
mile2 = 15
mile3 = 7
total_time_taken_by_jogging = ((1/7)+(1/15)+(1/15)+(1/7))*60
if (total_time_spent < total_time_taken_by_jogging):
    print(f"bus is faster than jogging")
else:
    print(f"jogging is faster")