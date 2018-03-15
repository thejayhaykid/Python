# Assignment 1 - Jake Hayes
hour = 6
minute = 52
mile_slow_minute = 8
mile_slow_sec = 15
mile_fast_minute = 7
mile_fast_sec = 12
num_slow = 2
num_fast = 3

total_sec = (num_slow * mile_slow_sec) + (num_fast * mile_fast_sec)
total_min = (total_sec / 60) + (num_slow * mile_slow_minute) + (num_fast * mile_fast_minute)
total_sec = total_sec % 60

fin_min = minute + total_min
fin_hour = hour + (fin_min / 60)
fin_min = fin_min % 60

print "You finished your run at " + str(fin_hour) + ":" + str(fin_min)