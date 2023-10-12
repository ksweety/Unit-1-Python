import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
current_datetime = datetime.datetime.now() #gets current date and time 
print(datetime.datetime.now) #prints the date and time

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
""" 
current_datetime = datetime.datetime.now() #getting the current date
formatted_date = current_datetime.strftime("%m/%d/%Y") #formatting the date in (/MM/DD/YYYY)
print(formatted_date) #prints the formatted date 
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
""" 
def convert(date_time): #creating the function and converting it to a string
    format = '%b %d %Y %I:%M%p' #making a format
    datetime_str = datetime.datetime.strptime(date_time, format) #uses the variable to set the format 

    return datetime_str #returning the datetime_str
date_time1 = 'Oct 11 2018 10:08AM' #creating a variable for the first date I made
date_time2 = 'Jan 22 2019 2:07am' #creating a second variable for the second date I made

x= convert(date_time1) #using the convert function to convert
y= convert(date_time2) #using the convert function to convert

print(y-x) #subtracting the variables

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
from datetime import date
def age(Birthdate): 
    today=date.today() 
    age=today.year -Birthdate.year -((today.month, today.day)) <(Birthdate.month, Birthdate.day)

    return age 
def convert2(date_time):
    format = 
