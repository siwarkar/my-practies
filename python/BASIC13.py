Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Range
>>> range(5) # range(stop)
range(0, 5)
>>> # main purpose of range function is to generate sequential numbers
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> #--------------------------
>>> bytes()
b''
>>> bytes([23,45])
b'\x17-'
>>> # up to 256 number we can give
>>> bytes([255])
b'\xff'
>>> bytes([256])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    bytes([256])
ValueError: bytes must be in range(0, 256)
>>> bytes('abc')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    bytes('abc')
TypeError: string argument without an encoding
>>> bytes('abc','utf8'))
SyntaxError: invalid syntax
>>> bytes('abc','utf8')
b'abc'
>>> # it converts data into a byte seqeunce
>>> #background data structure is an array
>>> b = bytes([10,20,30])
>>> b
b'\n\x14\x1e'
>>> #index
>>> b[0]
10
>>> b[-1]
30
>>> # slicing
>>> b[::-1]
b'\x1e\x14\n'
>>> b[1:]
b'\x14\x1e'
>>> #-----------
>>> # Is it mutable??
>>> b
b'\n\x14\x1e'
>>> b[-1]
30
>>> # lets try to direct assign 300 instead of 30
>>> b[-1] = 300
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b[-1] = 300
TypeError: 'bytes' object does not support item assignment
>>> # Direct item assignment is not possible hence its Immutable
>>> #check methods supported by bytes
>>> dir(b)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # methods of bytes are same as that of string hence it Immutable
>>> #-----------------------------
>>> # if we want mutable byte sequence then use bytearray
>>> c = bytearray([10,20,30])
>>> c
bytearray(b'\n\x14\x1e')
>>> c[-1]
30
>>> c[-1] = 300 #change 30--> 300
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    c[-1] = 300 #change 30--> 300
ValueError: byte must be in range(0, 256)
>>> c[-1] = 250
>>> c
bytearray(b'\n\x14\xfa')
>>> # direct item assignemnt is possible hence its Mutable
>>> dir(c)
['__add__', '__alloc__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'capitalize', 'center', 'clear', 'copy', 'count', 'decode', 'endswith', 'expandtabs', 'extend', 'find', 'fromhex', 'hex', 'index', 'insert', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'pop', 'remove', 'replace', 'reverse', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # bytearray is a combi. of String + list
>>> #-------------------------------------
>>> # frozenset()
>>> frozenset()
frozenset()
>>> frozenset([1,2,3,4,5])
frozenset({1, 2, 3, 4, 5})
>>> s = frozenset([1,2,3,4,5])
>>> s
frozenset({1, 2, 3, 4, 5})
>>> type(s)
<class 'frozenset'>
>>> # normal set is Mutable
>>> # but frozenset is nt Mutable/Immutable
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> # all above methods are able to give temp output
>>> # hence its Immutable
>>> # Q. set vs frozenset??
>>> #----------------------------------
>>> # Flow control block
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
I want to eat Pizza
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
I want to eat Pizza
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
Eat Vadapav
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
Admit +medication
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
14 days isolation
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
Welcome to COWIN portal
Enter your test result(+ve/-ve):-ve
14 days isolation
>>> 
 RESTART: C:/Users/hakim/AppData/Local/Programs/Python/Python37/20/sample.py 
Welcome to COWIN portal
Enter your test result(+ve/-ve):+ve
Admit +medication
>>> b = bytearray([10,20,30])
>>> b
bytearray(b'\n\x14\x1e')
>>> b[-1] = 250
>>> b
bytearray(b'\n\x14\xfa')
>>> list(b)
[10, 20, 250]
>>> 
