"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer. 


"""
my_float=3.0
my_int=int(my_float) 
print(my_float) 
print(my_int)

#So I first made a float variable(3.0) then I made an int variable that will convert it into a n interger, then after I printed both
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
number =int(input("give me a number"))
if number > 0:
    print("THIS IS POSITIVE") 
elif number==0:
    print("This is equal to zero")
else:
    print("U gave a negative number") 

# First created a variable (number), then added an interger input that would take the number. Then I added my if statement, if greater than 0 this is positive, else if it is equal to zero, then the
# number is equal to zero, else nothing, then it will print you gave me a negative number.
        

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
bigint=int(input("give me an interger")) # made a variable that would input an interger
bigfloat=float(input("give me a float")) # made a variable that would input a float

add= bigint + bigfloat #doin addition
subtract= bigint - bigfloat #doin subtra
multiply = bigint * bigfloat 
division = bigint / bigfloat 

print("added:" +str(subtract)) 
print("multiply:" +str(multiply))
print("division:" +str(division)) 

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
fruits =  {
    "apple": 3,
    "banana": 4, 
} 

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""  
numberlist= "1,2,3,4,5" 
bigTuple= tuple(numberlist.split(",")) #used commas to split 

print(numberlist) #printing list
print(bigTuple)  #conversioon