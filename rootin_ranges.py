"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(1,11): #made a for loop where the range is 1 to 11 where it can go from 1-10
    print(x) #printing

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for x in range(900,1010, 10): #starts at 900 and will go by 10s to 1000
    print(x) #printing the statement
"""
Exercise 3:
Write a program that counts form 1-100 by 9
""" 
for x in range(1,101,9): #for loop will start at 1 then count by 9 all the way until it reach 100
    print(x) #print

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

sum = 0 #a variable that will store the sum
for x in range(1,11):  # Use a for loop to iterate from 1 to 10
    sum+=x #adding current number to the total
print(sum) #Printing sum
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
         print('*', end=' ')
print()  

#The output of the code will be 15 stars that is split into five from the least to greatest. 

#Since the code row is seet to 5 , it is 5 seperate rows. Theres a nested loop that has the value of 1 being added to the variable created in the main range() statement which makes the rows add one star to it