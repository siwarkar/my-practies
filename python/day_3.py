Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # OPERATORS
>>> # Logical operators
>>> True and True
True
>>> 10 and 12
12
>>> 0 and 30
0
>>> # Rule : if we are using x(10) and y(12) , in this if x is True then return y
>>> # False, 0, None, '' all these are nothing but False
>>> # Except these 4, everything is True in Python
>>> 100 and 78
78
>>> 3 and 6
6
>>> 'python' and 'java'
'java'
>>> # if x is False then return x
>>> '' and 7
''
>>> False and 'python'
False
>>> 0 and 100
0
>>> None and 45
>>> None
>>> ####################
>>> 'python' and 23
23
>>> ###################
>>> 12 or False
12
>>> 12 or 30
12
>>> #  Rule: if x is True then return x
>>> 0 or 34
34
>>> # if x false then return y
>>> ########################
>>> 10 and 34
34
>>> 23 or 0
23
>>> 0 and 'py'
0
>>> #######################
>>> 0 or False
False
>>> False
False
>>> bool(0)
False
>>> bool('')
False
>>> bool(None)
False
>>> 0 and False
0
>>> # take -ve values
>>> -10 and -34
-34
>>> bool(-34)
True
>>> bool(-10)
True
>>> ####
>>> ###################
>>> # Membership operator
>>> # in(check is it present in sequence), not in(check its not present)
>>> # These are used for checking purpose
>>> # it will check, either submemebr is part of main collection or not???
>>> s = 'dil to pagal hai'
>>> s
'dil to pagal hai'
>>> 'dil' in s
True
>>> # if substring/sub element is present in sequence so it will return boolean output thats True
>>> # otherwise False
>>> 'Dil' in s
False
>>> # membership operators are best to finding elements in collection
>>> 'p' in s
True
>>> c = [10,20,300,450,600,220]
>>> c
[10, 20, 300, 450, 600, 220]
>>> 20 in c
True
>>> 333 in c
False
>>> # one element only we can check at a time
>>> # not in
>>> c
[10, 20, 300, 450, 600, 220]
>>> 340 not in c
True
>>> s
'dil to pagal hai'
>>> 'KGF' not in s
True
>>> 'pagal' not in s
False
>>> #######################
>>> # Identity operator
>>> # it check id of an object: id means it address
>>> # if id of 2 objects are same then it will return True
>>> # 2 options: is, is not
>>> ##
>>> 10 is 10
True
>>> x = 200
>>> y = 200
>>> x is y
True
>>> id(x)
140729284619520
>>> id(y)
140729284619520
>>> p = 'python'
>>> q = 'Python'
>>> p is q
False
>>> id(p)
2863980288856
>>> id(q)
2863941375512
>>> r = 'python'
>>> p is q
False
>>> p is r
True
>>> id(p)
2863980288856
>>> id(r)
2863980288856
>>> # is
>>> p is r
True
>>> p is not r
False
>>> p is not q
True
>>> id(p)
2863980288856
>>> id(q)
2863941375512
>>> # if id's are same u will get True
>>> # if  id's are different u will get False
>>> ####################
>>> # Data structure
>>> # in python we have 14 DS
>>> # Number: int, float , complex
>>> # boolean: True, False
>>> # String
>>> # List
>>> # Tuple
>>> # set
>>> # dict
>>> # frozenset
>>> # bytes
>>> # bytearray
>>> # range
>>> # None
>>> # for data science we need 7 Ds
>>> #######################
>>> # Number
>>> # int: base 10 value ==> [0-9]
>>> 10
10
>>> 90
90
>>> 23
23
>>> type(10)
<class 'int'>
>>> type(23)
<class 'int'>
>>> # float: floating point number
>>> # 12(floor).5(ceil)
>>> 15.6
15.6
>>> type(15.6)
<class 'float'>
>>> # complex:(real+img)
>>> # 3(real)+4j(img)
>>> 4+5j
(4+5j)
>>> type(4+5j)
<class 'complex'>
>>> 5j
5j
>>> type(5j)
<class 'complex'>
>>> 4j+5j
9j
>>> ##################
>>> # Boolean
>>> # True False
>>> # True and False are part of DS and these are Keywords as well
>>> True
True
>>> False
False
>>> # when we compare the 2 things or we are checking something in that case
>>> # we need boolean values
>>> 3 > 4
False
>>> # False: False, 0, None, ''
>>> # Except these everything is True
>>> # we can use bool() function to convert any object to its boolean form
>>> bool('py')
True
>>> bool(12)
True
>>> bool([10,20])
True
>>> bool(-11)
True
>>> bool(3+4j)
True
>>> # lets check False
>>> bool(0)
False
>>> bool('')
False
>>> bool(None)
False
>>> bool(False)
False
>>> bool(' ')
True
>>> # as it contains space , so space is one block hence output is True
>>> #################################
>>> # String
>>> # Syntax:
>>> ''
''
>>> ""
''
>>> type('')
<class 'str'>
>>> type("")
<class 'str'>
>>> 'hello good morning'
'hello good morning'
>>> hello good morning'
SyntaxError: invalid syntax
>>> 'hello good morning
SyntaxError: EOL while scanning string literal
>>> ##############
>>> # combinition of '' and ""
>>> # Rule: if outside we have '' then inside use ""
>>> # and viceversa
>>> "It is know as KGF"
'It is know as KGF'
>>> "It is know as 'KGF'"
"It is know as 'KGF'"
>>> "It is know as "KGF""
SyntaxError: invalid syntax
>>> 'It is know as "KGF"'
'It is know as "KGF"'
>>> # if we want '
>>> # this is virat's house
>>> 'this is virat's house'
SyntaxError: invalid syntax
>>> 'this is virat"s house'
'this is virat"s house'
>>> 'this is virat\'s house' # use \ is an escape sequence
"this is virat's house"
>>> "this is virat's house"
"this is virat's house"
>>> ###################
>>> # List
>>> # syntax: []
>>> []
[]
>>> type([])
<class 'list'>
>>> # create an empty list
>>> a = []
>>> a
[]
>>> type(a)
<class 'list'>
>>> b = list()
>>> b
[]
>>> type(b)
<class 'list'>
>>> # list can contain elements
>>> [1,2,3,4]# elements will be separated by comma,
[1, 2, 3, 4]
>>> ['A','B','C]
     
SyntaxError: EOL while scanning string literal
>>> ['A','B','C']
     
['A', 'B', 'C']
>>> list()
     
[]
>>> list((10,20,30))
     
[10, 20, 30]
>>> 
