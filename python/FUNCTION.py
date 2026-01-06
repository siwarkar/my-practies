****************************************************************************FUNC_1.PY*****************************************************************
"""
Function:
uses a strategy: Write ones and use multiple times
Advantage: Code Re-usability
----------------------------------
In programming, when we want a group of statements
to be executed as per requiremnt and multiple times
or it may be for ones then will write a block of code
and this is nothing but a Function
-------------------
Syntax:
def function_name():
    statement
    .
    .
===========================================
In function we have to follow 2 process:
1. Declaring the function
def simple():
    print('Hello')

2. Calling the function
simple()
=================================
in python we have 2 types of function:
1. Built-in function:
present in python default,
print()
id()
type()
bin()
list()
tuple()
range()

2. User defined function
will be created by user as per requirement
"""
# Declaration
def simple():
    print('Hello')

# calling
# to get output
# calling is important
simple()
for i in range(5):
    simple()

import test
test.suhas()
****************************************************************FUN_2.PY*******************************************************************
"""
# syntax:
def function_name(parameters):
    .....
    .....
    .....

function_name(parameters)
If in declaration we have parameters then
we must need to supply values to it
==============================
# a, b are positional arguments
def sum(a,b):
    print(a+b)
sum(20,40)
sum(100,200)
sum(-10,-40)
sum(1)# this will raise exception bcz b value is nt given
sum()# this will give error bcz a,b values bt given
=========================================
# a, b are positional arguments
def sum(a,b):
    print(a+b)
sum(20,40,50,60)
# raise TypeError: sum() takes 2 positional arguments but 4 were given
=====================================
# a, b are positional arguments
def sum(a,b,c,d):
    print(a+b+c+d)
sum(10,20)
# raise TypeError: sum() takes 2 positional arguments but 4 were given
# Rule: if u have 4 parameters in declaration
# u must have to pass 4 values/arguments at the time of calling
======================================
# Types of arguments:
- Positional: sequence/order of values matters
--------------------------------------
Example:
---------------------------------------
def info(name,age):
    print('your name is:',name)
    print('Your age is:',age)
info('Suhas',24)
info(31,'python')
# bcz its positional hence
# 31 will be given to name and python will be age
=====================================
- Keyword: sequence/order of values doesn't matters
-----------------------------------
Example:
-------------------------------
def info(name,age):
    print('your name is:',name)
    print('Your age is:',age)
info('Suhas',24)
info(age=31,name='python')
# keyword map values to its exact parameter
# so, order doesnt matters in this case
==========================================
def display(roll_no,name,per,):
    print('Roll number:',roll_no,'name:',name,'percentage:',per)

display(name='Dinesh',roll_no=34,per=88)

display(name='Shital',roll_no=11,76)
# Rule: positional argument should nt follow keyword argument
=============================================
# we can specify/give a positional argument
# ONLY before Keyword argument
def display(roll_no,name,per,):
    print('Roll number:',roll_no,'name:',name,'percentage:',per)

#display(22,per = 88,name='Pranay')
# this is allowed because positional argument
# follow keyword argument
display(name='A',roll_no=12,name=99)
========================================
def sample(a,b,c):
    pass
sample(a =10,b= 10,c=10)
=============================
def sample(a,b,c):
    print(a,b,c)
sample('10','20','30')
# if i expect first 2int, last float
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = float(input('Enter c:'))
sample(a,b,c)
==========================================================
- Default
-----------------------------
# Default arg we can supply in declaration only
def bank(name,branch,IFSC='SBI7700'): #here IFSC is a default arg.
    print(name,branch,IFSC)
bank('Supriya','Katraj')
bank('Swapnil','Swaragate','BOI87234')
bank('Sujit','Katraj','BOM783645')
===============================
def operating_sys(name,account='Guest'):
    print('Hello',name,'welcome to',account,'account')

operating_sys('Renuka')
operating_sys('Karishma','Star')
=========================================
- Variable length
"""
****************************************************************FUN_3.PY*******************************************************************
"""
def function(parameters):
    ...
    ..
    ..
    return
# Parameters and return are optional
----------------------------------------------
4. Variable length argument:
-----------------
# WAP to do the addition of variable numbers
def add(a,b):
    print(a+b)
add(10,20)
add()
add(1,2,3)
add(10,20,30,40)
=========================
We cant pass multiple values in above case as declaation only
contains 2 parameters(a,b)
So above issue we can solve using variable length arguments.
---------------------------------------------------------
# WAP to do the addition of variable numbers
def add(*args): # instead of args we can use any other valid identifier
    print(args)
add(10,20)
add()
add(1,2,3)
add(10,20,30,40)
# when we supply variable length Positional arguments
# then it returns Tuple always
====================================
# supply following inputs to a function func
and get the addition of elements
func(10,20)
func(1,2,3,-5)
func()
func(1,2,3,4,5,6)
===================================
def func(*n):
    print(sum(n))
func(10,20)
func(1,2,3,-5)
func()
func(1,2,3,4,5,6)
=============================
# WAP to fetch only characters from function calling
def func(*n):
    for i in n:
        if str(i).isalpha():
            print(i,end=' ')
    print()
func('X',10,'A')
func(1,'V',3,'N')
===============================
Variable length keyword arguments
-----------------------
def func(**kwargs):
    print(kwargs)
func()
func(name='Python',age=23)
func(roll_no= 12,name='Abhi',marks= 80)
# kwargs gives a dict always
func(a =10,b=20,c=30)
=================================
def func(**kwargs):
    print(kwargs.values())
func()
func(name='Python',age=23)
func(roll_no= 12,name='Abhi',marks= 80)
# kwargs gives a dict always
func(a =10,b=20,c=30)
===============================================
VVIMP Q:
What is *args and **kwargs?
Differentiate both???
##############################################
Return statement:
return is a keyword
---------------------------
# a function without return
def add():
    print(100+200)

result = add()
print(result)
# When ur function does nt return anything
# then it returns ==> None means nothing
-------------------------------------
def add():
    #print(100+200)
    return 100 + 200

result = add()
print(result)
# When ur function does nt return anything
# then it returns ==> None means nothing
===========================
def kharacha(paise):
    paise -= 500 # purchased 500 rs Tshrt
    return paise
rem = kharacha(1000)
print(rem)
==========================
# How many values we can return
-> n number
===================================
def sample(a,b):
    return a,b,a+b
    # return brings the value outside
    # only single return is allowed
print(sample(20,40)) #packing is performed here
#x,y,z = sample(1,2) #unpacking
p = sample(1,2)
print(p)
#print(x,y,z,sep='--')
============================
def sample(a,b):
    return a,b,a+b
    # return brings the value outside
    # only single return is allowed
print(sample(20,40)) #packing is performed here
#x,y,z = sample(1,2) #unpacking
p = sample(1,2)
print(p)
#print(x,y,z,sep='--')
====================================
def test(fever):
    if fever >96:
        return 'positive'
    else:
        return 'negative'
result =test(70)
if result == 'positive':
    print('14 days isolation')
else:
    print('Take medicine and rest+ Home isolation')
==================================================
"""
****************************************************************FUN_4.PY*******************************************************************
"""
VVVVVVIMP:
Anonymous function/Nameless function/lambda function
Syntax:
lambda parameter/s:expression
---------------------------------
It is a function without name
used for performing one time operation
One time operation/use means we can supply only one Expression
Multiple expressions are not allowed
==================================
s = lambda x: x + 100
print(s(50))
# Lambda function has implicit return statement
#-------Normal function--------
def add(x):
    return x + 100
print('add',add(50))
==============================
Example 2:
------------------
# Normal function
def square(n):
    return n*n
print(square(4))
#########################
sq = lambda n: n*n
print(sq(10))
-----------------------------
def convert(s):
    return s.split(),s.upper()
    # return list of string
out = convert('Hello all batch 19')
print(out)
#------------------------
con = lambda s:s.split(),s.upper()
print(con('This is mentos life'))
# only single expression or operation we can perform
# but more than 1 is not allowed in lambda

# How lambda is different from normal function
# What is the difference between lambda and normal function
=====================================
def sample(name,branch='SBI'):
    return name,branch
print(sample('Umesh'))
#-------------------
sample = lambda name,branch='BOI':name+' '+branch
#lambda with default arguemnt
print(sample('Priya'))
print(sample('Abhilash','IDBI'))
---------------------
info = lambda nm,age:nm+age
#print(info('34', 'Pranav')) #positional
print(info(age='34', nm='Pranav')) #keyword args
---------------------------------------
add = lambda a,b,c:a+b+c
print(add(10,1,30,40))
#in normal function return is optional
# in lambda function return is implicit/by default
#-------------------------------
# in  normal function we can return multiple values
# whereas in lambda only single expression we can return
-------------------------------
def add():
    pass
sub = lambda x:x+10

print(add)
print(sub)
#check the output
# lambda is used form short term purpose
basically used for writing a concise,simple, one liner, compact expression
-------------------------------------------
# WA function to find out even odd number
def check(num):
    if num%2 == 0:
        return 'Even'
    else:
        return 'Odd'
print(check(1))
#----------------------------
# to implement this logic we need ternary operator
check = lambda num: 'Even' if num %2 == 0 else 'Odd'
print('Lambda:',check(8))
-----------------------------------
# WA function to find out largest amongst 2 numbers
# return_of_if if_condition else else_return
grt = lambda x,y:'X is greater' if x>y else 'Y is greater'
print(grt(10,30))
print(grt(1,0))
--------------------------------
# Actually this lambda function is used in higher order function
as an input
 ---------------------
 Which are higher order function???
 3 types of higher order functions:
 1. map
 2. filter
 3. reduce
==========================================
1. map(func,iterable):
the function inside a map will be applied on each element from iterable
-------------------------------
ls = list(range(10,21))
print(ls)
# make a square of each element
print(map(lambda num:num*num, ls))
# when we got the output in the form of object
# then to see actual values typecast the object
print(list(map(lambda num:num*num, ls)))
# this lambda function will be applied on each element of ls
--------------------------------------------
Example2:

"""
nms = ['renuka','abhijit','akshay','Vaibhav','yogesh','arti']
# name should be in reverse order
#for i in nms:
#    print(i[::-1],end=' ')
#------------------------
#reverse = lambda name:name[::-1]
#print(list(map(reverse,nms)))
#---single line solution required
#print(list(map(lambda name:name[::-1],nms)))
#--------------Normal-------------------
def rev(nm):
    #print(type(nm))
    for i in nm:
        print(i[::-1],end=' ')

rev(nms)
#print(list(map(rev,nms)))
****************************************************************FUN_5.PY*******************************************************************
"""
Higher order function:
- map(func,iterable)
- filter(func,iterable)
used to filter out the values based
on condition given inside a function
it will return results for only True instances

filter will give a original sequence or may be sub-sequence
================================
- reduce(func,sequence)
-------------------------------
k = [12,45,3,67,89,90,1,23,44,68,22]
# filter out even number from above sequence
even = lambda no : no%2==0
# filter will check this condition and selects values
# from sequence where it returns True
#print(even(9))
print(filter(even,k))
# typecast the filter object
print(list(filter(even,k)))
------------------------------
k = [12,45,3,67,89,90,1,23,44,68,22]
# filter out numbers divisible by 5
print(tuple(filter(lambda num: num % 5 == 0,k)))
-------------------------------------------
names = ['Ajay','Vijay','Nitish','Ramesh','Suresh','Ratna']
# WA single line solution: for to fetch name end with 'h'
print(list(filter(lambda nm: nm.endswith('h'),names)))
------------------------------------------------------
# Q. what is difference/similarity between map and filter??
====================================================
# Reduce: used to reduce the sequence into single object
Example: sum,greater no,
------------------
Reduce is not directly present like map and filter
it is present in functools module
so we need to import reduce
Syntax:
reduce(function,sequence)
--------------------------
from functools import reduce
k = [12,45,3,67,89,90,1,23,44,68,22]
# addition of all numbers
print(reduce(lambda x,y:x+y,k)) # performs cumulative addition
# in case of reduce we need not to typecast
-------------------------------
from functools import reduce
k = [12,45,3,67,89,90,1,23,44,68,22]
# find out largest number
print(reduce(lambda x,y: x if x>y else y,k))
--------------------------------
Assignment:
Solve 10 examples on each higher order function
==============================================
# Nested functions:
function inside another function is nested function
----------------------------
def outer():
    print('This is outer function')
    def inner():
        print('Inner function')
    inner()
outer()
=========================
# function referencing
# using outer we are referring to inner
def outer():
    print('This is outer function')
    def inner():
        print('Inner function')
    return inner
o = outer()
print(o)
# o in an instance of inner
o()
o()
==========================
def central_gov():
    print('Central')
    def state_gov():
        print('State')
    return state_gov
ref = central_gov()
print(ref)
# this ref will use to access state_gov
ref()
ref()
ref()
=============================
def central_gov():
    print('Central')
    def state_gov():
        print('State')
    return central_gov,state_gov
ref1,ref2 = central_gov()
print(ref1,ref2)
# this ref will use to access state_gov
ref1()
ref1()
ref2()
===============================
def central_gov():
    print('Central')
    def state_gov():
        print('State')
    return central_gov,state_gov
ref1,ref2 = central_gov()
print(ref1,ref2)
# this ref will use to access state_gov
ref1()
ref1()
ref2()
===========================
def outer():
    x = 100
    def inner():
        print(x)
    inner()
outer()
===============================
# Function aliasing: giving a nick name or
short name to existing function
-----------------
def prerajulization():
    print('Operations')
p = prerajulization
p()
p()
-----------------
"""
****************************************************************FUN_6.PY*******************************************************************
"""
z = lambda a,b:(a+b,a-b,a+100)
print(z(10,20))
==============================
Types of Variable:
Global var.
Local Var.
Non local
===========================
Global variable:
The variable which is available anywhere throughout the program
and we declare this variable outside the function
at the same indent level
Example:
# global variable
x = 200
def test():
    # access x inside a function
    print('Inside:',x)

# access x outside a function
print('Outside:',x)
test()
-----------------------------------
Local Variable:
the variable which is declared inside a function called as Local var
This var. wil nt be accessible outside the function
Local var is having a restricted scope
means it will be accessible only to that function or within the function
outside we  cant access.
Example:
def test():
    # local var. to test
    x = 'python inside'
    print(x)
test()
print(x)# wont be accessible
----------------------------------
# local x directly nt available
# but we want to access it outside
# solution 1  is to use: return
def test():
    # local var. to test
    x = 'python inside'
    print(x)
    return x
x = test()
print(x)
------------------------------
# Solution 2 is: use global keyword
y = 70
def test():
    # local var. now set as a global
    global x
    x = 'python inside'
    print(x,y)
test()
print(x,y)
-------------------------------
x = 100 #global
def test():
    #print(x)
    # lets try to modify x
    #x = x + 100
    #x = 80
    global x
    x += 2
    print(x)
test()
--------------------------------------
cm = 'Udhhav Thackrey'
def politics():
    #print(cm)
    #print(cm.replace('Udhhav Thackrey','Devendra Fadanvis'))
    # in local scope changing the cm is nt possible
    cm = cm.replace('Udhhav Thackrey','Devendra Fadanvis')
politics()
=======================================
cm = 'Udhhav Thackrey'
def politics():
    #print(cm)
    #print(cm.replace('Udhhav Thackrey','Devendra Fadanvis'))
    # in local scope changing the cm is nt possible
    global cm
    cm = cm.replace('Udhhav Thackrey','Devendra Fadanvis')
    print(cm)
politics()
print(cm)
=====================================
Nonlocal variable:
it is related to nested function
====================================
def outer():

    x = 200 #local to outer
    def inner():
        nonlocal x
        x = 400
        print('Inner:',x)
    inner()
    print('Outer:',x)
outer()
#print(x)
=========================
def sample_1():
    val1 = 'local_1'
    def sample_2():
        val1 = 'local_2'
        print('Sample2:',val1)
    sample_2()
    print('Sample1:',val1)
sample_1()
===========================================
def sample_1():
    val1 = 'local_1'
    def sample_2():
        nonlocal val1
        val1 = 'local_2'
        print('Sample2:',val1)
        def test():
            print(val1)
        test()
    def sample_3():
        print('Sample3:',val1)

    sample_2()
    sample_3()
    print('Sample1:',val1)

sample_1()
=====================================================
Function:
Decorator
Iterator
Generator
Closure
==========================
#eval()
#print(12+45/5*4)
# tk input from user
op = eval(input('Enter expression:'))
print(op)
print(type(op))
"""
# take a list as an input from user
ls = eval(input('Enter a list'))
print(ls)
print(type(ls))
***************************************************************************FUNC_7.PY*********************************************
"""
Types of Variables
- Local var
---------------------
# local var is available anywhere INSIDE a function
# nt outside
def sample():
    x = 'local'
    print(x)
    def test():
        print(x)
    test()
    print(x)
sample()
print(x)
-----------------------------------
# if local var. we want outside then use return
# with calling function u wil get it
def sample():
    x = 'local'
    print(x)
    def test():
        print(x)
    test()
    return x
x = sample()
print(x)
---------------------------------------
# if local var. we want outside then use return
# with calling function u wil get it
def sample():
    global x
    x = 'local'
    print(x)
    def test():
        print(x)
    test()
sample()
print(x)
------------------------------------------
- Global var
------------------------------
# global variable is available everywhere throughout the program
x = 'global'
def sample():
    print(x)
    def test():
        print(x)
    test()
print(x)
sample()
print(x)

def secret():
    print(x)
    def test_2():
        print(x)
------------------------------------------
- Nonlocal var: is associated with nested function
-----------------------------
def politics():
    cm = 'UT'
    def S_sena():
        nonlocal cm
        cm = 'DF'
        print(cm)
    S_sena()
    #print(cm)
    return cm
cm = politics()
print(cm)
=====================================
VVVVVVIMP
Lets considdr following example:
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want new list in which all names in CAPITAL
new = []
for nm in ls:
    #print(nm.upper())
    new.append(nm.upper())
print(new)
--------------------
List Comprehension: the above example we can solve using this
to give a small, and concise solution
Syntax:
[expression for val in sequence]
[expression for val in sequence if condition]
Example:
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
print([nm.upper() for nm in ls])
# its a short way to reduce no. of lines
# best for one liner solution
----------------------------------------------
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want list of tuple
# [(name,len(name)]
print([(nm.upper(),len(nm)) for nm in ls])
====================================================
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want list of names whose length is > 5
print([nm for nm in ls if len(nm) > 5])
-------------------------------------------------
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want list of names whose name contains 'i'
print([nm for nm in ls if 'i' in nm.lower()])
---------------------------------
#fetch even numbers
print([x for x in range(10) if x%2 ==  0])
---------------------------
k = [10,20,30,40,50]
# set a constant value at each place
# take constant as 0
print([0 for i in k])
print(['Constant' for i in k])
============================
k = [10,20,30,40,50]
# add 100 in each element
add = lambda i: i+ 100
print([add(i) for i in k])
print([i+100 for i in k])
==============================
# Use of ternary operator in List comprehension
--------------------------
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# Assign Group 1 to the student whose name ends with a
# else will go to Group 2
print(['Group_1' if x.endswith('a') else 'Group_2' for x in ls])
--------------------------------
# flipkart: apply charges for purchase of below 499
# otherwise free delivery
cart = [499,1000,2999,199,154]
print(['Free delivery' if p>499 else '+Rs.40 charges applied'for p in cart])
---------------------------------------------
Dict comprehension:
syntax:
{expression(key:value) for i in sequence}
=================================

ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# Expected output:{'abhijeet':7.....}
print({len(i): i for i in ls}) # keys cant be duplicate
print({i: len(i) for i in ls})
========================================
"""
*********************************************************************PROBLEM STATEMENT FILTER()**************************************
Example 1. Using Filter With a Simple Function on a List.
Suppose you have a list of letters and we want to filter out the vowels using a filter on that list.
 You can create a simple function to check whether a letter as an argument to that function
 is a vowel or not and return True or False based on the check. It is also possible to
 use this method as an argument for the filter function along with the list of letters. 
Now, try it out.
-----------------------------------------------------------------------------------------------------------------------------
Example 2. Using Filter With a Lambda Function on a List
In this example, you will use the filter function on a list of numbers to 
separate the numbers into two lists of odd and even numbers. 
Here, use the lambda function instead of a traditional function in the parameter.
------------------------------------------------------------------------------------------------------------
Example 3. Using Filter With None as a Function Parameter
If you use the None as a function argument, the filter method will 
remove any element from the iterable that it considers to be false.
 Some examples of such elements are empty strings, 0, empty braces,
 boolean False, etc. Let’s check out the below example.
-------------------------------------------------------------------------------------------------------------------
Example 4. Using Filter With a List of DictionariesIn this example, you will create
 a list of dictionaries that will store details of books such as author names, publication, 
price, etc. The aim is to try to filter out the details of those books that are costlier than
 a fixed price. Let’s check out the example below.
---------------------------------------------------------------------------------------------------------------------------
program5:Given a list of numbers, find all numbers divisible by 13.
---------------------------------------------------------------------------------------------------------------------------
program 6:Given a list of strings, find all palindromes.
---------------------------------------------------------------------------------------------------------------------------
program 7:Given a list of strings and a string str, print all anagrams of str
# Python Program to find all anagrams of str in 
# a list of strings.
----------------------------------------------------------------------------------------------------------------------
program 8:Example
inp_list = ['t','u','t','o','r','i','a','l']
sort  the list without "t"
--------------------------------------------------------------------------------------------------------------------

****************************************************PROBLEM STATEMENT MAP()*************************************************
1. Write a Python program to triple all numbers of a given list of integers. Use Python map. 
2. Write a Python program to add three given lists using Python map and lambda. 
3. Write a Python program to listify the list of given strings individually using Python map.
4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map
5. Write a Python program to square the elements of a list using map() function
6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function
7. Write a Python program to add two given lists and find the difference between lists. Use map() function. 
8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer. 
10. Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate a list of the numbers.
11. Write a Python program to compute the sum of elements of a given array of integers, use map() function.
12. Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers. 
13. Write a Python program to count the same pair in two given lists. use map() function.
14. Write a Python program to interleave two given list into another list randomly using map() function. 
15. Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
16. Write a Python program to convert a given list of strings into list of lists using map function. 
17. Write a Python program to convert a given list of tuples to a list of strings using map function.























