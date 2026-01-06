Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Identifiers: identity/name given to the object
>>> 23
23
>>> id(23)
140730059445984
>>> x = 23
>>> x
23
>>> id(x)
140730059445984
>>> x
23
>>> y #dont present in memory
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    y #dont present in memory
NameError: name 'y' is not defined
>>> # if u want to check objects present in the memory then use dir()
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x']
>>> y = 88
>>> y
88
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x', 'y']
>>> # x and y are identifiers
>>> # 23 and 88 are objects which are present ina memory
>>> #########################
>>> # Rules of Identifier
>>> #a-z characters are allowed
>>> # word with alphabates allowed
>>> x
23
>>> y
88
>>> bank = 'SBI'
>>> bank
'SBI'
>>> # bank is an identifier
>>> # 'SBI' is string/str object
>>> type(bank)
<class 'str'>
>>> 'SBI'
'SBI'
>>> "SBI"
'SBI'
>>> # _ underscore is allowed
>>> _a = 240
>>> _a
240
>>> _ = 100
>>> _
100
>>> # Space in between 2 char or words not allowed
>>> ab = 45 # is ok
>>> ab
45
>>> a b = 33
SyntaxError: invalid syntax
>>> # space between 22 char nt alowed
>>> bank ifsc = 'SBI1232'
SyntaxError: invalid syntax
>>> bank_ifsc = 'SBI1232'
>>> bank_ifsc
'SBI1232'
>>> a_b = 33
>>> a_b
33
>>> ##########
>>> # Special symbols and characters not allowed
>>> # $@!~%^&*()-+=:.....
>>> nm@ = 'sham'
SyntaxError: invalid syntax
>>> na$me = 'seema'
SyntaxError: invalid syntax
>>> a&b = 33
SyntaxError: can't assign to operator
>>> % = 100
SyntaxError: invalid syntax
>>> ##################
>>> # Number as a prefix is nt allowed
>>> 2a = 'python'
SyntaxError: invalid syntax
>>> # number as a suffix is allowed
>>> a4 = 600
>>> a4
600
>>> a_4 = 500
>>> a_4
500
>>> 3_f = 456
SyntaxError: invalid token
>>> ################
>>> a=10
>>> a
10
>>> b = 20
>>> b
20
>>> # PEP8 standards
>>> #############################
>>> # Keywords: are reserved words in python for performing a specific task
>>> # example: or, not, in, assert, and, with
>>> # fetch all keyword in python
>>> # we need to import  keyword
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> # how many keyword ???
>>> # use len() function to count total number of elements in a container
>>> len(keyword.kwlist)
35
>>> # check meaning of a perticula keyword using help() function
>>> help('del')
The "del" statement
*******************

   del_stmt ::= "del" target_list

Deletion is recursively defined very similar to the way assignment is
defined. Rather than spelling it out in full details, here are some
hints.

Deletion of a target list recursively deletes each target, from left
to right.

Deletion of a name removes the binding of that name from the local or
global namespace, depending on whether the name occurs in a "global"
statement in the same code block.  If the name is unbound, a
"NameError" exception will be raised.

Deletion of attribute references, subscriptions and slicings is passed
to the primary object involved; deletion of a slicing is in general
equivalent to assignment of an empty slice of the right type (but even
this is determined by the sliced object).

Changed in version 3.2: Previously it was illegal to delete a name
from the local namespace if it occurs as a free variable in a nested
block.

Related help topics: BASICMETHODS

>>> # example of del
>>> x
23
>>> del x
>>> dir()
['_', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_a', 'a', 'a4', 'a_4', 'a_b', 'ab', 'b', 'bank', 'bank_ifsc', 'keyword', 'y']
>>> x
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> #########################
>>> # These reserved keywords are not allowed as an Identifier
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> try = 'good morning'
SyntaxError: invalid syntax
>>> is = 600
SyntaxError: invalid syntax
>>> # python is case sensitive language
>>> # if we still want to use these reserved keywords then change style
>>> Try = 56
>>> Try
56
>>> #################################
>>> # Literals in python
>>> # int literal
>>> # Example
>>> a = 450
>>> # 450: object, int literal
>>> 45
45
>>> 34.55
34.55
>>> 6+7j
(6+7j)
>>> 'python'
'python'
>>> # we can differentiate object on the basis of its type
>>> # this type is nothing  bt a literal
>>> # 45 is int literal
>>> # 34.55 is float literal
>>> # 6+7j is complex literal
>>> # 'python' is string literal
>>> # in python we have 14 data types
>>> #######################
>>> # OPERATORS in PYTHON
>>> # Arithmatic operator
>>> # + - * / // ** %
>>> #division
>>> 5/6
0.8333333333333334
>>> 10/3
3.3333333333333335
>>> # we want floor part then use // operator
>>> # floor divison operator
>>> 10//3
3
>>> 10/4
2.5
>>> 10//4
2
>>> ####
>>> # % is used to fetch remainder
>>> 2%3
2
>>> 10%2
0
>>> 10%6
4
>>> ##################
>>> # Assignment operator
>>> a = 10
>>> a + 100
110
>>> # but a is unchanged
>>> a
10
>>> # requirement is to do addition and update object
>>> a
10
>>> a = a+100
>>> a
110
>>> # use assignmnt operator
>>> a
110
>>> a += 20 # a = a(110) + 20
>>> a
130
>>> # -=,*=,/=,//=,**=, %=
>>> a
130
>>> a -= 30
>>> a
100
>>> a *= 2
>>> a
200
>>> a /= 100
>>> a
2.0
>>> # **: exponential operator
>>> a
2.0
>>> a ** 3 #power of 3== cube
8.0
>>> a
2.0
>>> a **= 3
>>> a
8.0
>>> # % on float values
>>> a
8.0
>>> a % 3
2.0
>>> 1.4 % 2
1.4
>>> 100.2 % 12
4.200000000000003
>>> #####################
>>> # Logical operators
>>> # and or not
>>> # it returns boolean output
>>> # boolean means : True and False
>>> True and True
True
>>> False and True
False
>>> True and False
False
>>> False and False
False
>>> # Comparison / COnditional operators
>>> # Relational operators
>>> # < > <= >= == !=
>>> # it results boolean output
>>> 3 > 1
True
>>> 4 < 14
True
>>> 'python' == 'python'
True
>>> 'python' == 'Python'
False
>>> # case sensitivity
>>> 'p' == 'P'
False
>>> 'p' != 'P'
True
>>> 34 != 43
True
>>> ###############
>>> # Now lets combine Relational and Logical operators
>>> 'p' == 'p' and 12 > 3
True
>>> 'p' == 'p'
True
>>> 12 > 3
True
>>> 'p' == 'p' and 12 < 3
False
>>> 'p' == 'p' or 12 < 3
True
>>> ##################
>>> x = 10.0
>>> y = 10.0
>>> x
10.0
>>> y
10.0
>>> ###
>>> x = 10
>>> x = 20
>>> x
20
>>> name = 'Jayant'
>>> name == 'JAYANT'
False
>>> name.lower() == 'JAYANT'.lower()
True
>>> name.lower()
'jayant'
>>> 'JAYANT'.lower()
'jayant'
>>> ######
>>> 'abc' == ' abc'
False
>>> 'abc' == ' abc'.strip()
True
>>> '    abc'.strip()
'abc'
>>> 
