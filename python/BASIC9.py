Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List methods
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # copy() method
>>> k = [ 10,20,30,40]
>>> k
[10, 20, 30, 40]
>>> help(k.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> # shallow copy
>>> h = k.copy()
>>> k
[10, 20, 30, 40]
>>> h
[10, 20, 30, 40]
>>> #check id
>>> id(k)
2544911716616
>>> id(h)
2544916568072
>>> # in shallow copy: values will be same in both the lists
>>> # but id's will be different
>>> ##########
>>> # Deep copy
>>> # in deep copy: values will be same in both the list's
>>> # but id's will be same
>>> g = k
>>> k
[10, 20, 30, 40]
>>> g
[10, 20, 30, 40]
>>> #check id now
>>> id(g)
2544911716616
>>> id(k)
2544911716616
>>> # same values with same id
>>> # What is difference between shallow and deep copy
>>> # shallow we have different id, in deep same id
>>> #-----------------
>>> k
[10, 20, 30, 40]
>>> #lets change value in k
>>> k[0] = 100
>>> k
[100, 20, 30, 40]
>>> # now check h:shallow copy used
>>> h
[10, 20, 30, 40]
>>> # there is no change is h
>>> # bcz its address is different
>>> #---------------------
>>> # now lets check g:deep copy
>>> k
[100, 20, 30, 40]
>>> g
[100, 20, 30, 40]
>>> # we performed changes in k but same change reflected in g as well
>>> # rzn: bcz of id: and its same
>>> id(k)
2544911716616
>>> id(g)
2544911716616
>>> #------------------------------------------
>>> ####################################
>>> k
[100, 20, 30, 40]
>>> k.count(20)
1
>>> k.count(450)
0
>>> #-----------------
>>> k.index(100)
0
>>> k.index(40)
3
>>> x = [1,2,3,4,1,1,1,6]
>>> x
[1, 2, 3, 4, 1, 1, 1, 6]
>>> x.index(1)
0
>>> x.index(1,3)
4
>>> 
>>> x.index(1) # lowest index
0
>>> x.index(1,3)
4
>>> x.index(1,1)
4
>>> x.index(1,6)
6
>>> #x.index(1(value),3(from where to start search))
>>> #--------------------------------
>>> help(k.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> k
[100, 20, 30, 40]
>>> # add 'A' between 20 n 30
>>> # before 30
>>> k.insert(2,'A')
>>> k
[100, 20, 'A', 30, 40]
>>> # Q.
>>> # add value -1 at start
>>> k.insert(0,-1)
>>> k
[-1, 100, 20, 'A', 30, 40]
>>> #Q. add -2 after 40
>>> # k.append(-2)
>>> len(k)
6
>>> k.insert(-2,len(k)) # k.insert(-2,6)
>>> k
[-1, 100, 20, 'A', 6, 30, 40]
>>> k.insert(len(k),-2)
>>> k
[-1, 100, 20, 'A', 6, 30, 40, -2]
>>> # -------------------------
>>> # how to remove elements
>>> k
[-1, 100, 20, 'A', 6, 30, 40, -2]
>>> 
>>> k.remove(-1) # remove -1(value from list)
>>> k
[100, 20, 'A', 6, 30, 40, -2]
>>> # remove 'A'
>>> k.remove('A')
>>> k
[100, 20, 6, 30, 40, -2]
>>> x
[1, 2, 3, 4, 1, 1, 1, 6]
>>> # we have duplicates in x
>>> x.remove(1)# remove first occurance
>>> k
[100, 20, 6, 30, 40, -2]
>>> x
[2, 3, 4, 1, 1, 1, 6]
>>> x.remove(1)
>>> x
[2, 3, 4, 1, 1, 6]
>>> x
[2, 3, 4, 1, 1, 6]
>>> x.append(1)
>>> x
[2, 3, 4, 1, 1, 6, 1]
>>> # i want to remove 1 added at the end by mistake
>>> # pop()
>>> help(k.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> x
[2, 3, 4, 1, 1, 6, 1]
>>> # remove last 1
>>> x.pop()
1
>>> x
[2, 3, 4, 1, 1, 6]
>>> x.pop()
6
>>> x
[2, 3, 4, 1, 1]
>>> # remove 3
>>> x.pop(1) # here 1 is index
3
>>> x
[2, 4, 1, 1]
>>> # Q. differentiate remove() and pop()
>>> help(x.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> help(x.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> #----------------------------
>>> 
