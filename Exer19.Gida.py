#A python program that will count time
import time
# function for countdown
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '\n{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("\n stop")
    print('Developed By: Crismark E. Gida \n \t\tBSIT IV')
countdown(8)

