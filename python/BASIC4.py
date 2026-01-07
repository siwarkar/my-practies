Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Data Structures
>>> # list
>>> []
[]
>>> list()
[]
>>> # Tuple()
>>> # syntax
>>> ()
()
>>> type(())
<class 'tuple'>
>>> tuple()
()
>>> t = (2,3,4,5)
>>> t
(2, 3, 4, 5)
>>> type(t)
<class 'tuple'>
>>> (10,20,33.33,4+4j,'java')
(10, 20, 33.33, (4+4j), 'java')
>>> ##################
>>> #Set
>>> # syntax {10,}
>>> {}
{}
>>> type({})
<class 'dict'>
>>> {10,}
{10}
>>> type({10,})
<class 'set'>
>>> set()
set()
>>> s = set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> # how to create an empty set
>>> ############
>>> # Dict: Dictionary
>>> # syntac: {key:value}
>>> # it is a combination of key and value pair
>>> # empty dict?
>>> {}
{}
>>> type({})
<class 'dict'>
>>> dict()
{}
>>> d = {1:100,2:200,3:300}
>>> d
{1: 100, 2: 200, 3: 300}
>>> type(d)
<class 'dict'>
>>> d2 = {'name':'Mahesh','age':22,'place':'Pune'}
>>> d2
{'name': 'Mahesh', 'age': 22, 'place': 'Pune'}
>>> ##################
>>> # range()
>>> # used to create sequential numbers
>>> # number defaault starts from 0
>>> # range(stop)
>>> range(10) # 0-9
range(0, 10)
>>> #range(0=start, 10=stop)
>>> # to get output of range, we need to convert into other data type
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> tuple(range(10))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> # 2nd option of range
>>> # range(start,stop)
>>> # start at 11 and stop at 20[11-20]
>>> range(11,21)# need 20 to be present in the output
range(11, 21)
>>> list(range(11,21))
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> list(range(101,111))
[101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
>>> # can we get -ve values
>>> list(range(-12))
[]
>>> list(range(-12,-1))
[-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2]
>>> list(range(-12,-1,1))# extra 1 is a step
[-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2]
>>> # if we change the stepping
>>> list(range(-12,-1,2))
[-12, -10, -8, -6, -4, -2]
>>> #3rd option in range
>>> # range(start,stop,step)
>>> list(range(1,101))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> list(range(1,101,2))# odd numbers
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> # even numbers
>>> list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> # Can we perform stepping by -1
>>> list(range(10,0,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> list(range(0,10,-1))
[]
>>> # +ve stepping means left to right(increasing order)
>>> # -ve stepping mean right to left(reverse order)
>>> # -6 to +6
>>> list(range(-6,7))
[-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
>>> # +6 to -6
>>> list(range(6,-7,-1))
[6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]
>>> list(range(100,0))
[]
>>> list(range(100,0,-1))
[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> ################
>>> # Frozenset()
>>> s = frozenset()
>>> s
frozenset()
>>> type(s)
<class 'frozenset'>
>>> ##############
>>> # bytes()
>>> k = [19,20,34]
>>> k
[19, 20, 34]
>>> bytes(k)
b'\x13\x14"'
>>> # bytearray()
>>> bytearray(k)
bytearray(b'\x13\x14"')
>>> # bytes and bytearray give conversion of int list into a byte sequence
>>> # but both are different
>>> ######################
>>> None
>>> # none mean nothing
>>> # its a Null
>>> ################
>>> x = bytearray(k)
>>> x
bytearray(b'\x13\x14"')
>>> type(x)
<class 'bytearray'>
>>> list(x)
[19, 20, 34]
>>> ##########################
>>> # Type casting/Type conversion
>>> # COnverting from one data type to another is nothing but type casting
>>> num = 25
>>> type(num)
<class 'int'>
>>> # Number system:
>>> # Binary, Octal, Decimal, Hexadecimal
>>> # python default supports decimal numbers
>>> # decimal numbers means base 10[0-9]
>>> # lets start converting the number
>>> num
25
>>> # binary
>>> bin(num)
'0b11001'
>>> # octal 0-7
>>> oct(num)
'0o31'
>>> # hex
>>> # 0-9A-F
>>> # base 16
>>> hex(num)
'0x19'
>>> 0b11001
25
>>> 0o31
25
>>> 0x19
25
>>> #######
>>> num
25
>>> # str
>>> str(num)
'25'
>>> # list
>>> list(num)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    list(num)
TypeError: 'int' object is not iterable
>>> # list requires collection of element
>>> # it wont work on single element
>>> list((2,3,4))
[2, 3, 4]
>>> # bool
>>> num
25
>>> bool(25)
True
>>> # tuple
>>> tuple(num)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    tuple(num)
TypeError: 'int' object is not iterable
>>> # tuple requires collection of element
>>> tuple([10,33,20])
(10, 33, 20)
>>> ###
>>> num
25
>>> complex(num)
(25+0j)
>>> ######
>>> age = '34'
>>> age
'34'
>>> type(age)
<class 'str'>
>>> # add 2 in age
>>> age + 2
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    age + 2
TypeError: can only concatenate str (not "int") to str
>>> int(age) + 2
36
>>> #####
>>> # calculate monthly salary
>>> no_of_day = 20
>>> per_day = 500
>>> per_day = '500'
>>> no_of_day * per_day
'500500500500500500500500500500500500500500500500500500500500'
>>> # it happens bcz int * str performs repetition
>>> no_of_day * float(per_day)
10000.0
>>> ################
>>> # if we want to check info about anything builtin  of python
>>> # then use help()
>>> help(float)
Help on class float in module builtins:

class float(object)
 |  float(x=0, /)
 |  
 |  Convert a string or number to a floating point number, if possible.
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |      
 |      When an argument is passed, work like built-in round(x, ndigits).
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original float
 |      and with a positive denominator.
 |      
 |      Raise OverflowError on infinities and a ValueError on NaNs.
 |      
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |  
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |  
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |      
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |  
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |      
 |        typestr
 |          Must be 'double' or 'float'.
 |      
 |      It exists mainly to be used in Python's test suite.
 |      
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |  
 |  __set_format__(typestr, fmt, /) from builtins.type
 |      You probably don't want to use this function.
 |      
 |        typestr
 |          Must be 'double' or 'float'.
 |        fmt
 |          Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',
 |          and in addition can only be one of the latter two if it appears to
 |          match the underlying C reality.
 |      
 |      It exists mainly to be used in Python's test suite.
 |      
 |      Override the automatic determination of C-level floating point type.
 |      This affects how floats are converted to and from binary strings.
 |  
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |      
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number

>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
