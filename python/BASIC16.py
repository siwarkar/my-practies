"""
3. Transfer statement:
- break: if i want to suspend current execution of a program
and exit from current loop
------------------------
frts = ['mango','orange','apple','bus','mango','banana']
for i in frts:
    if i == 'bus':
        break
    else:
        print(i)
-------------------------------
cart = [1000,670,560,999,1200,450,199,799,3400]
# if purchase is < 500 then stop
for item in cart:
    if item < 500:
        print('You purchased item with price',item, ' ur price<500')
        break
    else:
        print('you purchased an item with price Rs.',item)
====================================================
- continue: it is used to skip only the value given in the condition
rest of the part will be considerd
its centric to specific condition
But it continues loop
Q. what is diffrerence between break and continue
Q. Similarity????
-------------------

cart = [1000,670,560,999,1200,450,199,799,3400]
# if purchase is < 500 then stop
for item in cart:
    if item < 500:
        #print('You purchased item with price',item, ' ur price<500')
        continue
    else:
        #print('you purchased an item with price Rs.',item)
        print(item)
--------------------
for i in range(10):
    if i == 5:
        break
        #continue
    else:
        print(i)
---------------------
- pass: is used to create empty blocks
it is a keyword acts like a null statement
If we have a block (:) we cant keep that block empty
so rahter than writing any empty print statement
use pass simply
------
Example:
if 2 == 2:
    pass
for i in range(5):
    pass
----------------------
class BankApplication:
    def debit(self):
        pass
    def credit(self):
        pass
    def check_balance(self):
        pass
========================
Functions:
if we want to perform a typical operation multiple times as per the need
in this case we want a strategy: write a code ones and use it multiple times
Main advantage is: Code reusability
Best option in python is a function
--------------
When we want to group a multiple statements as a single unit
then we can go for a function
-------------------
# Functions are of 2 types
- Built-in functions: these are provided by/ present in python itself
Example:
print()
id()
type()
len()
help()
input()
dir()
sum()
range()
eval()
zip()
list
tuple
dict
set
bin
oct
hex
enumerate
------------------------
Assignment: How to fetch all built-in functions in python??
=================
print(round(12.7567))

print(round(12.7567,2))

# -ve to +ve
print(abs(-12))

# alphbate to number
print(ord('A'))

# number to alphabate
print(chr(67))

# enumerate
k = [12,33,44,55]
# it give a tuple of (index,value)
print(list(enumerate(k)))
-----------------------
2. User defined function:
A function created by user as per business requirement
------
While creating a function 2 things we need to perform
1. declaration of a func (a structure)
syntax:
def function_name(paratemeter):
    .
    . code
    .
    .
2. calling of a func (bring a function into a memory)
syntax:
function_name(parameters)
------------------------
WAF to do the addition of 2 numbers
-----------------------
# declaration
def addition(x,y):
    print('addition is:',x+y)

# calling
addition(x = 20, y = 40)
addition(-100,600) #positional arguments
# -100 is given to x
# 600 is given to y
---------------------------
WAF to print name age n salary data
--------------
def info(name,age,salary):
    print('Your name:',name)
    print('Your age:',age)
    print('Your salary:',salary)

nm = input('Enter your name:')
ag = int(input('Enter your age:'))
sal = float(input('Enter your salary:'))
info(nm,ag,sal)
------------------------
"""








    








    




































    










