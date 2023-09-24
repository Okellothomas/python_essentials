from math import *

name = str(input("Enter your name please: "))
age = int(input("Enter your age please: "))
testAnswer = sqrt(int(input("Enter the squaroot of 100: ")))

print("Your name is: " + name + " And your are", age,
      " old", " and the right answer is ", testAnswer)


# simple relacement program

namei = str(input("Enter your name: "))
myage = int(input("Enter your age: "))
changeAnge = int(input("Enter your correct age: "))
correctAge = namei.replace(myage, changeAnge)
print("My Name is " + namei + " and my correct age is ", correctAge)

# the correct replacement program code.
sentence = input("Enter a sample of a poem: ")
print(sentence)
word1 = input("Enter the word you want to replace in the sentence: ")
word2 = input("Enter the word you want to replace it with in the sentence: ")
word3 = sentence.replace(word1, word2)
print("Your finally poem is: " + word3)
