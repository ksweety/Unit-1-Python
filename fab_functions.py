# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def greet(name): #making function the argument
    print("Hello" + name) #prints hello plus the parameter

greet("Zest") #creating name

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.

def sum_numbers(a,b): #making the function with two argument names 
    print(a+b) #prints the sum of the parameters  
sum_numbers(2,3) #calls the function with the two numbers 

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def factorial(n): #creates the funtion with the parameter of a 
    if n == 0:
        return 1 #returns 1 
    else:
        return n * factorial(n - 1) #returns the factorial number 
print(factorial(5)) #prints and calls the factorial function 
# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

def even(num): #creation of the function is even with the 
    if num % 2 ==0: 
        print('this is an even number') #if the modulus is =0 then its an even number 
    else: 
        print('this is and odd number') #if the modulus is not 0 when its an odd number
even(5) #calls the number with parameter 5 
even(4) #calls the number with parameter 4

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.

def calculate_area(length, width): #creates the calculate_area function with 2 parameters 
    print(width * length) #prints the value of the width and length multiplied together

calculate_area(5,3) #calls the function with the parameters 5, and 3
   