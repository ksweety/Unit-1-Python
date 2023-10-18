"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square_number(x): #creating of the square_number function
    return x**2  #gives the value back as the number square
assert square_number(2) ==4 #checking the value of two squared to see it gonna give me an error
try: #uses a try to make sure the code still goes after the error
    assert square_number(2) ==6 
except: #needed for the try to run
    print('The assert is wrong') #print its wrong                                                                                                                                            
print(square_number(2)) #prints the square number of 2 calling the square_number function 


"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area_rectangle(a,b): #creation of the area_rectangle 
    return a * b #returning a multiplied by B 
assert area_rectangle (2,5) ==10 #checks the value 5 times 2 and check for an error
try: #uses a try to keep the code going even when error occurs 
    assert area_rectangle(6,10) == 70 #checking to see value of 6 times 10 and see if the output returns an error
except: #added except so that the try statement can work
        print("this assert is wrong")
print(area_rectangle(3,6)) #prints the area rectangle

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def cel_converted(ded): #creating of the cel converted function 
    g = ded * 1.8 #g variable which holds the ded variable stored and 1.8 is multiplied together
    h = g * 32 #adds 32 to the and sets the value to h
    return h  #returning the value stored in h 
assert cel_converted(68) ==20 #checking the value of 68 F ---> C to see if gives me a return error
try: #uses try statement to keep it going after error occurss 
    assert cel_converted(20)==6 #checks the value of 20 farenheit to see if it returns an error
except: #Except this is needed for every the try to statemtnet to occur
    print('this assert is incorrect')
print(cel_converted(24)) #prints the value 
 



"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def calculate_average(numbers): #creation of the calculation average function 
    total = sum(numbers) #total is equal to sum of every number in the parameter
    return total / len(numbers) #returns the sum divided by the length of numbers  
assert calculate_average(1,2,3,4)==2.5 #check the value of the mean for the given list 1,2,3,4 to see if it returns a error 
try: #uses a try to keep the code going after the error occurs 
    assert calculate_average (9,4,3,2) ==2 #checks the value of the mean for the list 9,4,3,2 to see if it, returns an error
except: #except is needed because for the try statement to run
    print('this asserrt is incorrect')

numbers = [1, 2, 3, 4, 5] #creation of list of numbers to calculate the average for
print(calculate_average(numbers)) #prints average
