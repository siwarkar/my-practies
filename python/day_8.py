Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Unicode
>>> # are codes given to each charcater/symbol
>>> # Syntax: '\ucode'
>>> '\u00D3'
'Ó'
>>> '\u00A9'
'©'
>>> '\u00A9 Copyright Gooogle.com inc'
'© Copyright Gooogle.com inc'
>>> '\u00A9 Copyright 2022'
'© Copyright 2022'
>>> '\u2126'
'Ω'
>>> '\u090A'
'ऊ'
>>> '\u1F600'
'ὠ0'
>>> '\u1F571'
'ὗ1'
>>> '\u090A \u090B'
'ऊ ऋ'
>>> #########################
>>> # List
>>> # Syntax: []
>>> []
[]
>>> list()
[]
>>> # Features of a list
>>> # List is a collection of element separated by comma
>>> # Example
>>> [1,2,3]
[1, 2, 3]
>>> # List accepts homo./Hetro. values
>>> [10,20,30] # homo.
[10, 20, 30]
>>> [1,'A',34.44] #hetro.
[1, 'A', 34.44]
>>> #----------
>>> # List background data structure is an Array
>>> # array is sequential storage of given values
>>> k = [10,20,30,40,50]
>>> k
[10, 20, 30, 40, 50]
>>> #-----------
>>> # it supports indexing
>>> # +ve and -ve indexing
>>> # Example
>>> k
[10, 20, 30, 40, 50]
>>> # +ve index
>>> k[3]
40
>>> k[0]
10
>>> k[4]
50
>>> # -ve index
>>> k[-1]
50
>>> k[-3]
30
>>> k[-5]
10
>>> # if we use index beyond its range
>>> k
[10, 20, 30, 40, 50]
>>> k[-10] # we dont have element at this index
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    k[-10] # we dont have element at this index
IndexError: list index out of range
>>> k[100]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    k[100]
IndexError: list index out of range
>>> #-----------------
>>> # slicing is also supported
>>> k
[10, 20, 30, 40, 50]
>>> k[:2]
[10, 20]
>>> k[2:]
[30, 40, 50]
>>> k[-2:]
[40, 50]
>>> k[::-1]
[50, 40, 30, 20, 10]
>>> k[-2::-1]
[40, 30, 20, 10]
>>> #------------------------
>>> # It preservs sequence order
>>> # in same order will get the values/objects
>>> #-------------------------
>>> # Duplicates are allowed
>>> j = [1,2,12,1,1,1,3,41,1,1]
>>> j
[1, 2, 12, 1, 1, 1, 3, 41, 1, 1]
>>> #--------------------------
>>> # List is Mutable
>>> # Mutable means: we can change the values of the same object
>>> # but when change occurs, it gets preserved in the same object
>>> # there is no need to create a new object
>>> # simply we can say: changes persist in same object
>>> # its flexible for change
>>> # Example
>>> k
[10, 20, 30, 40, 50]
>>> #access 40
>>> k[3]
40
>>> # now check id of k
>>> id(k)
2401200363400
>>> k
[10, 20, 30, 40, 50]
>>> # lets change 40 to 400 using indexing
>>> k[3]
40
>>> k[3] = 400
>>> k
[10, 20, 30, 400, 50]
>>> # now after change check id
>>> id(k)
2401200363400
>>> # id is not changed
>>> # id remains same
>>> # exmaple 2
>>> k
[10, 20, 30, 400, 50]
>>> # add 'python' in k
>>> k.append('python')
>>> k
[10, 20, 30, 400, 50, 'python']
>>> #now check id of k
>>> id(k)
2401200363400
>>> # still id remains same
>>> # When we are performing changes in a list, and changes persist in same object
>>> #hence it is known as MUTABLE DATA TYPE
>>> #-----------------------
>>> # in data type , we have 2 categories
>>> # Mutable data type
>>> # Immutable data type
>>> # Mutable data type: changes persist in same object
>>> # Immutable data type: changes doesnt persist in same object, changes are temp.
>>> #-------------------------
>>> #check methods of list
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> f
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> j
[1, 2, 12, 1, 1, 1, 3, 41, 1, 1]
>>> j.index(1)
0
>>> # to find out index of each element use enumerate
>>> enumerate(j)
<enumerate object at 0x0000022F12B0F828>
>>> # from this object in order to retrieve value
>>> # we need to typecast it
>>> list(enumerate(j))
[(0, 1), (1, 2), (2, 12), (3, 1), (4, 1), (5, 1), (6, 3), (7, 41), (8, 1), (9, 1)]
>>> j[7]
41
>>> list(enumerate('akshay'))
[(0, 'a'), (1, 'k'), (2, 's'), (3, 'h'), (4, 'a'), (5, 'y')]
>>> # --------------------------------
>>> # METHODS OF LIST
>>> dir(k)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # append
>>> k
[10, 20, 30, 400, 50, 'python']
>>> # help() to check info abt any method
>>> help(k.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> k.append(33)
>>> k
[10, 20, 30, 400, 50, 'python', 33]
>>> # append a new list
>>> k.append([1,2])# total list will be added
>>> k
[10, 20, 30, 400, 50, 'python', 33, [1, 2]]
>>> k[-1]
[1, 2]
>>> #-------------
>>> # extend()
>>> help(k.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> k
[10, 20, 30, 400, 50, 'python', 33, [1, 2]]
>>> k.extend([1,2])# it will add 1 and 2 as a separate element
>>> k
[10, 20, 30, 400, 50, 'python', 33, [1, 2], 1, 2]
>>> k.append('AB')
>>> k
[10, 20, 30, 400, 50, 'python', 33, [1, 2], 1, 2, 'AB']
>>> k.extend('AB') # separate A and B
>>> k
[10, 20, 30, 400, 50, 'python', 33, [1, 2], 1, 2, 'AB', 'A', 'B']
>>> # Q. Difference between Append and Extend
>>> []
[]
>>> s = 'PQR'
>>> # add P Q R separately as an element of list
>>> [].extend(s)
>>> h = []
>>> h.extend(s)
>>> h
['P', 'Q', 'R']
>>> k.extend(23)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    k.extend(23)
TypeError: 'int' object is not iterable
>>> h
['P', 'Q', 'R']
>>> h.extend(range(4))
>>> h
['P', 'Q', 'R', 0, 1, 2, 3]
>>> h.append(range(4))
>>> h
['P', 'Q', 'R', 0, 1, 2, 3, range(0, 4)]
>>> #---------------------
>>> # clear()
>>> h
['P', 'Q', 'R', 0, 1, 2, 3, range(0, 4)]
>>> h.clear() # removes all elements from list
>>> h
[]
>>> #---------------------------
>>> 
