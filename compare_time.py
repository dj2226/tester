#Program name: compare_time.py 
#Description: reads a date from the user in numeric form and validate.
#Author: Dennis Seldon
#Date: 9/25/2014
import datetime
now = datetime.datetime.now()
month=int(input("Enter a month(1-12): "))
day=int(input("Enter the day: "))
year=int(input("Enter the year: "))
if (now.month==month) and (now.day==day) and (now.year==year):
    print("Valid")
else:
    print("Not Valid")
