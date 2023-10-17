
try: #creating a try statement since when the user inputs a string it gives an error
    age = int(input('Enter your age: '))

except: #runs when the occurs 
    print("Hey! That isn't a valid number try again pal") #prints after the error occurs 



  
 
faveNum = int(input('What is your favorite number: ')) #asking the user for a int input for their favorite number
 
if age <= 21: #making an if statement runs wheh the age is less or equal to 21
 print('You are not allowed to enter, you are too young.') #print that they are too young
else: #runs when the if statement isn't true
 print('Welcome, you are old enough.') #prints you are able to come through because they are old enough

try: #creating the try because when the user inputs 0 for the faveNum variable it will cause an error

    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum) #prints the fun fact and divides 
except: #if error is false the print occurs 
   print("Hey! I am sorry we can't divide this by 0") #prints ther user friendly error!
    
