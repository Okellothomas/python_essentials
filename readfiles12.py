# we can read file into python from different file extension such .docs, .txt among others
'''
syntax:
file = open('filename', 'r+'-> readwrite, 'r'->read, 'w'->write, 'a'->append)
print(file.readable()->check if the file is readable)
print(file.readlines()->to read the file line by line)
print(file.readline()->to read to first line of the file)
file.close()
'''

# We check if the file is readable
myfile = open('names.txt', 'r+')

print(myfile.readable())  # output true

print("****************************************")

myfile.close()

# we read the file line by line
myfile = open('names.txt', 'r+')

print(myfile.readline())
print("***************************************")
myfile.close()

# We read te file lines:
myfile = open('names.txt', 'rt')

print(myfile.readlines())

print("****************************************")

myfile.close()


# loop and function on the file

def Loop_File(name):
    myfile = open('names.txt', 'rt')
    for name in myfile:
        print(name)
    myfile.close()


print(Loop_File(myfile))

# For loop for the
