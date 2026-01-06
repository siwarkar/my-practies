Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello')
Hello
>>> print('Hello Good morning')
Hello Good morning
>>> print('Hello Good morning 1234')
Hello Good morning 1234
>>> 23 * 4
92
>>> #####################
>>> # Identifier rules
>>> # hash is used for commenting purpose
>>> jkhjhkjssfdsf
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    jkhjhkjssfdsf
NameError: name 'jkhjhkjssfdsf' is not defined
>>> # Identifier: it an identity of an object
>>> # object is an entity which exist in the memory
>>> # in python everything is an object
>>> 100
100
>>> 'python'
'python'
>>> 23.5
23.5
>>> # how to check object exist into the memory???
>>> # use id function of a python
>>> id(100)
140707068108928
>>> id('python')
2659653565384
>>> a = 100
>>> # a: is an identifier
>>> a
100
>>> id(a)
140707068108928
>>> b = 'python'
>>> b
'python'
>>> id(b)
2659653565384
>>> #######################
>>> # Rules of an identifier
>>> # Use a-zcharacters
>>> # while giving name to an object use all letters n lower case
>>> q = 'Java'
>>> q
'Java'
>>> A = 67
>>> A
67
>>> a
100
>>> # A and a makes a difference here
>>> # Python is case sensitive language
>>> py = 'python'
>>> py
'python'
>>> Py #here P is in caps
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Py #here P is in caps
NameError: name 'Py' is not defined
>>> pY
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    pY
NameError: name 'pY' is not defined
>>> PY
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    PY
NameError: name 'PY' is not defined
>>> # Only numbers are not allowed
>>> 12 = 120
SyntaxError: can't assign to literal
>>> # we can use  alphabates + numbers
>>> # number as a prefix is not allowed
>>> 5a = 'good morning'
SyntaxError: invalid syntax
>>> 3b = 450
SyntaxError: invalid syntax
>>> # number as a suffix , its allowed
>>> a5 = 'good morning'
>>> a5
'good morning'
>>> b3 = 450
>>> b3
450
>>> # PEP8 standards
>>> # use of _ underscore is allowed in identifier
>>> _  = 'MI'
>>> _
'MI'
>>> a_5 = 'GM'
>>> a_5
'GM'
>>> bank_name ='SBI'
>>> bank_name
'SBI'
>>> bankname = 'BOI'
>>> bankname
'BOI'
>>> ############################
>>> # Special symbols and characters are not allowed
>>> # !@~$%^&*():"<>?{}_+
>>> c@ = 'sham'
SyntaxError: invalid syntax
>>> $bank_pin = 1234
SyntaxError: invalid syntax
>>> #########################
>>> # between 2 chars or words, space is not allowed
>>> a b = 300
SyntaxError: invalid syntax
>>> bank ifsc = 'SBI12344'
SyntaxError: invalid syntax
>>> a_b = 300
>>> a_b
300
>>> bank_ifsc = 'SBI12344'
>>> bank_ifsc
'SBI12344'
>>> ########################################
>>> bank_ifsc = 'SBI#@Q$#%##$'
>>> bank_ifsc
'SBI#@Q$#%##$'
>>> a = $ab
SyntaxError: invalid syntax
>>> ########################################
>>> # Keywords in python
>>> # These are reserved words from Python
>>> # to check keywords present in python
>>> # we have to import keyword library
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> # to count total number of keywords present in python
>>> # use len() function
>>> len(keyword.kwlist)
35
>>> # these keywords can not be used as an identifier
>>> del = 'C++'
SyntaxError: invalid syntax
>>> with = 600
SyntaxError: invalid syntax
>>> #################################
>>> # if u want to undestand meaning of each keyword
>>> # then use help() function
>>> help('not')
Boolean operations
******************

   or_test  ::= and_test | or_test "or" and_test
   and_test ::= not_test | and_test "and" not_test
   not_test ::= comparison | "not" not_test

In the context of Boolean operations, and also when expressions are
used by control flow statements, the following values are interpreted
as false: "False", "None", numeric zero of all types, and empty
strings and containers (including strings, tuples, lists,
dictionaries, sets and frozensets).  All other values are interpreted
as true.  User-defined objects can customize their truth value by
providing a "__bool__()" method.

The operator "not" yields "True" if its argument is false, "False"
otherwise.

The expression "x and y" first evaluates *x*; if *x* is false, its
value is returned; otherwise, *y* is evaluated and the resulting value
is returned.

The expression "x or y" first evaluates *x*; if *x* is true, its value
is returned; otherwise, *y* is evaluated and the resulting value is
returned.

(Note that neither "and" nor "or" restrict the value and type they
return to "False" and "True", but rather return the last evaluated
argument.  This is sometimes useful, e.g., if "s" is a string that
should be replaced by a default value if it is empty, the expression
"s or 'foo'" yields the desired value.  Because "not" has to create a
new value, it returns a boolean value regardless of the type of its
argument (for example, "not 'foo'" produces "False" rather than "''".)

Related help topics: EXPRESSIONS, TRUTHVALUE

>>> #how to check details of print function
 
>>> help(print)
 
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(id)
 
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> ############################
     
>>> import keyword
     
>>> keyword.kwlist
     
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 

**********************************DAY 2***********************************


Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # check keywords present in the python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
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

>>> # we cant use these keywords as an identifier
>>> a = 70
>>> a
70
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> try = 50
SyntaxError: invalid syntax
>>> # bcz these keywords are reserved keywords
>>> with = 'java'
SyntaxError: invalid syntax
>>> w = 'java'
>>> w
'java'
>>> with = 'java'
SyntaxError: invalid syntax
>>> # if we want to use with then change case sensitivity
>>> With = 'java'
>>> With
'java'
>>> # Python is case sensitive language
>>> a = 1
>>> a=1
>>> # PEP8 proposal
>>> ##############################
>>> 'Saurabh'
'Saurabh'
>>> "Saurabh"
'Saurabh'
>>> Saurabh # it will be treated as an identifier
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Saurabh # it will be treated as an identifier
NameError: name 'Saurabh' is not defined
>>> print('Hello good evening to all participants')
Hello good evening to all participants
>>> print('Hello \ngood evening \nto all participants')
Hello 
good evening 
to all participants
>>> # \n for a new line
>>> print('Hello \ngood evening \n to all participants')
Hello 
good evening 
 to all participants
>>> print('Hello \tgood evening \tto all participants') # \t for tab
Hello 	good evening 	to all participants
>>> ########################
>>> print(123456789)
123456789
>>> print('My mobile number is:',9822131415)
My mobile number is: 9822131415
>>> #####################
>>> name = 'Umesh'
>>> name
'Umesh'
>>> age = 25
>>> age
25
>>> print('My name is:',name)
My name is: Umesh
>>> print('My name is:',name,'and age is:',age)
My name is: Umesh and age is: 25
>>> ####################
>>> print('My name is:','name','and age is:',age)
My name is: name and age is: 25
>>> #############
>>> 'avinash' # object
'avinash'
>>> avinash # identifier
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    avinash # identifier
NameError: name 'avinash' is not defined
>>> ####################
>>> # Space is also considered as a block
>>> print('            ')
            
>>> print('     hello       ')
     hello       
>>> ####################################
>>> print('My name is {} and age is {}'.format(name,age))
My name is Umesh and age is 25
>>> # lets change the sequence
>>> print('My name is {} and age is {}'.format(age,name))
My name is 25 and age is Umesh
>>> # here seuquence order matters, but we have a solution
>>> # give the positions
>>> print('My name is {1} and age is {0}'.format(age,name))
My name is Umesh and age is 25
>>> #################################
>>> # format specifiers: int 23 %d, float 12.5 %f, string 'python' %s
>>> name
'Umesh'
>>> age
25
>>> print('My name is %s and age is %d'%(name,age))
My name is Umesh and age is 25
>>> n1 = 'suresh'
>>> n2 = 'ramesh'
>>> n3 = 'mahesh'
>>> n1
'suresh'
>>> n2
'ramesh'
>>> n3
'mahesh'
>>> print('We are 3 friends:%s,%s,%s'%(n1,n2,n3))
We are 3 friends:suresh,ramesh,mahesh
>>> print('We are 3 friends:%s,%s,%s'%(n3,n2,n1))
We are 3 friends:mahesh,ramesh,suresh
>>> print('We are 3 friends:%s,%s'%(n3,n2,n1))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print('We are 3 friends:%s,%s'%(n3,n2,n1))
TypeError: not all arguments converted during string formatting
>>> print('We are 3 friends:%s,%s,%s'%(n3,n2))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print('We are 3 friends:%s,%s,%s'%(n3,n2))
TypeError: not enough arguments for format string
>>> print('My name is %s and age is %d'%(name,age))
My name is Umesh and age is 25
>>> print('My name is %s and age is %d'%(age,name))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print('My name is %s and age is %d'%(age,name))
TypeError: %d format: a number is required, not str
>>> print('My name is %s and age is %f'%(name,age))
My name is Umesh and age is 25.000000
>>> age
25
>>> 


*******************************DAY3********************************************

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Operators in Python
>>> # used to perform some operations
>>> # Arithmatic operator:
>>> # + - * / % // **
>>> 12 + 20
32
>>> 20 - 10
10
>>> 3 * 4
12
>>> 3/4
0.75
>>> # % mod operator: it gives remainder
>>> 23 % 10
3
>>> 4 % 2
0
>>> # // floor division
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 4/5
0.8
>>> 4//5
0
>>> 5/3
1.6666666666666667
>>> 5//3
1
>>> # ** exponential/ power of operator
>>> 2 ** 4
16
>>> 3 ** 2
9
>>> 25 ** 2
625
>>> ##########################
>>> # Assignment operator
>>> a = 100
>>> a
100
>>> a + 100
200
>>> a
100
>>> a += 100 # a = a + 100
>>> a
200
>>> a-= 50
>>> a
150
>>> a *= 2
>>> a
300
>>> a /= 10
>>> a
30.0
>>> a **= 2
>>> a
900.0
>>> a //= 10
>>> a
90.0
>>> 900//10
90
>>> ######################
>>> # Relational operator/ COnditional operators
>>> # These operators alwways results boolean output[True, False]
>>> # < > <= >= == !=
>>> 1 < 0
False
>>> 1 ==  10
False
>>> 'python' == 'Python'
False
>>> 'Python' == 'Python'
True
>>> 34 != 23
True
>>> ##############################
>>> # Logical Operators
>>> # associated with conditional checking
>>> # here we need the help of comparison operators
>>> # 3 options: and or not
>>> # It is based on Truth Table
>>> # and Truth table
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> name = 'Snehal'
>>> name
'Snehal'
>>> age = 23
>>> age
23
>>> # nw check the conditions
>>> name == 'Snehal'
True
>>> name == 'Sneha'
False
>>> age == 40
False
>>> # True and True
>>> name == 'Snehal' and age == 23
True
>>> name == 'Shital' and age == 23
False
>>> name == 'Snehal' and age == 34
False
>>> name == 'Shital' and age == 3
False
>>> # value of True is 1
>>> int(True)
1
>>> # value of False is 0
>>> int(False)
0
>>> 10 and 20
20
>>> # x and y
>>> # if ur X is True then return Y
>>> # False means 0,None, ''
>>> # if ur X is False then return X
>>> 0 and 33
0
>>> False and 'python'
False
>>> ########################
>>> # or operator
>>> 10 and 0
0
>>> False and 10
False
>>> 'sagar' and 'pramod'
'pramod'
>>> '' and 'pramod'
''
>>> None and 'pramod'
>>> None
>>> 'sagar' and 10
10
>>> 'sagar' and 93457345
93457345
>>> #####################################
>>> # or operator
>>> name
'Snehal'
>>> age
23
>>> name == 'Snehal' or age == 90
True
>>> name == 'ehal' or age == 90
False
>>> ###########################
>>> # Not: negation
>>> not True
False
>>> not False
True
>>> not name == 'Vikas'
True
>>> not age == 23
False
>>> age == 23
True
>>> ##############################
>>> # Membership
>>> # it  checks either an element is a member of a sequence or not
>>> 'hema' in 'hema malini'
True
>>> # it has 2 types: in , not it
>>> 'jaya' in 'hema malini'
False
>>> # it results boolean output
>>> 12 in [10,11,12,13]
True
>>> 120 in [10,11,12,13]
False
>>> 120 not in [10,11,12,13]
True
>>> 'abc' not in 'prq'
True
>>> #######################
>>> # Identity operator
>>> # its check id / address of an objects
>>> # if address matches then it results True
>>> # otherwise False
>>> # 2 types:
>>> # is , is not
>>> #-----------
>>> 10 is 10
True
>>> 'py' is 'Py'
False
>>> id('py')
2945141591880
>>> id('Py')
2945181503928
>>> 'py' is not 'Py'
True
>>> #############################
>>> # interview question
>>> 10 ==  10
True
>>> 10 == 10.0
True
>>> 10 is 10
True
>>> 10 is 10.0
False
>>> id(10)
140723146511680
>>> id(10.0)
2945141292080
>>> # id's are different hence False
>>> # Content equality and address equality
>>> 10 == 10.0
True
>>> # it does contents equality
>>> 10 is 10.0
False
>>> # it does address equality
>>> # == is content equality
>>> # is : address equality
>>> 


*****************************DAY4******************************************

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Data types in Python
>>> # Numeric: int, float, complex
>>> # int: base 10 [0-9]
>>> type(10)
<class 'int'>
>>> 125827682743687624876782468234
125827682743687624876782468234
>>> # in python we dont have a limit for int value
>>> # float: floating values
>>> 1.3
1.3
>>> 14.55
14.55
>>> 456.22
456.22
>>> type(456.22)
<class 'float'>
>>> # complex: real + img
>>> 3 + 0j
(3+0j)
>>> type(3+0j)
<class 'complex'>
>>> 3 + 0J
(3+0j)
>>> 4j
4j
>>> type(4j)
<class 'complex'>
>>> #########################
>>> # Boolean:True False
>>> # when we are comparing the objects/ doing the conditional check
>>> # it result boolean output
>>> True
True
>>> False
False
>>> 2 > 3
False
>>> 3 == 3
True
>>> #######################
>>> # String
>>> # Global data type
>>> # bcz it accepts everything
>>> # syntax: '' or ""
>>> ''
''
>>> ""
''
>>> type('')
<class 'str'>
>>> type("")
<class 'str'>
>>> type('''''')
<class 'str'>
>>> ####
>>> '123123214'
'123123214'
>>> '$^%$^%&^#!'',.;'
'$^%$^%&^#!,.;'
>>> '$^%$^%&^#!'',.;
SyntaxError: EOL while scanning string literal
>>> '$^%$^%&^#!'',.;'
'$^%$^%&^#!,.;'
>>> "$^%$^%&^#!'',.;"
"$^%$^%&^#!'',.;"
>>> ################
>>> 'my name is 'Amruta''
SyntaxError: invalid syntax
>>> # Rule: if we have single quote outside , inside u must use " viceversa
>>> "''"
"''"
>>> '""'
'""'
>>> ''''


''''
SyntaxError: EOL while scanning string literal
>>> 'my name is "Amruta"'
'my name is "Amruta"'
>>> "my name is 'Amruta'"
"my name is 'Amruta'"
>>>  #####################
>>> # Features of a String
>>> # Background data structure : Array
>>> s = 'pythonist'
>>> s
'pythonist'
>>> # if i want to count total elements in a list
>>> # will use len() fucntion
>>> len(s)
9
>>> len(s)-1
8
>>> # indexing gives an access to a single element
>>> # access t
>>> s[
	]
SyntaxError: invalid syntax
>>> s[2]
't'
>>> s[6]
'i'
>>> s[1]
'y'
>>> type(s)
<class 'str'>
>>> s
'pythonist'
>>> s[8]
't'
>>> # space is also oen block
>>> a = 'amit shaha'
>>> a
'amit shaha'
>>> a[4]
' '
>>> a[3]
't'
>>> b = '@#$%'
>>> b[2]
'$'
>>> b[0]
'@'
>>> #################
>>> s
'pythonist'
>>> s[2]
't'
>>> # to access a subpart/substring from main string then use Slicing
>>> s[:]
'pythonist'
>>> #[start:stop]
>>> # [start_index:stop_index]
>>> # lets acces thon
>>> s[2:5]
'tho'
>>> # stop is exclusive
>>> s[5]
'n'
>>> s[2:6]
'thon'
>>> # python
>>> s[0:6]
'python'
>>> # slicing always starts from 0
>>> s[:6]
'python'
>>> # onist
>>> s[4:9]
'onist'
>>> # slicing readches upto end if index not provided
>>> s[:]
'pythonist'
>>> s[4:]
'onist'
>>> # slicing also has step option
>>> s[::]
'pythonist'
>>> # s[start:stop:step]
>>> s[::1]
'pythonist'
>>> s[::2]
'ptoit'
>>> s[::20000]
'p'
>>> # We have +ve and - ve indexing
>>> s[0]
'p'
>>> s[-9]
'p'
>>> s[-5]
'o'
>>> #slicing
>>> s
'pythonist'
>>> s[-7:]
'thonist'
>>> # when we hv step 1 it progress from left to right always
>>> s
'pythonist'
>>> s[-5:]
'onist'
>>> # BUT if WE HAVE STEPING OF -1
>>> # THen it progress from right to left
>>> s
'pythonist'
>>> s[::1]
'pythonist'
>>> s[::-1] #go from right to left/ will get reverse order
'tsinohtyp'
>>> # reverse the string
>>> a
'amit shaha'
>>> a[::-1]
'ahahs tima'
>>> #############
>>> a
'amit shaha'
>>> a[-4::]
'haha'
>>> a[-4::-1]
'hs tima'
>>> # haha reverse
>>> # ahah
>>> a[-1::-1]
'ahahs tima'
>>> a[-1:-5:-1]
'ahah'
>>> a
'amit shaha'
>>> # reverse amit
>>> # tima
>>> a[-7::-1]
'tima'
>>> #####################
>>> a
'amit shaha'
>>> # String methods
>>> a.upper()
'AMIT SHAHA'
>>> # A of amit Capital
>>> a.capitalize()
'Amit shaha'
>>> #  so A and S should be capital
>>> a.title()
'Amit Shaha'
>>> # repalce shaha with patil
>>> a.replace('shaha','Patil')
'amit Patil'
>>> #all these changes are temp.
>>> a
'amit shaha'
>>> # how to give multiline string
>>> 'jkhjhjks lksjldkfj'
'jkhjhjks lksjldkfj'
>>> 'jkhskjfh \
jkbsjkfbkjbkj \
bksdfkjbkjsdf\
234235345345
SyntaxError: EOL while scanning string literal
>>> 'jkhskjfh \
jkbsjkfbkjbkj \
bksdfkjbkjsdf\
234235345345'
'jkhskjfh jkbsjkfbkjbkj bksdfkjbkjsdf234235345345'
>>> 'jkhskjfh\n\
jkbsjkfbkjbkj\n\
bksdfkjbkjsdf\n\
234235345345'
'jkhskjfh\njkbsjkfbkjbkj\nbksdfkjbkjsdf\n234235345345'
>>> print('jkhskjfh\n\
jkbsjkfbkjbkj\n\
bksdfkjbkjsdf\n\
234235345345')
jkhskjfh
jkbsjkfbkjbkj
bksdfkjbkjsdf
234235345345
>>> s
'pythonist'
>>> s[::2]
'ptoit'
>>> s[1::2]
'yhns'
>>> 'madam'[::-1]
'madam'
>>> s1 = 'madam'
>>> s2 = 'Madam'
>>> s1 == s2
False
>>> s1[::-1] == s2[::-1]
False
>>> '121' == '121'[::-1]
True
>>> s
'pythonist'
>>> 


************************************DAY 5*******************************************

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String and its methods
>>> s =
SyntaxError: invalid syntax
>>> s = 'today its nice day'
>>> s
'today its nice day'
>>> # upper: all elements will be in caps
>>> s.upper()
'TODAY ITS NICE DAY'
>>> s1 =  'JOSEPH'
>>> s1
'JOSEPH'
>>> # i want in lower case
>>> s1.lower()
'joseph'
>>> #####
>>> s
'today its nice day'
>>> # t i want in caps
>>> s.title()
'Today Its Nice Day'
>>> s.capitalize()
'Today its nice day'
>>> #####
>>> # count
>>> s
'today its nice day'
>>> # count i
>>> s.count('i')
2
>>> # if something is not present
>>> s
'today its nice day'
>>> s.count('zebra')
0
>>> s.count('I')
0
>>> s.count('Today')
0
>>> ######
>>> # index
>>> s
'today its nice day'
>>> # returns an index of given substring/character
>>> s.index('a')
3
>>> s[3]
'a'
>>> s.index('its')
6
>>> # we try to findout index of missing substring
>>> s.index('java')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.index('java')
ValueError: substring not found
>>> # Q. if we try to find out index and count of something which is nt present then what will happn?
>>> s
'today its nice day'
>>> s.index('a')
3
>>> # index gives u lowest index of it
>>> # we can also use slicing to check index of next char/substring
>>> s
'today its nice day'
>>> s[6:]
'its nice day'
>>> s[6:].index('a')
10
>>> # to get index of highest char use rindex
>>> s.rindex('a')
16
>>> s[16]
'a'
>>> s.index('a')
3
>>> s.rindex('a')
16
>>> #####
>>> 'aaaaa'.index('a')
0
>>> 'aaaaa'.rindex('a')
4
>>> #########
>>> # find()
>>> # will return an index
>>> s
'today its nice day'
>>> s.find('nice')
10
>>> s[10]
'n'
>>> s.index('nice')
10
>>> # difference is
>>> s.find('java')
-1
>>> s.index('java')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s.index('java')
ValueError: substring not found
>>> # differentiate between find and index of a string
>>> #########
>>> nm = '     rakesh lipare    '
>>> nm
'     rakesh lipare    '
>>> # remoce spaces present in suffix and prefix
>>> # use strip() method
>>> nm.strip()
'rakesh lipare'
>>> # above change is temp.
>>> nm
'     rakesh lipare    '
>>> nm = '****rakesh lipare******'
>>> nm
'****rakesh lipare******'
>>> nm.strip('*')
'rakesh lipare'
>>> nm = '****rakesh lipare$$$$'
>>> nm
'****rakesh lipare$$$$'
>>> nm.strip('*$')
'rakesh lipare'
>>> nm.strip('$*')
'rakesh lipare'
>>> nm
'****rakesh lipare$$$$'
>>> nm.strip('*re')
'akesh lipare$$$$'
>>> nm.strip('*re$')
'akesh lipa'
>>> #########
>>> nm = 'may$$**    uri'
>>> nm
'may$$**    uri'
>>> nm.strip('$* ')
'may$$**    uri'
>>> # in this case use repalce
>>> # replace
>>> nm.replace('$',' ')
'may  **    uri'
>>> nm.replace('$','')
'may**    uri'
>>> nm.replace('** ','')
'may$$   uri'
>>> nm
'may$$**    uri'
>>> nm
'may$$**    uri'
>>> nm.replace('$* ','')# this will work in new python
'may$$**    uri'
>>> nm.replace('$','').replace('*','').replace(' ','')
'mayuri'
>>> ############
>>> nm = 'AsHwIn'
>>> nm
'AsHwIn'
>>> nm.casefold()
'ashwin'
>>> 'ashwin' == nm
False
>>> 'ashwin' == nm.casefold()
True
>>> 'AmiTabhBachHaN'
'AmiTabhBachHaN'
>>> 'AmiTabhBachHaN'.casefold()
'amitabhbachhan'
>>> 'AmiTabhBachHaN'.lower()
'amitabhbachhan'
>>> # differencce betwen lower and casefold????
>>> ####################
>>> nm
'AsHwIn'
>>> s
'today its nice day'
>>> # s. after dot wait for 3-4 sec it will listout all methods of string
>>> # shortcut to use method of str.
>>> # after s. hit the tab and if u know the start of any method then give it and tab
>>> # it will appear
>>> ##########
>>> s
'today its nice day'
>>> # convert string to list of string
>>> s.split()
['today', 'its', 'nice', 'day']
>>> k = s.split()
>>> k
['today', 'its', 'nice', 'day']
>>> type(k)
<class 'list'>
>>> k
['today', 'its', 'nice', 'day']
>>> k[::-1]
['day', 'nice', 'its', 'today']
>>> # spliting criteria is a space
>>> # if we want to choose another splitting criteria
>>> s
'today its nice day'
>>> # split on the basis of nice
>>> s.split('nice')
['today its ', ' day']
>>> 'ramesh,suresh,dinesh'.split(',')
['ramesh', 'suresh', 'dinesh']
>>> ##############
>>> k
['today', 'its', 'nice', 'day']
>>> # i want to convert into a str.
>>> k.join(' ')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    k.join(' ')
AttributeError: 'list' object has no attribute 'join'
>>> ' '.join(k)
'today its nice day'
>>> '--'.join(k)
'today--its--nice--day'
>>> ''.join(k)
'todayitsniceday'
>>> ##############
>>> fname = 'aarti patil'
>>> fname
'aarti patil'
>>> # check fname start with a or nt
>>> fname.startswith('a') #return boolean output
True
>>> fname.startswith('D')
False
>>> # if we want to check end
>>> fname.endswith('l')
True
>>> fname.endswith('patil')
True
>>> fname.endswith('Patil')
False
>>> 'patil' == 'Patil'
False
>>> 


**************************************DAY 6 *************************************

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String methods
>>> s = 'raKeSh'
>>> s
'raKeSh'
>>> # convert lower to upper and viceversa
>>> s.swapcase()
'RAkEsH'
>>> #####################
>>> # is type of method
>>> # is methods gives a boolean output
>>> s
'raKeSh'
>>> s.isalpha()
True
>>> s = 'abc123'
>>> s
'abc123'
>>> s.isalnum()
True
>>> s.isalpha()
False
>>> a = '1234'
>>> a.isdigit()
True
>>> s.isdigit()
False
>>> s1 = '   '
>>> s1.isspace()
True
>>> 'hello my number is:9866345123'
'hello my number is:9866345123'
>>> 'hello my number is:9866345123'.split(':')
['hello my number is', '9866345123']
>>> 'hello my number is:9866345123'.split(':')[1]
'9866345123'
>>> 'hello my number is:9866345123'.split(':')[1].isdigit()
True
>>> #################
>>> # Assignment: check other string methods
>>> ####################################
>>> # List:
>>> # How to declare a list?
>>> []
[]
>>> list()
[]
>>> type([])
<class 'list'>
>>> ###########
>>> # Feature of a list
>>> # Background data structure is array
>>> # hence it supports indexing
>>> # it supports slicing
>>> #-------------------
>>> k = [10,20,30,40,50]
>>> k
[10, 20, 30, 40, 50]
>>> type(k)
<class 'list'>
>>> e = [1 2 3 4]
SyntaxError: invalid syntax
>>> # , is used as a seperator
>>> k
[10, 20, 30, 40, 50]
>>> # index
>>> # +ve indexing
>>> k[0]
10
>>> k[2]
30
>>> # -ve indexing
>>> k[-1]
50
>>> k[-4]
20
>>> # Slicing
>>> k[:]
[10, 20, 30, 40, 50]
>>> k[3:]
[40, 50]
>>> k[::-1]
[50, 40, 30, 20, 10]
>>> k[-2:-4:-1]
[40, 30]
>>> ############
>>> # it accepts homo./hetro. values
>>> k
[10, 20, 30, 40, 50]
>>> # in k we have all elements of int type
>>> w = [12,34.5,'python',4+5j]
>>> w
[12, 34.5, 'python', (4+5j)]
>>> ###########
>>> # It preserves sequence order
>>> ###########
>>> # Duplicates are allowed
>>> l = [1,2,1,1,1,1]
>>> l
[1, 2, 1, 1, 1, 1]
>>> ############
>>> # List is Mutable data type
>>> k
[10, 20, 30, 40, 50]
>>> id(k)
1716868357000
>>> # lets change the list
>>> # using index we can change element
>>> k[-1]
50
>>> k[-1] = 500
>>> k
[10, 20, 30, 40, 500]
>>> id(k)
1716868357000
>>> k
[10, 20, 30, 40, 500]
>>> # lets replace 20,30 by 100,20
>>> # 100 and 200
>>> k[1:3]
[20, 30]
>>> k[1:3] = [100,200]
>>> k
[10, 100, 200, 40, 500]
>>> id(k)
1716868357000
>>> # when we are performing the changes is an object, and changes persist in the same
>>> # here new object is not required to save the changes
>>> # then that data type is MUTABLE
>>> # suppose we want to add a new element
>>> k
[10, 100, 200, 40, 500]
>>> k.append('java')
>>> k
[10, 100, 200, 40, 500, 'java']
>>> # append()will add a single element at the end
>>> ###########################
>>> # if we want to check doc. of any method from data structure then use help()
>>> help(k.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> # now if  i want to check all the methods of a list
>>> dir(k)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> k
[10, 100, 200, 40, 500, 'java']
>>> id(k)
1716868357000
>>> # clear
>>> help(k.clear)
Help on built-in function clear:

clear() method of builtins.list instance
    Remove all items from list.

>>> k.clear()
>>> k
[]
>>> id(k)
1716868357000
>>> #####
>>> a = ['A',12,30,50,100,'B']
>>> a
['A', 12, 30, 50, 100, 'B']
>>> id(a)
1716868918920
>>> # copy()
>>> help([].copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> # copy method is used to create a new copy of ur object
>>> # new object will have same elements as that of old one
>>> a
['A', 12, 30, 50, 100, 'B']
>>> b = a.copy()
>>> b
['A', 12, 30, 50, 100, 'B']
>>> id(a)
1716868918920
>>> id(b)
1716868936136
>>> # here id's are different
>>> # means a new object with same element gets created
>>> # lets try to change any of list
>>> b
['A', 12, 30, 50, 100, 'B']
>>> b[0]
'A'
>>> b[0] = 'Amit'
>>> b
['Amit', 12, 30, 50, 100, 'B']
>>> # now check a
>>> a
['A', 12, 30, 50, 100, 'B']
>>> # copy() creates an individual objects using same data
>>> ####################
>>> # i want to create an object with same value and same id
>>> # it is known as Deep copy
>>> c = a
>>> a
['A', 12, 30, 50, 100, 'B']
>>> c
['A', 12, 30, 50, 100, 'B']
>>> id(a)
1716868918920
>>> id(c)
1716868918920
>>> # here we have same id's
>>> # hence changes performed in any of the object persist in both
>>> a
['A', 12, 30, 50, 100, 'B']
>>> c
['A', 12, 30, 50, 100, 'B']
>>> c[-1]
'B'
>>> c[-1] = 'Baban'
>>> c
['A', 12, 30, 50, 100, 'Baban']
>>> a
['A', 12, 30, 50, 100, 'Baban']
>>> a[2]
30
>>> a[2] = 'C#'
>>> a
['A', 12, 'C#', 50, 100, 'Baban']
>>> #check c
>>> c
['A', 12, 'C#', 50, 100, 'Baban']
>>> # changes persist in both object bcz of same id
>>> ##################
>>> # qQ. What is shallow and deep copy?
>>> # what is difference betwn them?
>>> ###############
>>> #Recap
>>> # shallow copy
>>> s1 = ['amit','dinesh','suresh']
>>> s1
['amit', 'dinesh', 'suresh']
>>> id(s1)
1716868917448
>>> #shallow copy
>>> s2 = s1.copy()
>>> s2
['amit', 'dinesh', 'suresh']
>>> id(s2)
1716868939208
>>> # deep copy
>>> s3 = s1
>>> s3
['amit', 'dinesh', 'suresh']
>>> id(s3)
1716868917448
>>> s3[-1]
'suresh'
>>> s3[-1] = 'ramesh'
>>> s3
['amit', 'dinesh', 'ramesh']
>>> s1
['amit', 'dinesh', 'ramesh']
>>> s2 #shallow copy
['amit', 'dinesh', 'suresh']
>>> 


*********************************DAY 7*************************************


Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List methods:
>>> # how to check the methods of list==> using dir()
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> k = [10,20,10,30,40,10]
>>> k
[10, 20, 10, 30, 40, 10]
>>> # count
>>> help(k.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> k.count(10)
3
>>> k.count(100)
0
>>> ########
>>> # extend()
>>> help(k.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> # iterable???
>>> # it means a collection of multiple elements,objects
>>> # on which we can perform iterations
>>> k
[10, 20, 10, 30, 40, 10]
>>> # examples of iterable: string,list,tuple,set,range,dict
>>> k
[10, 20, 10, 30, 40, 10]
>>> k.extend([1,2,3])
>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3]
>>> k.extend(['A','B'])
>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
>>> ##########
>>> # what is difference between append and extend????
>>> help([].append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> help([].extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> r = []
>>> r
[]
>>> r.append(1)
>>> r
[1]
>>> r.extend(2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    r.extend(2)
TypeError: 'int' object is not iterable
>>> r.extend([2])
>>> r
[1, 2]
>>> # see now actual difference
>>> # if we try to add iterable using append
>>> # it will add complete ietrable as a single element
>>> r
[1, 2]
>>> r.append('Shital')
>>> r
[1, 2, 'Shital']
>>> # if we try to add same using extend then it will add each char/block
>>> # separatly
>>> r.extend('Shital')
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l']
>>> ####### Example 2
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l']
>>> r.append([10,20])
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l', [10, 20]]
>>> r.extend([10,20])
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l', [10, 20], 10, 20]
>>> # extend does not accepts int,float,complex,boolean
>>> r.extend(34.66)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    r.extend(34.66)
TypeError: 'float' object is not iterable
>>> r.extend(True)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    r.extend(True)
TypeError: 'bool' object is not iterable
>>> ######################
>>> # List of list
>>> g = [[10,20],[40,50]]
>>> g
[[10, 20], [40, 50]]
>>> g[0]
[10, 20]
>>> g[-1]
[40, 50]
>>> # change 40 to 400
>>> g[-1][0]
40
>>> g[-1][0] = 400
>>> g
[[10, 20], [400, 50]]
>>> # lets add name amruta in 10,20 list
>>> g
[[10, 20], [400, 50]]
>>> g[0]
[10, 20]
>>> g[0].append('Amruta')
>>> g
[[10, 20, 'Amruta'], [400, 50]]
>>> ##########
>>> help(k.index)
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.list instance
    Return first index of value.
    
    Raises ValueError if the value is not present.

>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
>>> k.index('A')
9
>>> k.index(10)
0
>>> k.index(400)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    k.index(400)
ValueError: 400 is not in list
>>> ###############
>>> help(k.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
>>> # add 500 between 30 and 40
>>> k[4]
40
>>> k.insert(4,500)
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 'B']
>>> # Interview question
>>> # add element 90 between A and B using -ve indexing
>>> k.insert(-1,90)
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B']
>>> # after B i want to add Hello using insert only
>>> k.insert(0,'Hello')
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B']
>>> len(k)
14
>>> k.insert(14,'Hello')
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B', 'Hello']
>>> len)k)
SyntaxError: invalid syntax
>>> len(k)
15
>>> k[-15]
'Hello'
>>> ####################
>>> help(k.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B', 'Hello']
>>> k.pop()
'Hello'
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B']
>>> k.pop()
'B'
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90]
>>> # we can remove one element at a time
>>> # remove element at specific index
>>> # remove hello
>>> k.pop(0)
'Hello'
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90]
>>> # remove A
>>> k.pop(-2)
'A'
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 90]
>>> k.pop()
90
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3]
>>> # if element nt present in the list and we try to remove it
>>> k.pop(56)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    k.pop(56)
IndexError: pop index out of range
>>> ###############
>>> # pop is used to remove one element at a time
>>> # it can not remove multiple elements
>>> #####################
>>> # if we want to remove element by giving element as an input
>>> # then use remove()
>>> help(k.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3]
>>> k.remove(10)
>>> k
[20, 10, 30, 500, 40, 10, 1, 2, 3]
>>> k.remove(3)
>>> # remove is value based
>>> # pop is index based
>>> # Q. difference between remove and pop
>>> #--------------------
>>> # pop removes and return an element
>>> # remove doesnt return an element
>>> #----------------------
>>> # pop() default removes last element
>>> # remove() needs value always
>>> k
[20, 10, 30, 500, 40, 10, 1, 2]
>>> k.remove()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    k.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> k.pop()
2
>>> #--------------------------------
>>> help(k.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.

>>> #Reverse *IN PLACE*. inplace means permanent change
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> k.reverse()
>>> k
[1, 10, 40, 500, 30, 10, 20]
>>> k.reverse()
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> # this reverse is permenant
>>> # if we want temp. reverse then use slicing
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> k[::-1]
[1, 10, 40, 500, 30, 10, 20]
>>> # using builtin function reversed() we can reverse the sequence
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> reversed(k) #it give output in the form of object
<list_reverseiterator object at 0x00000247F1D40240>
>>> # when we get an output in the form of object, then to see actual values
>>> # u need to convert it into another data type
>>> list(reversed(k))
[1, 10, 40, 500, 30, 10, 20]
>>> # Q. differentiate between reverse() and reversed()
>>> # reverse():is a method of list
>>> # reversed() is built in function (python)
>>> #----------------------
>>> # reveres(): in -place
>>> # reversed(): temp.
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> # reverse() : does not return anything
>>> # reversed(): returns output in the form of object
>>> #------------------------
>>> # sort()
>>> help(k.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Stable sort *IN PLACE*.

>>> d = [10,99,34,0,4,34,56,1,3]
>>> d
[10, 99, 34, 0, 4, 34, 56, 1, 3]
>>> d.sort()
>>> d
[0, 1, 3, 4, 10, 34, 34, 56, 99]
>>> # sort in ascending order default
>>> # but if i want to sort in descending order
>>> # use reverse = True
>>> d.sort(reverse=True)
>>> d
[99, 56, 34, 34, 10, 4, 3, 1, 0]
>>> h = [12,0,'A',300,'Z','B']
>>> h
[12, 0, 'A', 300, 'Z', 'B']
>>> h.sort()
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    h.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> o = ['Z','C','G','A','M']
>>> o
['Z', 'C', 'G', 'A', 'M']
>>> o.sort()
>>> o
['A', 'C', 'G', 'M', 'Z']
>>> 


**********************************DAY 8*********************************************

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List remaining methods
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # sort(): default ascending order
>>> p = [23,100,9,3,45,67,88,100]
>>> p
[23, 100, 9, 3, 45, 67, 88, 100]
>>> help(p.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Stable sort *IN PLACE*.

>>> p.sort(key=min)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    p.sort(key=min)
TypeError: 'int' object is not iterable
>>> p
[23, 100, 9, 3, 45, 67, 88, 100]
>>> min(p)
3
>>> max(p)
100
>>> min(23)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    min(23)
TypeError: 'int' object is not iterable
>>> d = ['ram','Abhijeet','ashok','nilesh','Abhiram']
>>> d
['ram', 'Abhijeet', 'ashok', 'nilesh', 'Abhiram']
>>> len(d)
5
>>> d.sort(key=len)
>>> d
['ram', 'ashok', 'nilesh', 'Abhiram', 'Abhijeet']
>>> # sorted the list in ascending order
>>> ##########################
>>> # Tuple
>>> # syntax: ()
>>> ()
()
>>> type(())
<class 'tuple'>
>>> # create an empty  tuple
>>> ()
()
>>> tuple()
()
>>> a = ()
>>> a
()
>>> type(a)
<class 'tuple'>
>>> b = tuple()
>>> b
()
>>> type(b)
<class 'tuple'>
>>> #############
>>> # Features: It has almost all features same as that of List
>>> # except one
>>> # List is Mutable &
>>> # Tuple is Immutable
>>> #######################
>>> # why tuple is immutable???
>>> t = (10,20,30,40)
>>> # aasignment: check indexing and slicing over a tuple
>>> t
(10, 20, 30, 40)
>>> # lets try to change 40 to 400
>>> t[-1]
40
>>> t[-1] = 400
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[-1] = 400
TypeError: 'tuple' object does not support item assignment
>>> ##############
>>> # lets check method supported by tuple
>>> dir(t)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> # it contains only 2 methods:'count', 'index'
>>>  # which are nt used for perfroming manipulation
>>> # check method of a list
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # list many methods are used for direct manipulation of data
>>> # hence list is mutable and tuple is immutable
>>> #################################
>>> # Q. Interview
>>> t1 = (1,2,3)
>>> t1
(1, 2, 3)
>>> t2 = (5,6,7)
>>> t2
(5, 6, 7)
>>> t1 + t2
(1, 2, 3, 5, 6, 7)
>>> t1
(1, 2, 3)
>>> t2
(5, 6, 7)
>>> # Q.  which one is better????
>>> # list or tuple???
>>> # it depends on the requirement of a business
>>> ####################
>>> # Q. why list take more memory than tuple
>>> # Example
>>> t1
(1, 2, 3)
>>> l1 = [1,2,3]
>>> l1
[1, 2, 3]
>>> # now check the memory for bot
>>> # both
>>> t1.__sizeof__()
48
>>> l1.__sizeof__()
64
>>> # what is the reason of above case?????
>>> # which one is faster tuple of list???
>>> ########################################
>>> # Set:
>>> # Packing and Unpacking of tuple: VVIMP
>>> 10
10
>>> type(10)
<class 'int'>
>>> 10,
(10,)
>>> type(10,)
<class 'int'>
>>> type((10,))
<class 'tuple'>
>>> # default comma separated values in python are Tuple
>>> 10,20,30
(10, 20, 30)
>>> 'A','F','G'
('A', 'F', 'G')
>>> # Paacking: grouping multiple objects in a single identifier
>>> 'k','g',f'
SyntaxError: EOL while scanning string literal
>>> 'k','g','f'
('k', 'g', 'f')
>>> film = 'k','g','f'
>>> film
('k', 'g', 'f')
>>> #rx:2
>>> f = 12.3,45.55,60.77
>>> f
(12.3, 45.55, 60.77)
>>> # Unpacking: opposite of packing
>>> # to unfold packed values, we need multiple identifiers
>>> film
('k', 'g', 'f')
>>> # how many elements present in film
>>> len(film)
3
>>> x,y,z = film # her k,g,f will be assigned to x,y,z resp.
>>> x
'k'
>>> y
'g'
>>> z
'f'
>>> ###########
>>> p,q,q = 100,200,300
>>> p
100
>>> q
300
>>> q = 200
>>> q = 300
>>> q
300
>>> p1,q1,r1 = 100,200,300
>>> p1
100
>>> q1
200
>>> r1
300
>>> ############
>>> ##############################
>>> # SET
>>> # Syntax:
>>> # Empty set
>>> s = set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> ############
>>> # Syntax:
>>> s = {1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> a = {'A','B','C'}
>>> a
{'B', 'A', 'C'}
>>> # Set doesnt preserve sequence order
>>> #########
>>> d = {1,2,'A','B'}
>>> d
{1, 2, 'B', 'A'}
>>> # it suppports homo. and hetro type of data
>>> #########
>>> # duplicates are not allowed
>>> f = {1,2,3,4,1,1,1,1,1,1,1}
>>> f
{1, 2, 3, 4}
>>> r = {1,2,2,2,2,3,3,3,1,1,1,1,}
>>> r
{1, 2, 3}
>>> e = {12,0,1,'2','23'}
>>> e
{0, 1, '2', 12, '23'}
>>> ##############
>>> # Indexing is not supported
>>> s
{1, 2, 3, 4, 5}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> # no slicing
>>> s[::-1]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    s[::-1]
TypeError: 'set' object is not subscriptable
>>> # No array data structure
>>> # Background data struucture is a HASH TABLE
>>> ###############
>>> # Set is Mutable in nature
>>> s
{1, 2, 3, 4, 5}
>>> id(s)
2141431803976
>>> s.update({10,20,30})
>>> s
{1, 2, 3, 4, 5, 10, 20, 30}
>>> s.update({'A'})
>>> s
{1, 2, 3, 4, 5, 10, 20, 'A', 30}
>>> ###########
>>> # can we use empty {} to create an empty set
>>> {}
{}
>>> type({})
<class 'dict'>
>>> {()}
{()}
>>> type({()})
<class 'set'>
>>> type({[]})
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    type({[]})
TypeError: unhashable type: 'list'
>>> t1
(1, 2, 3)
>>> s
{1, 2, 3, 4, 5, 10, 20, 'A', 30}
>>> d = set()
>>> d
set()
>>> d.update(t1)
>>> d
{1, 2, 3}
>>> # www.programiz.com
>>> 


**************************************DAY 9*******************************

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # SET
>>> set()
set()
>>> s = {1,2,1,3,1}
>>> s
{1, 2, 3}
>>> # Set is mutable data type
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s
{1, 2, 3}
>>> s.add(10)
>>> s
{10, 1, 2, 3}
>>> # insertion order is nt preserved
>>> s.add('KGF')
>>> s
{1, 2, 3, 10, 'KGF'}
>>> # bcz its background data structure is Hash Table
>>> # a = {23,4,10,79,56,10,4}
>>> # for this working of Hash table
>>> # lets assume hash function is mod %
>>> 23 % 10
3
>>> 4 % 10
4
>>> 10 % 10
0
>>> 79 % 10
9
>>> 56 % 10
6
>>> ########################
>>> # Methods of set
>>> s
{1, 2, 3, 10, 'KGF'}
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> # SET operations
>>> # intersection
>>> # Fetch common elements from 2 sets
>>> s1 = {1,2,3}
>>> s1
{1, 2, 3}
>>> s2 = {2,3,4,5}
>>> s2
{2, 3, 4, 5}
>>> s1.intersection(s2)
{2, 3}
>>> ms1 = 'this is sample program'
>>> ms2 = 'program is simple'
>>> # find out common contents from ms1 and ms2
>>> # COnveert string to set
>>> ms_1 = set(ms1)
>>> ms_1
{' ', 'e', 'g', 'r', 'm', 'p', 'i', 'l', 's', 'o', 'h', 't', 'a'}
>>> # here it gives characters
>>> # but we want  words
>>> # so need to convert into list of string
>>> ms1.split()
['this', 'is', 'sample', 'program']
>>> ms_1 = set(ms1.split())
>>> ms_1
{'is', 'program', 'sample', 'this'}
>>> ms_2 = set(ms2.split())
>>> ms_2
{'is', 'program', 'simple'}
>>> ms_1.intersection(ms_2)
{'is', 'program'}
>>> ####################
>>> # union
>>> # Take all elements from both set, without duplicates
>>> s1
{1, 2, 3}
>>> s2
{2, 3, 4, 5}
>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> ms_1.union(ms_2)
{'is', 'program', 'sample', 'this', 'simple'}
>>> ################
>>> # difference
>>> # fetch uncommon elements from set 1
>>> s1
{1, 2, 3}
>>> s2
{2, 3, 4, 5}
>>> s1.difference(s2)
{1}
>>> s2.difference(s1)
{4, 5}
>>> ##########
>>> # symmetric difference
>>> # fetch uncommon elements from set 1 and set 2 as well
>>> s1.symmetric_difference(s2)
{1, 4, 5}
>>> ####################################
>>> # Using operator if we want to apply set operations
>>> s1
{1, 2, 3}
s
>>> s2
{2, 3, 4, 5}
>>> s1 & s2
{2, 3}
>>> # & : intersection
>>> #######
>>> s1 | s2
{1, 2, 3, 4, 5}
>>> # | gives union
>>> ##########
>>> s1 - s2
{1}
>>> # - gives : difference
>>> s1.difference(s2)
{1}
>>> # Assignment : which operator is used for symmetric difference???
>>> ##################
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> # if we want to perform set operation and we want to store result in set 1
>>> # then go with update options
>>> s
{1, 2, 3, 10, 'KGF'}
>>> id(s)
2687694096648
>>> s1
{1, 2, 3}
>>> # now use difference_update option
>>> s.difference(s1) #uncommon
{10, 'KGF'}
>>> s
{1, 2, 3, 10, 'KGF'}
>>> s1
{1, 2, 3}
>>> # no any set gets changed
>>> s.difference_update(s1)
>>> s
{10, 'KGF'}
>>> # union
>>> s
{10, 'KGF'}
>>> s1
{1, 2, 3}
>>> s.update(s1)
>>> s
{2, 1, 3, 10, 'KGF'}
>>> ##################
>>> help(s.update)
Help on built-in function update:

update(...) method of builtins.set instance
    Update a set with the union of itself and others.

>>> s
{2, 1, 3, 10, 'KGF'}
>>> s.update(range(101,103))
>>> s
{2, 1, 3, 101, 102, 10, 'KGF'}
>>> s.update(12)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s.update(12)
TypeError: 'int' object is not iterable
>>> s
{2, 1, 3, 101, 102, 10, 'KGF'}
>>> s.add(12)
>>> s
{2, 1, 3, 101, 102, 10, 12, 'KGF'}
>>> # Iterable????
>>> # collection of elements/objects
>>> 10
10
>>> 12.5
12.5
>>> [10,12.5]
[10, 12.5]
>>> [23]
[23]
>>> s.add(12)
>>> s.update(120)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    s.update(120)
TypeError: 'int' object is not iterable
>>> s.update([120])
>>> s
{2, 1, 3, 101, 102, 10, 12, 'KGF', 120}
>>> # literables: string, list, tuple,set,range(),dict
>>> s
{2, 1, 3, 101, 102, 10, 12, 'KGF', 120}
>>> s.update(10,45)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    s.update(10,45)
TypeError: 'int' object is not iterable
>>> vishwas  = 10,45
>>> type(Vishwas)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    type(Vishwas)
NameError: name 'Vishwas' is not defined
>>> type(vishwas)
<class 'tuple'>
>>> s.update(vishwas)
>>> s
{2, 1, 3, 101, 102, 10, 12, 45, 'KGF', 120}
>>> s.update(('A','java'))
>>> s
{2, 1, 3, 101, 102, 'A', 10, 12, 45, 'KGF', 'java', 120}
>>> ###################
>>> # Difference and similarity between add and update
>>> ##############################
>>> s.discard(120)
>>> s
{2, 1, 3, 101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> # if it is a member then remove, but if its not then do nothing
>>> s.discard(120)
>>> s.discard(1200) #its nt present
>>> ###############
>>> help(s.pop)
Help on built-in function pop:

pop(...) method of builtins.set instance
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> s.pop()
2
>>> s.pop()
1
>>> s
{3, 101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> s.pop()
3
>>> d = set()
>>> d
set()
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    d.pop()
KeyError: 'pop from an empty set'
>>> # Q. DIfference between pop and discard?????
>>> s
{101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> s.pop(102)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    s.pop(102)
TypeError: pop() takes no arguments (1 given)
>>> 
>>> s
{101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> s.discard('KL')
>>> d
set()
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    d.pop()
KeyError: 'pop from an empty set'
>>> d.discard(10)
>>> #################
>>> s
{101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> # remove
>>> s.remove(10)
>>> s
{101, 102, 'A', 12, 45, 'KGF', 'java'}
>>> s.remove(10)# already removed
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    s.remove(10)# already removed
KeyError: 10
>>> #############################

*************************DAY 10***************************************

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # SET methods
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s1 = {1,2,3,4,5}
>>> s1
{1, 2, 3, 4, 5}
>>> s2 = {1,2,3}
>>> help(s1.isdisjoint)
Help on built-in function isdisjoint:

isdisjoint(...) method of builtins.set instance
    Return True if two sets have a null intersection.

>>> s1
{1, 2, 3, 4, 5}
s
>>> 2
2
>>> s2
{1, 2, 3}
>>> s3 = {10,20,30}
>>> s3
{10, 20, 30}
>>> s1
{1, 2, 3, 4, 5}
>>> # we are going to check, unique ness of 2 sets
>>> s3.isdisjoint(s1)
True
>>> # in s3 and s1 we dont have any common value
>>> # hence answer is True
>>> s1.isdisjoint(s2)
False
>>> ##############
>>> help(s1.issubset)
Help on built-in function issubset:

issubset(...) method of builtins.set instance
    Report whether another set contains this set.

>>> s1
{1, 2, 3, 4, 5}
>>> s2
{1, 2, 3}
>>> s2.issubset(s1)
True
>>> s1.issubset(s2)
False
>>> ###################
>>> ##########################
>>> # Dictionary
>>> # Dict
>>> # Syntax:
>>> {}
{}
>>> type({})
<class 'dict'>
>>> set()
set()
>>> ######
>>> {}
{}
>>> dict()
{}
>>> ######
>>> # Features of dict
>>> # dict is a combinition of 2 things
>>> # key and value
>>> {1,2,3}
{1, 2, 3}
>>> type({1, 2, 3})
<class 'set'>
>>> #{key:value}
>>> ##{key:value,key:value,key:value,key:value}
>>> {1:10,2:20,3:30}
{1: 10, 2: 20, 3: 30}
>>> type({1: 10, 2: 20, 3: 30})
<class 'dict'>
>>> ############################
>>> # Dict can contain multiplekey value pair
>>> # there is no inherent limit
>>> # Duplicate keys are not allowed
>>> {1:100,2:200,1:'ABC'} # key 1 appears twice
{1: 'ABC', 2: 200}
>>> # rzn: Background data structure HASH TABLE
>>> # No array
>>> # No indexing
>>> # No slicing
>>> d = {1:10,2:20,3:30,4:40}
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> len(d)
4
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d[0]
KeyError: 0
>>> d[-1]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d[-1]
KeyError: -1
>>> # key playes a role of index
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> d[3]
30
>>> d[1]
10
>>> d1 = {'name':'amol','age':23,'salary':34000}
>>> d1
{'name': 'amol', 'age': 23, 'salary': 34000}
>>> d1['salary']
34000
>>> # using key we can access values associated with it
>>> d2 = {1:[10,20,30,40]}
>>> d2
{1: [10, 20, 30, 40]}
>>> d2[1]
[10, 20, 30, 40]
>>> d2 = {1:{10,20,30,40}}
>>> d2
{1: {40, 10, 20, 30}}
>>> # Duplicate keys not allowed
>>> # but duplicate values are allowed
>>> # interview question
>>> d4 = {1:10,2:10,3:10}
>>> d4
{1: 10, 2: 10, 3: 10}
>>> {1: 10, 1: 10, 1: 10}
{1: 10}
>>> # if we have duplicate keys present in dict then it wil take
>>> # recent key value pair
>>> {1: 10, 1: 10, 1: 20}
{1: 20}
>>> {1:10,
     'A':'Renuka',
     'B':'Boss'}
{1: 10, 'A': 'Renuka', 'B': 'Boss'}
>>> ####################
>>> # Lets perform some operations over dict
>>> k = {}
>>> k
{}
>>> id(k)
1551175416064
>>> dir(k)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(k.update)
Help on built-in function update:

update(...) method of builtins.dict instance
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

>>> k
{}
>>> k.update({'A':'Amol','C':'Chetan'})
>>> k
{'A': 'Amol', 'C': 'Chetan'}
>>> k.update({'A':'Amit'})
>>> k
{'A': 'Amit', 'C': 'Chetan'}
>>> id(k)
1551175416064
>>> # id is not changing hence it MUTABLE data type
>>> k
{'A': 'Amit', 'C': 'Chetan'}
>>> # i want to add manual data
>>> # dict[key]=value
>>> k['D'] = 'Deepak'
>>> k
{'A': 'Amit', 'C': 'Chetan', 'D': 'Deepak'}
>>> k['C'] = 'Chintamani'
>>> k
{'A': 'Amit', 'C': 'Chintamani', 'D': 'Deepak'}
>>> k['C'] = ['Chintamani','Chetak']
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chetak'], 'D': 'Deepak'}
>>> # it accepts homo./hetro data
>>> k['D'] = ['Deepak',700]
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chetak'], 'D': ['Deepak', 700]}
>>> #########################
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> # How to access the values from dict
>>> # using method get
>>> d.get(1)
10
>>> d.get(3)
30
>>> d.get(30)
>>> help(d.get)
Help on built-in function get:

get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.

>>> # if key is present , return its value
>>> # if key is not present then return None
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> d.get(2)
20
>>> d.get(20,'Not present')# key 20 is not present
'Not present'
>>> d.get(100,-1)
-1
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> # mannual way
>>> #d[key]
>>> d[2]
20
>>> d[4]
40
>>> d[34]
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    d[34]
KeyError: 34
>>> ######################
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chetak'], 'D': ['Deepak', 700]}
>>> k['C']
['Chintamani', 'Chetak']
>>> k['C'][0]
'Chintamani'
>>> k['C'][-1]
'Chetak'
>>> k['C'][-1] = 'Chinta'
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chinta'], 'D': ['Deepak', 700]}
>>> k['C'][0]
'Chintamani'
>>> k['C'][0].upper()
'CHINTAMANI'
>>> # Amit(identifier) ---- 'Amit'(string/object)
>>> Amit = 'Amit'
>>> {1:Amit}
{1: 'Amit'}
>>> 

*********************************DAY 11**************************************


Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Dict methods
>>> # {key:value}
>>> # Sequence order is preseved
>>> d = {1:100,'A':'ABC',0:200}
>>> d
{1: 100, 'A': 'ABC', 0: 200}
>>> # accepts homo./hetro data
>>> # dir(d)
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> # suppose if we want to fecth keys of dict
>>> d
{1: 100, 'A': 'ABC', 0: 200}
>>> d.keys()
dict_keys([1, 'A', 0])
>>> # suppose if we want to fecth values of dict
>>> d.values()
dict_values([100, 'ABC', 200])
>>> ## suppose if we want to fecth key,value pair of dict as a tuple
>>> d.items()
dict_items([(1, 100), ('A', 'ABC'), (0, 200)])
>>> #################
>>> # Lets try to remove elements/pairs
>>> d
{1: 100, 'A': 'ABC', 0: 200}
>>> d.pop(1)
100
>>> d
{'A': 'ABC', 0: 200}
>>> d.pop(1) # already key 1 and its value removed
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.pop(1) # already key 1 and its value removed
KeyError: 1
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> # pop(key) needs a key--> return value
>>> #############
>>> d
{'A': 'ABC', 0: 200}
>>> help(d.popitem)
Help on built-in function popitem:

popitem(...) method of builtins.dict instance
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.

>>> d.popitem()
(0, 200)
>>> d
{'A': 'ABC'}
>>> d.popitem()
('A', 'ABC')
>>> d
{}
>>> d.popitem()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> ##################
>>> #fromkeys
>>> help(dict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> t = ['supriya','rakesh','umesh','shital']
>>> t
['supriya', 'rakesh', 'umesh', 'shital']
>>> dict.fromkeys(t)
{'supriya': None, 'rakesh': None, 'umesh': None, 'shital': None}
>>> dict.fromkeys(t,100)
{'supriya': 100, 'rakesh': 100, 'umesh': 100, 'shital': 100}
>>> h = [10,20,30,40]
>>> dict.fromkeys(h)
{10: None, 20: None, 30: None, 40: None}
>>> dict.fromkeys(h,'value')
{10: 'value', 20: 'value', 30: 'value', 40: 'value'}
>>> dict.fromkeys(h,[1,2,3])
{10: [1, 2, 3], 20: [1, 2, 3], 30: [1, 2, 3], 40: [1, 2, 3]}
>>> #####################
>>> # Interview question
>>> t = [(1,20),(2,40),(3,300)]
>>> t
[(1, 20), (2, 40), (3, 300)]
>>> dict(t)
{1: 20, 2: 40, 3: 300}
>>> ############
>>> a1 = ['A','B','C']
>>> a1
['A', 'B', 'C']
>>> b1 = [10,20,30]
>>> # create a dict in a such way: elements of a1 should be key and elements of b1 should be value
>>> dict(a1:b1)
SyntaxError: invalid syntax
>>> dict.fromkeys(a1,b1)
{'A': [10, 20, 30], 'B': [10, 20, 30], 'C': [10, 20, 30]}
>>> help(zip)
Help on class zip in module builtins:

class zip(object)
 |  zip(iter1 [,iter2 [...]]) --> zip object
 |  
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> a1
['A', 'B', 'C']
>>> b1
[10, 20, 30]
>>> zip(a1,b1)
<zip object at 0x000001A3D5855148>
>>> list(zip(a1,b1))
[('A', 10), ('B', 20), ('C', 30)]
>>> dict(zip(a1,b1))
{'A': 10, 'B': 20, 'C': 30}
>>> # if we have extra element in iterable
>>> a1
['A', 'B', 'C']
>>> c1 = [4,5,6,7]
>>> dict(zip(a1,c1))
{'A': 4, 'B': 5, 'C': 6}
>>> dict(zip(c1,a1))
{4: 'A', 5: 'B', 6: 'C'}
>>> ############
>>> help(d.setdefault)
Help on built-in function setdefault:

setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> a = {4: 'A', 5: 'B', 6: 'C'}
>>> a
{4: 'A', 5: 'B', 6: 'C'}
>>> a.setdefault(4)
'A'
>>> a.setdefault(44)
>>> a
{4: 'A', 5: 'B', 6: 'C', 44: None}
>>> a.setdefault('python',1989)
1989
>>> a
{4: 'A', 5: 'B', 6: 'C', 44: None, 'python': 1989}
>>> a.setdefault('python')
1989
>>> 

********************************DAY 12*******************************

"""
Flow control blocks:
1. Selective/conditional statements: purpose is to run the code
on the basis of a condition

if <condition> # used to test only one condition
here if is a keyword

if else # used to test 2 conditions
if elif else # used to test 3 condition
if elif elif elif....else [elif ladder]
# can test multiple conditions

if hp
    if 8gb
    else 6gb
else
# Nested if: can test dependent conditions
-----------------------------
if is condition based
elif is condition based
else is optional and condition less
we use else to test default/last condition
-----------------------------------
Examples:
=============================
# if <condition>:
# when condition is True, then only ur control will
# enter inside the block
# else it wont[if condition is False]
num = 2
# checking number is +ve or nt
if num > 0:
    print('Good evening')
==================================
# check number is even or odd
num = 27
if num %2 == 0:
    print(num, 'is even')
else:
    print(num,'is odd')
================================
# Test student percentage and assign a class to the student
per = float(input('Enter your percentage:'))
if per >= 75:
    print('You got Distinction')
elif per >= 65:
    print('You got First class')
elif per >= 55:
    print('You got Second class')
elif per >= 45:
    print('You got Pass class')
else:
    print('Sorry you are Fail..')
=================================================
# Q. find out largest number among 3
num1 = 125
num2 = 450
num3 = 10

if (num1 > num2) and (num1 > num3):
    print(num1,'is greater than',num2,'and',num3)
elif num2 > num3:
    print(num2, 'is greater than', num1, 'and', num3)
else:
    print(num3, 'is greater than', num1, 'and', num2)
================================================
# Nested if
# if outer condition is True then inner
# if condition will get checked
mobile = 'samsung'
ram = '1 gb'
if mobile == 'realme':
    if ram == '8 gb':
        print('Price is:Rs.',12000)
    elif ram == '6 gb':
        print('Price is:Rs.', 10500)
    else:
        print('Price is:Rs.', 9000)
else:
    print('Sorry we only sell Realme mobiles ')
===================================================

2. Iterative statements
3. Transfer statements
"""
if 2 == 2:
    pass



**************************DAY12-1**********************************

"""
Numeric: int, float, complex
Boolean: True, False
String
List
Tuple
Set
Dict
=============================================
Frozen set: Immutable set
==================================
s = frozenset([10,20,30,40])
print(s)
print(dir(s))
# after looking at the output
# it tells us, frozenset does not contain mutable methods.
# example: pop, update,add,discard, remove etc
# Q. Differentiate Set and frozenset?
# Q. when to use set and frozenset??
===============================================
Range: is used to generate sequential numbers
Default range starts from 0
range is a data type
range is a function
Different patterns of range():
range(n/stop)=> stop is exclusive:stop will nt be added in the output
----------------------
print(list(range(16)))
# it will generate 0 - 15 , 16 will nt be in the output
-------------------------------------------
# range(start,stop)
print(list(range(16,21)))
# start is 16 and stop at 21
--------------------------------------------
# range(start,stop,step)
print(list(range(16,21,2)))
---------------------------
# Can we do -ve stepping
# yes
print(list(range(21,16,-1)))
----------------------------
# Q. Generate 1-100 numbers
print(list(range(1,101)))

generate 1-100 een numbers
print(list(range(2,101,2)))

generate 1-100 odd numbers
print(list(range(1,101,2)))
==========================================
bytes(): it is used to generate byte sequence for given list of int
it has a range: 0-256
===========================
k = [12,4,60]
print(bytes(k))
========================================
k = [12,4,60]
bt = bytes(k)
print(bt[-1])
#is it mutable?
# bt[-1] = 30
# in case of bytes direct assignment of value is nt possible
print(dir(bt))
# as it does nt contain any mutable method hence bytes is immutable
=======================================
bytearray(): it is same as that of bytes
but bytearray is Mutable in nature
----------------------------------------
k = [12,4,60]
bt = bytearray(k)
print(bt)
print(bt[-1])
bt[-1] = 30
print(bt)
print(bt[-1])
#-----------------
print(dir(bt))
# as it contains methods those support mutable operations, and changes
# persist in the same object
# hence its mutable
=========================================
None: its a keyword
Nothing, null, empty stub
--------------------------------
k = [1,None, None, 10]
print(k)
print(k[1])
========================================
NUMBER SYSTEM
TYPE CONVERSION/TYPECASTING
========================
NUMBER SYSTEM:
Binary [0,1]
Octal [0-7]
Decimal [0-9] #default
Hexadecimal [0-9A-F]
================================
num = 100
# binary
print('Decimal to binary:',bin(num)) # 0b1100100
print('Binary to Decimal:',0b1100100)
# Octal
print(oct(num)) # 0o144
print(0O144)
# Hex
print(hex(num)) # 0x64
print(0x64)
print('--------------------')
# hex to binary
print(bin(0x64))
===========================================
TYPECASTING:
1. Implicit: typecasting performed by python itself
Example:
print(10/5)
print('10'+'20')
print(0b1111)
print(4.5 + 1+5j)
--------------------------------
2. Explicit: typecasting performed by user
print(int(10/5))
print(int('10')+int('20'))
print(hex(0b1111))
print(str(4.5 + 1))
------------------
Assignment:
s = '190'
int
float
complex
bool
list
tuple
set
bytes
bytearray
bin
oct
hex
"""

*******************************DAY 13**********************************************

"""
2. Iterative statements: used for performing iterations
Iteration means we use iterable(str,list,tuple,set,dict,range)
and from that iterable we fetch each element one by one

It contains 2 types
- for loop
syntax:
for(keyword) var(identifier) in(operator) sequence/iterable:
    print(var)
------------------------------------
Example
----------------------------
# input as list
nm = ['Ramesh','Mahesh','Suresh','Dinesh']
# default for loop read from left to right
for n in nm:
    print(n)
--------------------------------
# string
s = 'good evening Nilesh'
for char in s:
    print(char, end='')
-------------------------------------
# string: need to print only words
s = 'good evening Nilesh'
print(s.split())
for word in s.split():
    print(word)
==================================
# string: need to print words ending with 'h'
s = 'good evening Nilesh Umesh'
print(s.split())
for word in s.split():
    #print(word)
    if word.endswith('h'):
        print(word)
-----------------------------------
# string: need to print only numbers into another list
s = 'good evening Nilesh 9834373453 Umesh 34534523 '
print(s.split())
n = []
for word in s.split():
    #print(word)
    if word.isdigit():
        #print(word)
        n.append(word)
print(n)
-----------------------------------
s = {10,20,10,40,10,50}
for i in s:
    print(i)
    # set does not preserve sequence order
---------------------------
#dict
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d:
    print(i)
    # default it fetches only keys
----------------------------------
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d:
    # i is key
    #b = i, d.get(i)
    #print(b)
    print(i, d.get(i))
===================================
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d.items():
    print(i)
===============================
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d.values():
    print(i)
===============================
# range function
for i in range(5):
    #print(i)
    print('Kuldip')
===============================
# range function
for i in range(5,16):
    print(i)
-------------------------
# range function
for i in range(16,4,-1):
    print(i)
---------------------------
- while loop
"""

***************************DAY 14*********************************************


11:01 PM 03/06/2022"""
# q. Reverse the words:Bachchan Amitabh
s = 'Amitabh Bachchan'
for i in s.split()[::-1]:
    print(i,end=' ')
=======================
# q. Reverse the character/blocks
s = 'Amitabh Bachchan'
# print(s[::-1])
print(reversed(s))
# whenever u get output in the form of object
# in order to get values from it
# u have 2 options:1. iterate over it 2. typecast
#print(tuple(reversed(s)))
final = ''
for i in reversed(s):
    final+=i #it will concatenate one block at a time
print(final)
===============================
# q. Reverse the character/blocks
s = 'Amitabh Bachchan'
print(s[-3])
#-1 to -n
for i in range(-1,-(len(s)+1),-1):
    #print(i,end=' ')
    print(s[i],end='')
==============================
# q. Reverse the character of individual word
s = 'Amitabh Bachchan'
for i in s.split():
    print(i[::-1],end=' ')
==============================
# q. i want to fetch vowels from the string: a,i,o,u,e
s = 'Amitabh Bachchan'
vowels = ['a','i','e','o','u','A','I','O','U','E']
for i in s:
    if i in vowels:
        print(i,end=' ')
===================================
# Interview q. i want a dict of each block and its count
#  {'A':1,'m':1,'i':1,'t':1,'a':3.....}
s = 'Amitabh Bachchan'
d = {}
for i in s:
    #print(i,s.count(i))
    # d[key] = value
    d[i] = s.count(i)
print(d)
"""
# Interview q. interchange 1st and last 2 chacters from string
# Expected: 'hantabh BachcAmi'
s = 'Amitabh Bachchan'
***************program*************
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
for i in s :
    if(len(s) > 2):
     pass
print(s[-3:17]+s[3:-3]+s[0:3])
*************output:****************
Amitabh Bachchan
hantabh BachcAmi

#################################
# Print the +ve and -ve index of each block
# example: A is present at 0,-16
*************program******************
s = 'Amitabh Bachchan'
print('Amitabh Bachchan')
length_s = len(s)
for start_latter, poitive_index in zip(s, range(length_s)):
     if start_latter == None:
         pass
     print(start_latter, poitive_index, -length_s)
     length_s = length_s-1

#################################
# my key  =3
# means i want to shift characters by 3
# input  s = 'Amitabh Bachchan'
# Expected: 'Dplw....
###############################
s = str(input('enter the string= '))
# print('Amitabh Bachchan')
for i in s:
   shifting_char = chr(ord(i)+3)
   print(shifting_char,end='')


*****************************DAY 15**********************************

"""
Iterative statements/Conditional:
1. for loop
# Patterns: *,number, Alphabate
-----------------------------------------
*
**
***
****
*****
---------------------
for i in range(1,6):
    print(i*'*')
---------------------------
for i in range(1,6): #row
    for j in range(i): # column
        print(j*'*',end='')
    print()
--------------------------
for i in range(1,6): #row
    for j in range(1,i+1): # column
        print(j, end='')
    print()
===========================
for i in range(1,6): #row
    for j in range(1,i+1): # column
        print(i, end='')
    print()
====================\
55555
4444
333
22
1
==============================
for i in range(5,0,-1): #row
    for j in range(1,i+1): # column
        print(i, end='')
    print()
======================
for i in range(5,0,-1): #row
    for j in range(1,i+1): # column
        print(j, end='')
    print()
=====================
12345
1234
123
12
1
====================
for i in range(5,0,-1): #row
    for j in range(i,0,-1): # column
        print(j, end='')
    print()

for i in range(5,0,-1):
    print(i,end=' ')
================================

# Amulyas academy
==============================
# alphabates
========================
for i in range(1,6):
    print(chr(i+64)*i)
------------------
A
BB
CCC
DDDD
EEEEE
=====================
for i in range(1,6):
    print(chr(70-i)*i)
-----------------------
E
DD
CCC
BBBB
AAAAA
==========================
AAAAA
BBBB
CCC
DD
E
=====================\
for i in range(5,0,-1):
    print(i*chr(70-i))
===================
for i in range(1,6):
    print(chr(i+64)*(6-i))
-------------------------------------
2. While loop:
conditionally infinite loop
Hence we need some external factors to stop the contineous
iteration
Syntax:
while <condition>:
    statements
    .
    .
-----------------------
num = 1
while num == 1:
    print('hello')
    num = 2
--------------------------
# Write a program to print 1,10 natural numbers using while loop

num = 1
while num < 11:
    print(num)
    num += 1
=========================
# WAP to print 1,10 even numbers
num = 1
while num < 11:
    print(num+1)
    num += 2
=========================
# WAP to Print python 5 times
st = 'python'
count = 1
while count <=5 :
    print(st)
    count += 1
==============================
Q. What is difference between for and while???
while is condition based, for is not
in while we control of iteration,in for it read all objects in container
"""















































