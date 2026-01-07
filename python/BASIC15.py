"""
syntax:
for variable in ssequence/iterable:

for loop examples:
# for loop on string
s = 'ajit pawar'
for i in s:
    print(i,end=' ')
----------------------
s = 'ajit 3456'
# fetch a number from s
for i in s:
    #print(i)
    if i.isdigit():
        print(i)
-------------------
s = 'ajit 3456'
# Count how many charactes we have
count = 0
for i in s:
    if i.isalpha():
        print(i)
        count+=1
print('Character count is:',count)
----------------------------
# List:
----------
d = [12,34,5,67,0,9,-12,44,-8,90,23]
for i in d:
    print(i)
--------------------
d = [12,34,5,67,0,9,-12,44,-8,90,23]
# fetch -ve values
for i in d:
    if i < 0:
        print(i)
-----------------------------
d = [12,34,5,67,0,9,-12,44,-8,90,23]
# fetch even values
for i in d:
    if i%2 == 0:
        print(abs(i))
        # abs used for getting absolute values

------------------------------------
d = [12,34,5,67,0,9,-12,44,-8,90,23]
# fetch values divisible by 5
for i in d:
    if i %5 == 0:
        print(i)
-----------------------------
# print value and its respectiv index
-------------------
d = [12,34,5,67,0,9,-12,44,-8,90,23]
# fetch values divisible by 5
for i in enumerate(d):
    print(i)
----------------------
d = [12,34,5,67,0,9,-12,44,-8,90,23]
# fetch values divisible by 5
for i in d:
    print(d.index(i),i)
---------------------
f = [1,1,1,1]
for i in enumerate(f):
    print(i)
---------------
f = [1,1,1,1]
for i in f:
    print(f.index(i),i)
# here it will give 0 index for all 1
-------------------
f = [1,1,1,1]
for i in range(len(f)):
    print(i,f[i])
-------------------
f = [1,1,1,1]
count=0
for i in f:
    print(count,i)
    count += 1
-------------------------
# Assignment:
apply for loop on set, dict, range
------------------------------
# While loop:
it is conditionally infinite loop
Syntax:
while condition:
    task1
    .
    .
in while until the condition is False
while loop will contineously get executed
----------------------
while 1 == 1:
    print('Yes')

#this loop will get executed for inf. times
# in order to stop the execution
# press ctrl + c
-----------------------
num = 1
while num == 1:
    print('Yes')
    num = 0
#in above case we are chaning the value of num
# as it makes the condition False
# while loop wil stop the execution
================================
# print 1-10 numbers using while loop
num = 1
while num <= 10:
    print(num)
    num += 1
--------------------
# print 1-10 odd numbers using while loop
num = 1
while num <= 10:
    print(num)
    num += 2
---------------------
# print python 4 times using while loop
count = 0
while count < 4:
    print('python')
    count += 1
--------------------
# want Addition of  the elements present in the list using while loop
Example : g = [102,30,506,7]
# ['ramesh',10,'suresh'] fetch only names from the list using while loop
# print 1-20 numbers those are divisible by 3
# find largest number between 2 using while loop
# Solve 10-20 questions on while loop
"""










































    














        









        






















