"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age. 

Create a new object using this new class, and call the method you created.
""" 
# Define a class called 'Person'
class Person:
    # Initialize the 'Person' class with 'name' and 'age' attributes
    def __init__(self, name, age):
        self.name = name  # Set the 'name' attribute to the provided name
        self.age = age    # Set the 'age' attribute to the provided age
    
    # Define a method 'intro' for the 'Person' class
    def intro(self):
        print("Hello my name is " + self.name + " and I'm " + self.age)

# Create an instance of the 'Person' class with the name 'kahlil' and age '17'
kahlil = Person('kahlil', "17")

# Call the 'intro' method on the 'kahlil' object (an instance of the 'Person' class)
kahlil.intro()

       

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
""" 
# Define a base class called Animal
class Animal:
    # Initialize the Animal class with a 'name' attribute
    def __init__(self, name):
        self.name = name  # Set the 'name' attribute to the provided name
    
    # Define a method 'speak' which is meant to be overridden by subclasses
    def speak(self):
        pass

# Define a subclass 'Cat' that inherits from the 'Animal' class
class Cat(Animal):
    # Override the 'speak' method for the 'Cat' class
    def speak(self):
        print("THE CAT MEOWS") #printing what the cat says 

# Define another subclass 'Dog' that also inherits from the 'Animal' class
class Dog(Animal):
    # Override the 'speak' method for the 'Dog' class
    def speak(self):
        print("THE DOG WOOFS") #printing what the dog says

# Create an instance of the 'Dog' class with the name 'MAX'
dog_object = Dog('MAX')

# Create an instance of the 'Cat' class with the name 'GARFIELD'
cat_object = Cat('GARFIELD')

# Call the 'speak' method on the 'dog_object' (which belongs to the 'Dog' class)
dog_object.speak()

# Call the 'speak' method on the 'cat_object' (which belongs to the 'Cat' class)
cat_object.speak()

   
       

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
""" 
# Define a class named BankAccount
class BankAccount:
    # Initialize the class with two attributes: balance and owner
    def __init__(self, balance, owner):
       self.balance = balance  # Set the balance attribute to the provided balance value
       self.owner = owner      # Set the owner attribute to the provided owner's name

    # Define a method to print the current balance
    def balances(self):
        print('the balance is', self.balance)

    # Define a method for depositing money
    def deposit(self, depo):
        self.balance = self.balance + depo  # Add the deposit amount to the current balance

    # Define a method for withdrawing money
    def withdrawl(self, withdraw):
        self.balance = self.balance - withdraw  # Subtract the withdrawal amount from the current balance
        print('Your new balance is', self.balance)

# Create an instance of the BankAccount class with an initial balance of 2303 and owner's name 'kahlil'
kahlil_bank = BankAccount(2303, 'kahlil')

# Call the balances method to print the initial balance
kahlil_bank.balances()

# Call the deposit method to deposit 30 into the account
kahlil_bank.deposit(30)

# Call the withdrawl method to withdraw 50 from the account and print the new balance
kahlil_bank.withdrawl(50)


