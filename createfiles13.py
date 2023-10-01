# to crate a new file, we provide the url an write permission.
create_file = open("Createfile.text", 'r+')
# We then use the write() method
create_file.write(
    "\nThis is a new file \n This is the second part of the file \n this is the last part")


# Using the create file to create a file in python

new_file = open("create_a_newfile.py", "w")
new_file.write('print("This is new file we have just created")')
