Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String
>>> ''
''
>>> ""
''
>>> '1234'
'1234'
>>> n = '1234'
>>> n[0]
'1'
>>> # backgroudn data structure is Array
>>> # it stores each char/an object separately in a memory block
>>> # and that memory block can be identified using index
>>> # ###
>>> # it supports indexing
>>> # it supports slicing
>>> # Sequence order is maintained
>>> # Methods of a string
>>> s = 'hello all good morning'
>>> s
'hello all good morning'
>>> # upper case
>>> s.upper()
'HELLO ALL GOOD MORNING'
>>> # all methods of a string give temp. output
>>> # now if u chekc s
>>> # it is unchanged
>>> s
'hello all good morning'
>>> #####
>>> # title()
>>> s.title()
'Hello All Good Morning'
>>> # i want only h of hello as a capital form
>>> # capitalize()
>>> s.capitalize()
'Hello all good morning'
>>> ###########################
>>> # to get the info about a function of string
>>> # use  help()
>>> help(s.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> help(str.upper)
Help on method_descriptor:

upper(self, /)
    Return a copy of the string converted to uppercase.

>>> ########################
>>> # to check all methods is there any builtin present???
>>> # yes, u can use dir()
>>> dir(s) # dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 'a' * 4
'aaaa'
>>> len(s)
22
>>> s
'hello all good morning'
>>> k = 'mAnDaR'
>>> k
'mAnDaR'
>>> # convert all characters in lower ccase
>>> k.lower()
'mandar'
>>> k.casefold()
'mandar'
>>> # q. difference between lower and casefold??
>>> k = 'mANDAR mAGDUM'
>>> k
'mANDAR mAGDUM'
>>> # convert upper to lower and viceversa
>>> k.swapcase()
'Mandar Magdum'
>>> #######
>>> k
'mANDAR mAGDUM'
>>> k.title()
'Mandar Magdum'
>>> 'MANDAR'.title()
'Mandar'
>>> #####
>>> k = '   pankaj     '
>>> k
'   pankaj     '
>>> # we want to remove leading and trailing spaces
>>> k.strip()
'pankaj'
>>> # if we want to remove left spaces
>>> k.lstrip()
'pankaj     '
>>> # if we want to remove right spaces
>>> k.rstrip()
'   pankaj'
>>> k = '*****pankaj######     '
>>> k
'*****pankaj######     '
>>> # remove * # space
>>> k.strip('*')
'pankaj######     '
>>> k.strip('*# ')
'pankaj'
>>> # but remember strip removes only from prefix and suffix side
>>> #  if we have special symbols and spaces present in between
>>> p = ' Sa   g$###ar'
>>> p
' Sa   g$###ar'
>>> p.strip(' $#')
'Sa   g$###ar'
>>> # strip only works on prefix and suffix side
>>> # solution is replace
>>> p
' Sa   g$###ar'
>>> p.replace(' ','')
'Sag$###ar'
>>> # replace will change one block at a time
>>> p.replace(' $#','')
' Sa   g$###ar'
>>> # hence we need multiple replace
>>> p.replace(' ','').replace('$','').replce('#','')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    p.replace(' ','').replace('$','').replce('#','')
AttributeError: 'str' object has no attribute 'replce'
>>> p.replace(' ','').replace('$','').replace('#','')
'Sagar'
>>> p.repalce(' ','')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    p.repalce(' ','')
AttributeError: 'str' object has no attribute 'repalce'
>>> p.replace(' ','')
'Sag$###ar'
>>> 'hem    a m^a&%li9789ni'.replace(' ','').replace('^a&%','').replace('9789','')
'hemamlini'
>>> 'hem    a m^a&%li9789ni'.replace(' ','').repalce('^','').replace('&%','').replace('9789','')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    'hem    a m^a&%li9789ni'.replace(' ','').repalce('^','').replace('&%','').replace('9789','')
AttributeError: 'str' object has no attribute 'repalce'
>>> 'hem    a m^a&%li9789ni'.replace(' ','').replace('^','').replace('&%','').replace('9789','')
'hemamalini'
>>> #####################
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s
'hello all good morning'
>>> # count the occurance on any block
>>> s.count('o')
4
>>> s.count('n')
2
>>> # count which is nt present
>>> s
'hello all good morning'
>>> s.count('RRR')
0
>>> ##########
>>> k
'*****pankaj######     '
>>> # if u want to check objects present in current memeory env. then use empty dir()
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'k', 'n', 'p', 's']
>>> k
'*****pankaj######     '
>>> n
'1234'
>>> p
' Sa   g$###ar'
>>> s
'hello all good morning'
>>> d = 'Akshata'
>>> d
'Akshata'
>>> d.center(20)
'      Akshata       '
>>> d.center(20,'*')
'******Akshata*******'
>>> help(d.center)
Help on built-in function center:

center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.
    
    Padding is done using the specified fill character (default is a space).

>>> ##########
>>> s
'hello all good morning'
>>> s.find('all') # returns index
6
>>> s[6]
'a'
>>> s.find('o')# returns lowest index
4
>>> s[4]
'o'
>>> # if u want to fetch highest index then
>>> s.rfind('o')
16
>>> s[16]
'o'
>>> ##########
>>> s
'hello all good morning'
>>> # index
>>> s.index('o')
4
>>> s.rindex('o')
16
>>> s.find('o')
4
>>> s.rfind('o')
16
>>> # Q. difference between find and index???
>>> # ans: is related to unkown instance
>>> s
'hello all good morning'
>>> s.find('KGF')
-1
>>> s.index('KGF')
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    s.index('KGF')
ValueError: substring not found
>>> help(s.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> 
