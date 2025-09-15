#File handling is an import part of programming which allows us to create, read, update and delete files.
# In Python to handle data we use open() built-in function.

'''
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

f = open('../Day16_File_Handling/reading_file_example.txt')
print(f)
txt = f.read()
#txt = f.read(10) #Instead of printing all the text, let us print the first 10 characters of the text file.
print(type(txt))
print(txt)
f.close()

#readline(): read only the first line
f = open('../Day16_File_Handling/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()


#readlines(): read all the text line by line and returns a list of lines
f = open('../Day16_File_Handling/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

'''
Opening Files for Writing and Updating
To write to an existing file, we must add a mode as parameter to the open() function:
"a" - append - will append to the end of the file, if the file does not it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates.

with statement
The with statement is a context manager in Python.
It makes sure the file is automatically closed after the block finishes (even if an error happens).
So, you don’t need to manually call f.close().
'''

with open('../Day16_File_Handling/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
    print(f)

with open('../Day16_File_Handling/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
    print(f)

#Deleting Files

#import os
#os.remove('./files/example.txt')

#If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

import os
if os.path.exists('../Day16_File_Handling/writing_file_example.txt'):
    os.remove('../Day16_File_Handling/writing_file_example.txt')
else:
    print('The file does not exist')