
"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
""" 
a=1 
while a <=10: # loop continues while a is equal to 10 
    print(a)  # prints x
    a+= 1     #adding 1 to x


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
a=10
while a>=1: #continues until a = 1
    print(a) #prints 
    a-=1 #now it descends 
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
""" 
number =int(input("please give me a number")) #creates variable that allow users to input a number 
fac = 1 
if number < 0: #if number is 0, it cannot be finished 
    print("Sorry man, factorial does exist ") #print that its wrong
elif number ==0: #if the number that is entered is equal to 0 then that factorial is 1
    print("Factorial of 0 is 1") #print that its 1
else: #if its none of them then we add one and also multiply by 1
    for i in range(1, number +1):
        fac = fac +i
print('The factorial of: ' , number, 'factorial') #prints this 


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = ('kkkmonkey') #creates password
guess = 0
while guess < 3: #giving the users 3 tries to get the answer
    for i in password:
        guess = input('Please guess a password:') 
    if guess in password: #if they guess correctly
         print('Great Job', +guess+ "is the password") #prints great job 
         break #ends iteration 
    else:
        print("incorrect") #print the answer is wrong
        


"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
def takesum(n): #creating the takesum function 

    sum = 0 #setting the sum to 0 
    while (n !=0): #while n parameter does not equal to 0 in the following runs 

        sum=sum + (n % 10) #sets the sum = to the sum plus the parameter modulus ten
        n = n//10 #floor divides the parameter n by 10 

    return sum #returns the sum when this function is called 

num = int(input("Please input a whole number:")) #asks users for an interger input 
print(takesum(number), "is the sum of the digits within this number") #calls and prints the function with input of the uses
"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""