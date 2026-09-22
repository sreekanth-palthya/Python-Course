# ---------single_inheritance
#one child class inherits from one parent class.

# ----------def is used to define a function.
# -------What is a function?
# A function is a block of code that performs a specific task.

# Example:
# def greet():
#     print("Hello")

# Here:
# def → tells Python that we are creating a function
# greet → function name
# () → parameters go here
# : → starts the function body
# print("Hello") → code executed by the function

# To run the function:
# greet()

class Animal:
    def eat(self):  #self is used to refer to the current object inside a class.
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()   # Inherited from Animal
d.bark()  # Defined in Dog

# output:
# Animal is eating
# Dog is barking

