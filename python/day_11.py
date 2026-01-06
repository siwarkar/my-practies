Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # SET
>>> # Syntax:
>>> set()
set()
>>> {}
{}
>>> # empty curly bracket is nt a set
>>> # its dict
>>> type({})
<class 'dict'>
>>> type(set())
<class 'set'>
>>> # using brackets if u want to create an empty set
>>> {()}
{()}
>>> type({()})
<class 'set'>
>>> #---------------------
>>> # Features of Set
>>> # It doesnt preserve sequence order
>>> # comma separated values are nothing but set
>>> # these values u must have to put inside {}
>>> {1,20,9,0,45}
{0, 1, 9, 45, 20}
>>> #------------
>>> # Duplicates are nt allowed
>>> {1,2,3,1,1,1,1,1,1}
{1, 2, 3}
>>> {'A','B','A','B','A','A']
SyntaxError: invalid syntax
>>> {'A','B','A','B','A','A'}
{'B', 'A'}
>>> #----------------
>>> # Does not support indexing
>>> s = {10,20,30,40}
>>> s
{40, 10, 20, 30}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> #----------
>>> # slicing is not supported
>>> s
{40, 10, 20, 30}
>>> s[::-1]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[::-1]
TypeError: 'set' object is not subscriptable
>>> # hence Set has different data structure than array
>>> # Background data structure of a set is Hash Table
>>> # bcz of hash table it does not allowes duplicates and nt preserving sequence order
>>> # example
>>> {1,20,9,0,45}
{0, 1, 9, 45, 20}
>>> #-------------------
>>> # Homo./Hetro. values supported
>>> {1,2,3}
{1, 2, 3}
>>> {1,'A','B',23}
{1, 'A', 23, 'B'}
>>> #---------------------
>>> #check different methods of set
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s
{40, 10, 20, 30}
>>> help(s.add)
Help on built-in function add:

add(...) method of builtins.set instance
    Add an element to a set.
    
    This has no effect if the element is already present.

>>> s.add(100)
>>> s
{100, 40, 10, 20, 30}
>>> # now 100 is already added
>>> # if we try to add again. no effect
>>> s.add(100)
>>> s
{100, 40, 10, 20, 30}
>>> # can we supply multiple values
>>> s.add(1,2)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s.add(1,2)
TypeError: add() takes exactly one argument (2 given)
>>> s.add((1,2))
>>> s
{(1, 2), 100, 40, 10, 20, 30}
>>> s.add({'A','B'})
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.add({'A','B'})
TypeError: unhashable type: 'set'
>>> s.add(['A','B'])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s.add(['A','B'])
TypeError: unhashable type: 'list'
>>> s.add('Python')
>>> s
{(1, 2), 100, 40, 10, 'Python', 20, 30}
>>> ########################
>>> s
{(1, 2), 100, 40, 10, 'Python', 20, 30}
>>> id(s)
2576628586760
>>> # clear()
>>> s.clear()
>>> s
set()
>>> id(s)
2576628586760
>>> # After performing changes id is not changing
>>> # changes persist in the same object directly
>>> #hence SET IS MUTABLE
>>> #####################
>>> # Check copy() method
>>> # copy() gives u a shallow copy
>>> # id will be different
>>> #--------------------
>>> # union: Combine 2 sets/all elements from 2 sets
>>> s1 = {1,2,3,4}
>>> s2 = {1,2,4,5,6}
>>> s1
{1, 2, 3, 4}
s
>>> 2
2
>>> s2
{1, 2, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> #---------
>>> # intersection: common elements from 2 sets
>>> s1.intersection(s2)
{1, 2, 4}
>>> #-----------
>>> # difference: Uncommon elements from set 1/Except common elements froms et 1
>>> s1.difference(s2)
{3}
>>> se
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    se
NameError: name 'se' is not defined
>>> s1
{1, 2, 3, 4}
>>> s2
{1, 2, 4, 5, 6}
>>> s2.difference(s1)
{5, 6}
>>> # if we want uncommon from both the sets
>>> # then use symmetric_difference
>>> s1.symmetric_difference(s2)
{3, 5, 6}
>>> # all above operations means union, intersection, difference, symmetric_diff are temp.
>>> s1
{1, 2, 3, 4}
>>> s2
{1, 2, 4, 5, 6}
>>> # if u want to store the result in first set then use update options
>>> dir(s1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> # use update()
>>> s1
{1, 2, 3, 4}
>>> s2
{1, 2, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> # its temp
>>> # union output to be stored in any one of the set then use update()
>>> s1.update(s2)
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s2
{1, 2, 4, 5, 6}
>>> # Remove elements from Set
>>> # 3 methods present
>>> # pop discard remove
>>> help(s2.pop)
Help on built-in function pop:

pop(...) method of builtins.set instance
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> s1
{1, 2, 3, 4, 5, 6}
>>> s1.pop()
1
>>> s1
{2, 3, 4, 5, 6}
>>> # difference between pop of list and set
>>> # discard
>>> help(s1.discard)
Help on built-in function discard:

discard(...) method of builtins.set instance
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.

>>> s1
{2, 3, 4, 5, 6}
>>> s1.discard(5)
>>> s1
{2, 3, 4, 6}
>>> s1.discard(5) # 5 already removed
>>> #----------------
>>> # remove()
>>> help(s1.remove)
Help on built-in function remove:

remove(...) method of builtins.set instance
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.

>>> s1
{2, 3, 4, 6}
>>> s1.remove(6)
>>> s1
{2, 3, 4}
>>> # now 6 is removed
>>> # try ones again to remove 6
>>> s1
{2, 3, 4}
>>> s1.remove(6)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    s1.remove(6)
KeyError: 6
>>> # Q. Differentiate pop, discard and remove??
>>> #-----------------
>>> dir(s1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> # is methods
>>> s1
{2, 3, 4}
>>> s2 = {1,2,3,4,5}
>>> help(s1.isdisjoint)
Help on built-in function isdisjoint:

isdisjoint(...) method of builtins.set instance
    Return True if two sets have a null intersection.

>>> s3 = {10,20}
>>> s3
{10, 20}
>>> s1
{2, 3, 4}
>>> # in both sets we dont have common elements
>>> s1.isdisjoint(s3)
True
>>> # issubset
>>> s1.issubset(s2)
True
>>> s1
{2, 3, 4}
>>> s2
{1, 2, 3, 4, 5}
>>> # issuperset
>>> s2.issuperset(s1)
True
>>> 
