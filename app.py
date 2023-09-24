from math import *  # importing all function from the math library
# Printing the first hello world in my data
print("Hello World")
# Second hello world data
print("Hello thomas, i am welcomed!")
# Variables
name = 'Okello Thomas'
print(name)
print(name + ' Okey')
age = 180
print(name + "okello is", age)

# Python Inbuilt functions
scores = "thomas okello olal"
print(scores[4])
print(scores.capitalize())
print(scores.islower())
print(scores.upper())
print(scores.isupper())
print(scores.lower())
print(scores.__len__())
print(len(scores))

# Chaining in python
print(scores.upper().islower())
print(scores.lower().islower())

# Finding the index of a given number
print(scores.index(" "))

# The replace one
print(scores.replace("m", "k"))

# Numbers in python
number = 6
print(number)
sum = number + number
print(sum)
num = str(89)
add = num + num
print(add)

absolute = 78 % 9
print(absolute)

maximum = max(7, 99)
minimum = min(7, 99)
print(maximum)
print(minimum)

mynum = 89.9283
print(round(mynum))
# bin returns the binary code of the number provided to it.
print(bin(maximum))

# using the imported functions
squaroot = 81
print(sqrt(squaroot))
