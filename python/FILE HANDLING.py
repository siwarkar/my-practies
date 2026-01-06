**************************************************HANDAL.PY*******************************************
'''
f = open('a.txt')
# 3 options
# read(), readline(), readlines()
# read() will read all the contents start to end
print(f.read())
---------------------------
supppose if  u want to read some specific part
f = open('a.txt')
print(f.read(10))
--------------------------------------
# readline(): it reads one line at a time
f = open('a.txt')
print(f.readline())
print(f.readline())
-----------------------------
# readline(hint): it reads one line at a time
f = open('a.txt')
print(f.readline(5)) # wil read 5 block from line1
print(f.readline(5)) # wil read 5 block from line1
print(f.readline()) # wil read remaining block from line1
print(f.readline())# will read next line
---------------------------------
# readline(hint): it reads one line at a time
f = open('a.txt')
print(f.readline()) # read line1
print(f.readline())# read line2
-------------------------------------
# readline(limit): it reads one line at a time
f = open('a.txt')
print(f.readline()) # read line1
print(f.readline())# read line2
'''
*****************************************************HANDAL1_1.PY************************************************************************************
"""
File:
Is a medium to store the data/information in a suitable format
Each file will be stored on hard drive.
With specific extension.
Example
sample.py
test.txt
flower.jpg
1.wav
3.mp3
-------------------------------------------------
Python supports default text files
Python has 2 file formats:
- .txt
- .binary file ( img, audio,video )
=========================================================
File operations are as follows:
- Create
- Open
- read
- write
- close
-----------------------------------
# All above operations we can do using a single function of a python
# i.e open()
------------------------------------
open()
- default text file we can read
- default mode is 'r' read mode
------------------------------------------
f = open('a.txt')
# f is a handle
print(f)
# Lets read the properties of a file
print('Name of a file:',f.name) # name
print('Mode of a file:',f.mode) # mode
print('Is read mode on?-',f.readable()) # bool
print('Is write mode on?-',f.writable()) # bool
print('is my file is closed?-',f.closed) #bool
# u need to close the file explicitly
f.close()
print('After close() is my file is closed?-',f.closed) #bool
--------------------------------------------------
# if file is present in another directory
# in same project so we need to give a complete path
----------------------------------------
# how to read a file from another directory in the project
f = open('C:\\Users\hakim\PycharmProjects\Batch_19\out.txt')
print(f)
--------------------------------------------------
# If i want to read a file from desktop
f = open(r"C:\Users\hakim\OneDrive\Desktop\b.txt")
# this is not working, how to read then???
------------------------------------------------------
# Modes present in Python:
-----------------------------
Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
===========================================
# READ OPERATION
"""
f = open('a.txt')
# now read the contents from a file
# i have 3 options present in r mode
# read(), readline(), readlines()
# -----------------------
print(f.read())
***********************************************************************HANDAL_2.PY************************************************************
"""
Read operation:
- read()
- readline()
- readlines()
-----------------------------------------
f = open('a.txt')
# print(f.read()) # used to read all the contents
# print(f.readline()) # used to read one line at a time
print(f.readlines()) # used to read all the contents but
# format is: list of string
# means each line of a text file will be a one element of a list
-------------------------------------------
# Iterations using the read operation
---------------------
read()
----------------

f = open('a.txt')
data = f.read()
for i in data:
    print(i)

# read a single block/char line by line
========================================
f = open('a.txt')
data = f.readline()
for i in data:
    print(i)

# read a first line character by character
========================================
f = open('a.txt')
data = f.readlines()
for i in data:
    print(i)
# read a line by line
# bcz its a list of string
# so one line at a time it will read
# All the lines will be visited
========================================
f = open('a.txt')
print(f.read(14))
print(f.read())
for i in range(3):
    print(f.read())
=========================
f = open('a.txt')
for i in range(3):
    print(f.readline())
    # will read 1st 3 lines
============================================

f = open('a.txt')
for i in range(3):
    print(f.readlines())

# Q. difference between read(), readline(), readlines()
-----------------------------------------------------------
# WRITE OPERATION
################################################
Modes used :
'w' Write
'a' append
'x' exclusive

All above modes are used to create a file+ performs Write operation
====================================
# w mode:
------------------------------------------
f = open('A.txt') Default its read mode
# case sensetivity abt file name is nt an issue here
# but extension(.txt) + proper name u should give  while reading
print(f.read())
---------------------------------
# lets create a new file using write mode
f = open('b.txt', mode='w')
# w mode performs Truncate operation
# remove old contents

# lets add new contents
print(f.writable())
#f.write('This is b.txt file\n')
#f.write('I am adding new content in this file\n')
#f.write('Lets enjoy new operation')
# write all in one write
f.write('This is new file\nI am adding new content\nEnjoy')
# above new content is overwritten in b.txt
# in write operation ur content must be in string format
f.write(1234) #accepts only str data type
---------------------------------------------------------
f = open('b.txt','w')
f.writelines(['Name is Ramesh\n','Age is 30\n','Place is Pune'])
f.writelines([12,'A','345','ASE'])# int values not allowed
==================================================
f = open('b.txt','w')
f.writelines('This is str we are\n supplying')
# in writelines list of string + string is allowed as an input
f.write(['A','F']) # list is nt allowed in write()
=================================
Q. Difference between write() and writelines()
==============================================
# Seek() and Tell() functions in file handling
-----------------------------
tell(): it will tell current position of ur cursor in the file
# used for checking operation
=============================
f = open('b.txt')
print(f.tell())
# lets read some blocks
print(f.read(4))
print(f.tell())
# seek(): bring the cursor to given position
f.seek(16)
print(f.read())
============================================
# read only transaction id
f = open('trans.txt','r')
f.seek(5)
print(f.read(12))
"""
******************************************************************HANDAL3.PY********************************************************
"""
WRITE OPERATION:
- w mode
- a append mode
- x exclusive mode
------------------------------------------
append mode: create+add lines at the end
------------------------
f = open('c.txt','a')
print(f.writable())
# it is used to create file + add contents at the end of file
# add some contents
# f.write('This is append mode\n')
# f.write('We can add contents at the end')
f.write('\n1234234546')
---------------------------------
x: exclusive mode
Rule: if file is not present then create a new file
but if file already present then throw an exception FileExistsError:
- this is used to create a file only ones
-----------------------------------------------
# create a new file d.txt with x mode
f = open('d.txt','x')
print(f.writable())
f.write('123\n4567')
--------------------------------------------
Another file extension is binary file
img,audio,video
-------------------
Lets try to read an image file from desktop
-------------------------------------
f = open('C:\\Users\hakim\OneDrive\Desktop\\New\ML_flow.jpeg','rb')
# rb means read in binary mode
# print(f.read())
data = f.read()

f2 = open('C:\\Users\hakim\OneDrive\Desktop\sample.png','wb')
# wb write in binary
f2.write(data)

# Assignment: Read a text file and write contents to other files
----------------------------------------------------------

# lets create a new empty file
# open('e.txt','w')

# find out mobile number present in the e.txt
f = open('e.txt')
# print(f.read())

# for i in f.read():
#    if i.isdigit():
#        print(i,end='')
# --------------------
# print(f.read().find('9'))
#f.seek(39)
#print(f.read())
# ----------------------------
print(f.read().split(':')[-1])
====================================
# Read f.txt, it contains numbers
# read those numbers, display addition + average
---------------------------------------
f = open('f.txt')
tot = 0
#print(f.read().split(','))
data = f.read().split(',')
print(data)
for i in data:
    #print(type(i))
    # default dtype is str we need to typecast
    tot += int(i)
print(tot)
print(tot/len(data))
--------------------------------------
# Display Name and Age from g.txt
# now add Name and age data into h.txt
f = open('g.txt')
f2 = open('h.txt','w')
# print(f.read())
data = f.readlines()
for i in data:
    #print(i.split(',')[:2])
    f2.writelines(i.split(',')[:2])
    f2.write('\n')
------------------------------------------
"""
f = open('C:\\Users\hakim\OneDrive\Desktop\\trans.txt')
print(f)

f2 = open('C:\\Users\hakim\OneDrive\Desktop\\trans2.txt','w')
************************************************HANDAL4.PY*********************************************************************
"""
Read Write operations over CSV file
CSV: Comma separated values
# Example:
Name,Age,Salary
---------------------------------
To perform operations related to csv file we need CSV module
----------------------------------
import csv
# Create a new csv file
f = open('sample.csv','w',newline='\n')
wr = csv.writer(f)
print(wr)
# use writerow function to add values as a list of string
wr.writerow(['Name','Age','Salary'])
wr.writerow(['Mahesh',23,45000])
wr.writerow(['Arti',23,55000])
wr.writerow(['Swapnil',25,95000])
-------------------------------------
import csv
f = open('test.csv','a',newline='\n')
wr = csv.writer(f)
n = int(input('How many records you want to add?'))
# wr.writerow(['Name','Age'])
for i in range(n):
    nm = input('Enter the name of Student:')
    ag = int(input('Enter the age:'))
    wr.writerow([nm,ag])
=================================================
import csv
f = open('test.csv','w',newline='\n')
wr = csv.writer(f)
n = int(input('How many records you want to add?'))
# wr.writerow(['Name','Age'])
for i in range(n):
    nm = input('Enter the name of Student:')
    ag = int(input('Enter the age:'))
    wr.writerow([nm,ag])
wr.writerow('\n')
wr.writerow('\n')
wr.writerow('\n')
f.seek(22)
wr.writerow(['Amit',34])
==================================================
Read Operation over CSV
-------------------------------
import csv
f = open('sample.csv')
#print(f.read())
rd = csv.reader(f)
print(rd)
print(list(rd))
# Can we add above list as a multiple record at a time
-=============================================================

f = open('a.txt')
print(f.closed)
f.close()
print('After close():',f.closed)
# in above example, we need to take care of close operation
# In python we have solution on this
# which does auto closing of a file
------------------------------------------
Syntax:
with open(filename.ext) as f:
    Operations related to file inside a block
Outside the scope ur file will get closed automatically
-------------------
Example:
with open('a.txt') as f:
    print(f.readline())
    print('Is file closed(inside):',f.closed)
print('Is file closed (outside):',f.closed)
--------------------------------------
with open('b.txt','w') as f:
    f.write('1234\n')
    f.write('00000')
=================================================
"""





































