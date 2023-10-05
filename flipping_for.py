"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
""" 
thelist = "Kahlil" #this is the variable that stores the string
for x in thelist: #creating a for loop using x
    print(x) #will print each letter of the name 
 
 

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""  
numberlist=[1,2,3,4,5] #making the list of numbers to add
sum=0 #making the original sum = to 0 
for e in numberlist: #for all the numbers in the list this runs
    sum +=e #adds all the items in the num_list
print(sum) #prints sum


"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
sentence= 'I am looking for a partner' #creating my sentence
words=sentence.split() #splitting the sentence into words 

for x in words: #making the for loop using x as the items in my sentence
    print("the length of", x, "is:", len(x)) #prints how much letters are in each word
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
""" 

humans= { 
     'Lebron' :23, 
    'Kobe' : 24, 
    'Stephen' :30,
    'Kyrie': 11,

} #creating humans dictionary 

for nba in humans:
    print(nba)
# The output was that all the key were put on a different line and not just in one. I expected that because when you use for loops it prints on different lines unlike a while loop