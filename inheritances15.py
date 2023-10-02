# We use the student interface we have defined:

from inheritance15 import Student

# we then define our class


class Person(Student):
    pass


P1 = Person()

print(P1.name)
print(P1.gender)
print(P1.age)
