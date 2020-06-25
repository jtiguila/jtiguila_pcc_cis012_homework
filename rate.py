# Rate.py
# Module 2 Homework - CIS 12
# Instructor James Mertz
# By Josue Tiguila

#Print for input of hours
print ("How many hours are you working?")
hours = int(input())

#print for input of rate per hour
print ("What is the rate per hour")
rate = int(input())

#Compute gross pay
gross = (hours * rate)
print("Your gross pay is: " + str(gross))