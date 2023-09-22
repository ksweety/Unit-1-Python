'''
TASK 1 Even or Odd
Determine if a number is even or odd.
''' 
num = int(input("Enter any number to test whether it is odd or even: ")) #made a variable that will allow users to input a number

if (num % 2) == 0: #if its a multiple of 2 this number is even

              print("The number is even") #printing 

else: #if not it is odd

              print ("The provided number is odd") #printing 

'''
TASK 2 Positive, Negative, or Zero:3


EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
num = int(input("Enter a number: ")) #creating a variable that will be an interger. Allowing users to input an number
if num > 0: #if the number added is greater than zero
   print("Positive number") #this will print that they have put in a positive number
elif num == 0: #else if the number is equal to zero 
   print("Zero") #this will print that they have put in the number 0
else: #if its not positve or equal to zero
   print("Negative number") #this will print that they have put in a negative number
'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
''' 
number1= 20 
number2=10
number3= 30 

#creating variables that contain three values 

if (number1 >= number2) and (number1 >= number3): #if the first number is greater or equal to the second and third, its the largest
   largest = number1
elif (number2 >= number1) and (number2 >= number3): #if the second number is greater than the first and third, then its the largest
   largest = number2
else: #if not 
   largest = number3 #the largest is three

print("the larger number is " largest)

'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
birthyear = int(input("Please give me your birth year")) #CREATING A VARIABLE THAT WILL ALLOW USERS TO GIVE ME THEIR BIRTH YEAR

if birthyear % 4==0: #IF ITS A MULTIPLE OF 4 THEY WERE BORN ON A LEAP YEAR (if statement)
      print('you are a leap year')   #print that its a leap year
else: #if not 
      print("no leapy") #not a leap year

'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant. 

''' 
vowel = input("Enter a character:")

if(vowel=='A' or vowel=='a' or vowel=='E' or vowel =='e' or vowel=='I' #creating variables that are equal to vowels and consonant (if the character put in is a vowel)
 or vowel=='i' or vowel=='O' or vowel=='o' or vowel=='U' or vowel=='u'): #print that this is a vowel
    print(vowel, "is a Vowel")
else:    #made an else statement because if its not a vowel it is a consonant
    print(vowel, "is a Consonant") #printing that its a consonant