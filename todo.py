todolist=["get money", "save money", "rejoice"] #creating a starter list 

while True: #making a loop that will continue to repeat until the condition is met
    addtodos = input("Would you like to add a todo or remove a todo") # creating a variable that will allow you to add or remove a todo in the list
    if addtodos == ("add"): #giving a word they can use to add a todo to the todo list

        add= input("what is the new todo") #adding a new todo to their list

        todolist.append(add) #append function will add what they put to the end of the list

    elif addtodos == ('remove'): #if they put remove they can remove something from the list
        remove= input("what in the todo list, would you like to remove") #this will show them the current list and allow them to remove something from it

        if remove in todolist:  
            todolist.remove(remove) #this function will officially remove what they want to remove from the list

        else: #if its not in the list at all
            print("This isn't in the list")  #it will print this isn't in the list
    else: #if its incorect input
        print("The input is incorrect")   #print incorrect input
    
    print("-----------------------------------------------") #jus to create seperation
    
    print("your current todos are:"+str(todolist)) #this will print the current todo list that you have


   


 


