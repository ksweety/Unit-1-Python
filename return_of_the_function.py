"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square_number(x): #creating of the square_number function
    return x**2  #gives the value back as the number square

print(square_number(2)) #prints the square number of 2 calling the square_number function 


"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area_rectangle(a,b): #creation of the area_rectangle 
    return a * b #returning a multiplied by B
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
print(cel_converted(24)) #prints the value 
 



"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def calculate_average(numbers): #creation of the calculation average function 
    total = sum(numbers) #total is equal to sum of every number in the parameter
    return total / len(numbers) #returns the sum divided by the length of numbers 


numbers = [1, 2, 3, 4, 5] #creation of list of numbers to calculate the average for
print(calculate_average(numbers)) #prints average
