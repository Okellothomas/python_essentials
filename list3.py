# Defining a list
countries = ['Kenya', "UK", "UG", "US", "Niger", 8, True, 892.992]
names = list(('thomas', 'Okumu', "Sheril", 9020, False, 892.093))
# providing the length of the string
print(names.__len__())
print(len(names))
# accessing members of the string
print(names[2:])
print(names[-2:])
# change the values of the members of a list
names[2] = "Samwel"
countries[3] = "Alabama"
print(countries)


# The list inbuilt methods
# merging two list using the extend key word
list1 = [9, 10, 2, 10, 3, 4, 10, 2, 3, 90]
listtwo = list(("Okello", "Thomas", "Olal"))
list2 = [{
    10
}, {
    901
}]
list1.extend(listtwo)
print(list1)
# Add an element to the end of the list using the append keyword
list1.append(1903)
print(list1)
# adding an element to the a given index in the list using the insert keyword
list1.insert(3, 9393)
print(list1)
# removing an element of a list using the remove keyword
list1.remove(10)
print(list1)
print(list2)
# clearing the content of the list using the clear keyword
list2.clear()
print(list2)
# find the index of a given element of a list using index method
index = list1.index(10)
print(index)
# find the count of a given element of list using the count method
count = list1.count(10)
print(count)
# present the list element of the list in ascending order
listtwo.sort()
print(listtwo)
# reversing the order other the list using the revers method
listtwo.reverse()
print(listtwo)
# duplicate a list using the copy method
list3 = list1.copy()
print(list3)
# removing the last element of a list using the pop method
list3.pop()
print(list3)
# deleting the first element of a list using the del method
del list3[0]
print(list3)
# deleting an entire list using the del method
del list3
print(list3)
