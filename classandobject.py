# Python is an object oriented language and every

# typical structure of a class
class myClass:
    # object of the class
    object = 90

# create an instance of the class


instance = myClass()

# print the instance of the class
print(instance.object)

# Let us delve deeper into the class


# Using the init keyword

# Define the class animal
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


name = str(input("Enter your name!"))
color = str(input("Enter the color!"))

# Instances of the Animal class

A1 = Animal(name, color)

print("The animal is called", A1.name)
print("its color is: ", A1.color)

# delete an object of class Animal

del A1.name
print(A1.color)
print(A1.name, A1.color)
# deleting the entire object

del A1
print(A1.name, A1.color)


# The pass keyword to help bypass any error in the class:

class School:
    def __init__(self) -> None:
        # The pass allows us to bypass any error
        pass
