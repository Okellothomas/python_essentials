# For loop is also used for iteration just like the while loop, however, it is more powerful when compared to the while loop

number = "Hello numbers"

for num in number:
    print(num)

for num in range(1, 11):
    print("I love you mum")

# We can use break to terminate the iteration in python

for num in range(8):
    if (num == 7):
        break
    print(num)

# using else in for loop

for x in range(1, 100):
    if (x == 20):
        break
    print(x)
else:
    print("I love for loop")
