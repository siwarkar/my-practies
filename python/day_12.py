Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Dict
>>> # Dictionary
>>> # key:value/values
>>> # Dict is a data structure with key:value pair
>>> #{key1:value1,key2:value2}
>>> # Syntax:
>>> # empty dict
>>> {}
{}
>>> type({})
<class 'dict'>
>>> dict()
{}
>>> d = {1:100,2:200,3:300}
>>> d
{1: 100, 2: 200, 3: 300}
>>> # how many pairs we have??
>>> len(d)
3
>>> # Features of Dict
>>> # Supports Homo./Hetro values
>>> {1:10,2:20}
{1: 10, 2: 20}
>>> {'name':'Akash','place':'Satara'}
{'name': 'Akash', 'place': 'Satara'}
>>> #hetro
>>> {1:100,'a':'Amit',30:33.33}
{1: 100, 'a': 'Amit', 30: 33.33}
>>> #--------
>>> # Key acts as an index
>>> d
{1: 100, 2: 200, 3: 300}
>>> # with the help of key we can access values
>>> d[1]
100
>>> d[2]
200
>>> # can we use a -ve index??
>>> d[-1]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d[-1]
KeyError: -1
>>> # no negative indexing is supported
>>> # bcz Its background data structure is not an Array
>>> # no indexing + no slicing
>>> d
{1: 100, 2: 200, 3: 300}
>>> d[:]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d[:]
TypeError: unhashable type: 'slice'
>>> d[::-1]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d[::-1]
TypeError: unhashable type: 'slice'
>>> #---------------
>>> # we can use multiple keys
>>> # but duplicate keys not allowed
>>> {1:100,2:200,1:400,1:500}
{1: 500, 2: 200}
>>> # it takes last recent pair associated with a perticular key
>>> # why duplictas are not allowed??
>>> # bcz background datastructure is HASH TABLE
>>> #---------------
>>> # for a single we can store multiple values
>>> # for a single key we can store multiple values
>>> {1:[10,20,30,40],2:('A','B')}
{1: [10, 20, 30, 40], 2: ('A', 'B')}
>>> #-----------------
>>> # # duplicate values allowed
>>> {1:100,2:100,3:100}
{1: 100, 2: 100, 3: 100}
>>> #--------------------
>>> # It preseves sequence order
>>> #-------------------
>>> # Methods of a dict
>>> d
{1: 100, 2: 200, 3: 300}
>>> # Its a mutable data structure
>>> id(d)
2593319502184
>>> # lets Access the values
>>> # using key as a index
>>> d[2]
200
>>> d[3]
300
>>> d[4] # index is nt present
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d[4] # index is nt present
KeyError: 4
>>> # 2nd approach is
>>> # using get method
>>> d
{1: 100, 2: 200, 3: 300}
>>> d.get(1)
100
>>> d.get(4)
>>> None
>>> # if key is nt present is dict then get method returns None
>>> # otherwise it fetch value
>>> #-----------------
>>> # Change the dict/Update
>>> d.update({2:'Python'})
>>> d
{1: 100, 2: 'Python', 3: 300}
>>> #lets add new pairs
>>> d.update({'j':'Java'})
>>> d
{1: 100, 2: 'Python', 3: 300, 'j': 'Java'}
>>> # ---------------------
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> # clear
>>> # remove all pairs
>>> d
{1: 100, 2: 'Python', 3: 300, 'j': 'Java'}
>>> d.clear()
>>> d
{}
>>> id(d)
2593319502184
>>> # id remains same ,changes persist in the same object
>>> # hence dict is MUTABLE
>>> #--------------
>>> d = {1: 100, 2: 'Python', 3: 300, 'j': 'Java'}
>>> d
{1: 100, 2: 'Python', 3: 300, 'j': 'Java'}
>>> # using clear it removes all pairs
>>> # but if we want to remove some pairs
>>> # use pop() and popitem()
>>> help(d.pop)
Help on built-in function pop:

pop(...) method of builtins.dict instance
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised

>>> d
{1: 100, 2: 'Python', 3: 300, 'j': 'Java'}
>>> d.pop('j')
'Java'
>>> d
{1: 100, 2: 'Python', 3: 300}
>>> # if key is not found
>>> d.pop('z')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    d.pop('z')
KeyError: 'z'
>>> #----------
>>> help(d.popitem)
Help on built-in function popitem:

popitem(...) method of builtins.dict instance
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.

>>> d
{1: 100, 2: 'Python', 3: 300}
>>> d.popitem()
(3, 300)
>>> d
{1: 100, 2: 'Python'}
>>> # Q. explain pop and popitem
>>> # Q. difference between them?
>>> # Q. similarity in them>
>>> # Q. differentiate pop in list,set,dict
>>> #-----------------------
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> # access perticular things
>>> # keys
>>> d
{1: 100, 2: 'Python'}
>>> d.keys()
dict_keys([1, 2])
>>> #values
>>> d.values()
dict_values([100, 'Python'])
>>> # both: (key value)
>>> # items
>>> d.items()
dict_items([(1, 100), (2, 'Python')])
>>> #--------------
>>> help(d.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> dict.fromkeys(['A','B','C'])
{'A': None, 'B': None, 'C': None}
>>> dict.fromkeys([4,5,6,7]))
SyntaxError: invalid syntax
>>> dict.fromkeys([4,5,6,7])
{4: None, 5: None, 6: None, 7: None}
>>> # instead of None some other values we want to set
>>> dict.fromkeys([1,2,3],10)
{1: 10, 2: 10, 3: 10}
>>> dict.fromkeys('abc')
{'a': None, 'b': None, 'c': None}
>>> dict.fromkeys(['abc'])
{'abc': None}
>>> dict.fromkeys('123')
{'1': None, '2': None, '3': None}
>>> #-------------
>>> t1 = (1,2,3,4)
>>> t2 = (10,20,30,40)
>>> {1:10,2:20,3:30,4:40}
{1: 10, 2: 20, 3: 30, 4: 40}
>>> # SETDEFAULT
>>> 
