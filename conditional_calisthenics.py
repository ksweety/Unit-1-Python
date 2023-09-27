'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
user_Input = int(input("may I get a number")) # give me a number 
if user_Input > 10 and user_Input % 2 == 0: #if its greater than 10 and even

    print("True") # prints true  
else:
    print("False") #if not print false 


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
''' 
AGE= int(input('Please give me your age:')) # creating a variable that will let the user input their age
student= input("Are you a student? (yes or no):") #allow users to input "yes" if they are a student and "no" if they are not

if AGE <18 or student=="yes": # will be true if one of those are correct  
    print('This price is $10') # print if true
else: 
    print("This price is $20") # prints are both false 

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruits = ['apple', 'banana', 'kiwi'] # creates list
favoritefruit = input("Please give me your favorite fruit") # lets users give me their fav fruit

if favoritefruit in fruits:  #if their fav fruit is in the list 
    print('thats in the list')  #thats in the list5 is printed 
else:
    print('not in list') # if not its not in list

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year= int(input('GIVE ME A YEAR')) # input year
if year % 100 ==0 and year % 4 ==0: #if its a leap year or century 
    print('this is a century year and also a leap year') #print its leap or century
else:
    print('its not a lEAP YEAR OR CENTURY YEAR') #if not its not
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
zoneuser= input('what is your name ')
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''