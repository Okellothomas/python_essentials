# nested list, nested dictionary and nested while and for loop are just list, dictionaries and loops with each other.

# nested or 2D lists

list = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

# printing the elements of the list
print(list[0][1])
print("**********************************")
print(list[3][0])
print("**********************************")
# Using nested for loop to loop through the list

for lists in list:
    for num in lists:
        if (num == 5):
            break
        print(num)
