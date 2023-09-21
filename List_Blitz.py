"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
websites = ["nbalivestreams","chicken.io", "google", "goat"] # made a list of 4 websites 
print(websites) #printing the list
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list. 
"""
websites.append('schoology') # I added schoology to the list 
print(websites) #printing the new list
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
del websites[2] #Deleting google from the list 
print[websites] #Printing the new list
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
""" 
websites[3]='hulu' #making the index that was 3 turn into hulu
print(websites) #printing the websites 

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
""" 
websites.append('crunchyroll') # Added Crunchyroll to the list
websites.append('4anime') #Added 4anime to the list 
websites.append('Netflix') #Added Netflix to the list
print(websites) #printing website

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
""" 
del websites[-1] #deletes the last item on the list
print(websites) #print websites list


"""
Task 7: Create a List with a Range of Numbers
Create a list containing numbers within a specified range 
(inclusive). Print the created list.
""" 
c=websites[:2] #take the first two items and stores it into the variable c
print(c) #print my brand new list

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
""" 
animal_a= ['chicken', 'zebra'] #made a new list with animals
animal_b=['lion', 'buffalo']  #made a another list with animals
animals= animal_a + animal_b #made another list that added both of those past lists 
print(animals) #printing animals