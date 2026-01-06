*********************************************************************EXCEPT_1.PY*************************************************************************
"""
Exception means error.
Example:
    NameError
    TypeError
    ValueError
    .
    .
# Why to handle exception???

print(100)
print(list(range(5)))
print(a)
print('Hello gm')
print(234234255)
----- if we look at above scenario
bcz of a next 2 lines wont b executed
so in order to avoid this
problem we need Exception handling
-----------------------------------
How to handle exception:
We have 4 blocks to deal with this
try:
    test the code here
except:
    if exception occurs in try then handle it here
    in except
else:
   if exception doesnt occurs in try then else
finally:
    it dont care abt exception occur or nt
    this block will be executed always
    irrespective of exception
===================================
"""
try: #we put a code to test an error
    print(a)

except:# come here if error occurs
    print('Error present')
print('Hello I m ready to execute')

*******************************************************EXCEPT_2.PY***************************************************
"""
try:

except:

else:

finally:
========================
How to deal with  exception
--------------------------
a = 5
try:
    print(a)
except:
    print('please assign value to a')
    a = 100
    print(a)
else: # this is optional
    print('No exception')

    for i in range(a):
        print(i)
finally:
    print('Zukga nahi sala')
-------------------------------
How to handle typical exception?
-means we know which exception is gonna happen/occure
-----------------------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    print([].index(10))

except ZeroDivisionError as msg:
    print('Error:',msg)

except NameError as msg:
    print('Error:', msg)
    print('Write further logic here')


except TypeError as msg:
    print('Error:',msg)

# default exception
except:
    print('Default exception')
    try:
        print(e)
    except:
        print('Handled')
-----------------------------
# From where u will get names of all exceptions
----------------
#print(help('builtins'))
print(help(Exception))
----------------
# Lets combine multiple exceptions together
--------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    #print([].index(10))

except (ZeroDivisionError,NameError) as msg:
    print('Error:',msg)
-----------------------
To handle all exceptions under one roof use
Exception as a main class
----------------------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    print([].index(10))

except Exception as msg:
    print('Error:',msg)
------------------------------
- try and except must be there
- use of any one of them is nt allowed
=====================
try:#mandatory
    pass

except:#mandatory

    pass
    try:
        pass
    except:
        pass

else: # optional
    pass

finally: #optional
    pass

=======================
How to generate an exception
use raise keyword
---------------------
# we need to specify condition for which this exceptioon will get raised
#if we want to allow only adults
age = 13
if age <= 18:
    try:
        raise Exception('Error ala re....')
    except:
        print('Error handled')
else:
    print('Welcome to this...')
------------------------------
raise is used to customize exceptions
----------------------
raise NameError('Name error generated')
----------------------------------------
"""
*******************************************************EXCEPT_3.PY****************************************************************
"""
try:

except:

else:

finally:
========================
How to deal with  exception
--------------------------
a = 5
try:
    print(a)
except:
    print('please assign value to a')
    a = 100
    print(a)
else: # this is optional
    print('No exception')

    for i in range(a):
        print(i)
finally:
    print('Zukga nahi sala')
-------------------------------
How to handle typical exception?
-means we know which exception is gonna happen/occure
-----------------------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    print([].index(10))

except ZeroDivisionError as msg:
    print('Error:',msg)

except NameError as msg:
    print('Error:', msg)
    print('Write further logic here')


except TypeError as msg:
    print('Error:',msg)

# default exception
except:
    print('Default exception')
    try:
        print(e)
    except:
        print('Handled')
-----------------------------
# From where u will get names of all exceptions
----------------
#print(help('builtins'))
print(help(Exception))
----------------
# Lets combine multiple exceptions together
--------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    #print([].index(10))

except (ZeroDivisionError,NameError) as msg:
    print('Error:',msg)
-----------------------
To handle all exceptions under one roof use
Exception as a main class
----------------------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    print([].index(10))

except Exception as msg:
    print('Error:',msg)
------------------------------
- try and except must be there
- use of any one of them is nt allowed
=====================
try:#mandatory
    pass

except:#mandatory

    pass
    try:
        pass
    except:
        pass

else: # optional
    pass

finally: #optional
    pass

=======================
How to generate an exception
use raise keyword
---------------------
# we need to specify condition for which this exceptioon will get raised
#if we want to allow only adults
age = 13
if age <= 18:
    try:
        raise Exception('Error ala re....')
    except:
        print('Error handled')
else:
    print('Welcome to this...')
------------------------------
raise is used to customize exceptions
----------------------
raise NameError('Name error generated')
----------------------------------------
Assert:
syntax:
assert <condition>
Assertion error will occur if COndition
result is False
------
assert 4 > 20
print('hello')
---------
else for True output there clear execution of a code
---------
assert 4 < 20
print('hello')
==========
Another syntax of assert is:
assert <condition>,<message>
----------------------
assert 1!=1,'Your condition results False'
============================
def test(data):
    assert len(data) != 0,'List is empty'
    return sum(data),sum(data)/len(data)
print(test([1,2,3]))
print(test([]))
=====================================
Personalized exceptions/Customized exceptions:
Every exception is one class
==============================
class Umesh(Exception):
    def __init__(self,msg):
        self.msg =msg

amt = float(input('How much money do you have:'))
if amt < 10000:
    raise Umesh('Sir plz bring more money then will think')
else:
    print('Welcome to my Team')
==================================

# Select employees between 18 to 50
# if age > 60 then generate old exception
# if age < 18 then generate young exception
class Young(Exception):
    def __init__(self,msg):
        self.msg=msg

class Old(Exception):
    def __init__(self,msg):
        self.msg=msg

age = int(input('Enter the age:'))
if age > 60:
    raise Old('Your age is already crossed..Sorry')
elif age < 18:
    raise Young('Please wait for sometime.. ')
else:
    print('You are eligible')
=========================================
Decorator
Generator
Iterator
Closure
==============================
Modules:
functools
itertools
collection
array
os
sys


import array
# difference betwwen list and array in python

=======================
https://byjus.com/maths/probability-and-statistics/
=================================
Khan Academy: Math and Stat
==================================
3Blue3brown
=====================
"""






































































