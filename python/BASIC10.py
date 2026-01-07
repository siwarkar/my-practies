Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List methods
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # reverse
>>> a = [12,45,67,0,1,10,2,5,90,4]
>>> a
[12, 45, 67, 0, 1, 10, 2, 5, 90, 4]
>>> help(a.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.

>>> # changes persist directly in list a
>>> a
[12, 45, 67, 0, 1, 10, 2, 5, 90, 4]
>>> a.reverse()
>>> a
[4, 90, 5, 2, 10, 1, 0, 67, 45, 12]
>>> a.reverse()
>>> a
[12, 45, 67, 0, 1, 10, 2, 5, 90, 4]
>>> a[::-1] # temporary
[4, 90, 5, 2, 10, 1, 0, 67, 45, 12]
>>> a
[12, 45, 67, 0, 1, 10, 2, 5, 90, 4]
>>> #----------------------------
>>> # sort()
>>> help(a.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Stable sort *IN PLACE*.

>>> # changes persist directly in the same object
>>> a
[12, 45, 67, 0, 1, 10, 2, 5, 90, 4]
>>> # default sorting is performed in ascending order
>>> a.sort()
>>> a
[0, 1, 2, 4, 5, 10, 12, 45, 67, 90]
>>> # if we want sort in descending order
>>> a.sort(reverse= True)
>>> a
[90, 67, 45, 12, 10, 5, 4, 2, 1, 0]
>>> # Sort works on String data also
>>> n = ['mandar','aishwarya','vikas','sagar','akash']
	 
>>> n
	 
['mandar', 'aishwarya', 'vikas', 'sagar', 'akash']
>>> n.sort()
	 
>>> n
	 
['aishwarya', 'akash', 'mandar', 'sagar', 'vikas']
>>> # sorted in a-z alphabatic order
	 
>>> # if we want z-a
	 
>>> n.sort(reverse=True)
	 
>>> n
	 
['vikas', 'sagar', 'mandar', 'akash', 'aishwarya']
>>> # key
	 
>>> n
	 
['vikas', 'sagar', 'mandar', 'akash', 'aishwarya']
>>> # we want to sort the list of string on the basis of len
	 
>>> n.sort(key=len) #ascending
	 
>>> n
	 
['vikas', 'sagar', 'akash', 'mandar', 'aishwarya']
>>> j = ['AAA','A','AAAA','A']
	 
>>> j
	 
['AAA', 'A', 'AAAA', 'A']
>>> j.sort(key=len)
	 
>>> j
	 
['A', 'A', 'AAA', 'AAAA']
>>> # if list is a combo
	 
>>> p = [10,'A',20,'B']
	 
>>> p.sort()
	 
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    p.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> # only Homogeneous data(data of same type) is suppported in sort
	 
>>> # heterogeneous data is not supported
	 
>>> #------------------------------------
	 
>>> # tuple()
	 
>>> #  it has same features as that of list
	 
>>> # #xcept: Tuple is Immutable
	 
>>> ()
	 
()
>>> tuple()
	 
()
>>> t = (1,2,3,4)
	 
>>> t
	 
(1, 2, 3, 4)
>>> # It accepts homo/hetro. values
	 
>>> (1,2,3)
	 
(1, 2, 3)
>>> (1,23.4,'A')
	 
(1, 23.4, 'A')
>>> # it preserves sequence order
	 
>>> # values present in same order as we have supplied
	 
>>> # Background data structure is : Array
	 
>>> # Supports Indexing
	 
>>> t
	 
(1, 2, 3, 4)
>>> t[0]
	 
1
>>> # +ve and -ve indexing supported
	 
>>> t[-1]
	 
4
>>> # slicing is possible
	 
>>> t[::-1]
	 
(4, 3, 2, 1)
>>> t[2:]
	 
(3, 4)
>>> # Lets try to change value of a tuple using index
	 
>>> t
	 
(1, 2, 3, 4)
>>> t[0]
	 
1
>>> t[0] = 100 # replace 1 by 100
	 
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t[0] = 100 # replace 1 by 100
TypeError: 'tuple' object does not support item assignment
>>> m = 'mango'
	 
>>> m[1]
	 
'a'
>>> m[1] = 'O'
	 
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    m[1] = 'O'
TypeError: 'str' object does not support item assignment
>>> # this is 1st reason why tuple is immutable
	 
>>> ls = [1,2,3,4]
	 
>>> ls[0]
	 
1
>>> ls[0] = 100
	 
>>> ls
	 
[100, 2, 3, 4]
>>> # list is mutable
	 
>>> # direct change is possible
	 
>>> #-----------------------
	 
>>> # in tuple we dont have any method for manipulation of tuple
	 
>>> dir(tuple)
	 
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> # it contains only 'count', 'index' 2 mthods
	 
>>> # Hence 2nd reason : Tuple is immutable
	 
>>> # Q. why tuple is Immutable
	 
>>> #--------------------------
	 
>>> # Packing and unpacking of tuple
	 
>>> # comma separated values are always tuple
	 
>>> 10,
	 
(10,)
>>> 1,2,3
	 
(1, 2, 3)
>>> 'A','B','C'
	 
('A', 'B', 'C')
>>> 12,'A',3.33
	 
(12, 'A', 3.33)
>>> # packing
	 
>>> # grouping of multiple objects as s single unit
	 
>>> n = 'A','B','C'
	 
>>> n
	 
('A', 'B', 'C')
>>> y = 12,'A',3.33
	 
>>> y
	 
(12, 'A', 3.33)
>>> # Unpacking: reverse to packing
	 
>>> # if we have grouped objects, we can separate them into an individual identifier
	 
>>> y
	 
(12, 'A', 3.33)
>>> x1,x2,x3 = y
	 
>>> x1
	 
12
>>> x2
	 
'A'
>>> x3
	 
3.33
>>> # Examples
	 
>>> x = 1,2,3
	 
>>> # this is packing
	 
>>> #########
	 
>>> a,b,c = 10,20,30
	 
>>> a
	 
10
>>> b
	 
20
>>> c
	 
30
>>> # this is unpacking
	 
>>> #############################
	 
>>> # Write a program to swap value of 2 variables without using third variable
	 
>>> a
	 
10
>>> b
	 
20
>>> # we want 20 in a and 10 in b
	 
>>> a,b
	 
(10, 20)
>>> b,a = a,b
	 
>>> b
	 
10
>>> a
	 
20
>>> ######################
	 
>>> t1 = (1,2,3)
	 
>>> t1
	 
(1, 2, 3)
>>> t2 = (4,5,6)
	 
>>> t2
	 
(4, 5, 6)
>>> # if we add t1 and t2
	 
>>> t1 + t2
	 
(1, 2, 3, 4, 5, 6)
>>> # in above , it changes tuple, so can we call tuple as mutable???
	 
>>> t1
	 
(1, 2, 3)
>>> t2
	 
(4, 5, 6)
>>> # t1 and t2 are not changed
	 
>>> # hence its nt mutable
	 
>>> #---------------------------------------------
	 
>>> # Q.
	 
>>> t1
	 
(1, 2, 3)
>>> #check size of t1
	 
>>> t1.__sizeof__()
	 
48
>>> a1 = [1,2,3]
	 
>>> a1
	 
[1, 2, 3]
>>> a1.__sizeof__()
	 
64
>>> #Q. why list requires/takes more memory than tuple????
	 
>>> 
