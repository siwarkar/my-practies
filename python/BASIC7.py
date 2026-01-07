Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String methods
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # endswith
>>> s = 'hello how r u'
>>> s
'hello how r u'
>>> # it return boolean output
>>> # bcz its a checking operation
>>> # if string is ending with a perticular char or substring then it will return True
>>>  # else returns Fals
>>> s.endswith('u')
True
>>> s.endswith('M')
False
>>> s.endswith('r u')
True
>>> s.endswith('U')
False
>>> ##########
>>> # startswith()
>>> s
'hello how r u'
>>> s.startswith('Hello')
False
>>> s.startswith('hellO')
False
>>> #######
>>> s
'hello how r u'
>>> f = 'Vaibhav Aishwarya  Vijay Sagar'
>>> f
'Vaibhav Aishwarya  Vijay Sagar'
>>> # list of string is expected from above str
>>> # split()
>>> f.split()
['Vaibhav', 'Aishwarya', 'Vijay', 'Sagar']
>>> # splitting criteria is space ' '
>>> s
'hello how r u'
>>> s.split()
['hello', 'how', 'r', 'u']
>>> d = '10,20,30,40'
>>> d
'10,20,30,40'
>>> type(d)
<class 'str'>
>>> # listof numbers expected
>>> d.split(',')
['10', '20', '30', '40']
>>> # Interview que
>>> a = 'hello Ramesh ple call me on:9877654464'
>>> a
'hello Ramesh ple call me on:9877654464'
>>> # fetch mobile number from this string
>>> a.index('9')
28
>>> a[28:]
'9877654464'
>>> # split
>>> a.split(':')
['hello Ramesh ple call me on', '9877654464']
>>> a.split(':')[1]
'9877654464'
>>> a.split(':')[-1]
'9877654464'
>>> ############################
>>> # split converts string to list of string
>>> # but if i have a list and i want a string
>>> f
'Vaibhav Aishwarya  Vijay Sagar'
>>> f.split()
['Vaibhav', 'Aishwarya', 'Vijay', 'Sagar']
>>> fr = f.split()
>>> fr
['Vaibhav', 'Aishwarya', 'Vijay', 'Sagar']
>>> type(fr)
<class 'list'>
>>> # lets convet list of string to a str
>>> # use join()
>>> help(str.join)
Help on method_descriptor:

join(self, iterable, /)
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

>>> fr
['Vaibhav', 'Aishwarya', 'Vijay', 'Sagar']
>>> '.'.join(fr)
'Vaibhav.Aishwarya.Vijay.Sagar'
>>> ' '.join(fr)
'Vaibhav Aishwarya Vijay Sagar'
>>> # str,list,tuple,set,range,dict.. are iterables means collection of elements
>>> '--'.join([10,20,30,40])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    '--'.join([10,20,30,40])
TypeError: sequence item 0: expected str instance, int found
>>> '--'.join(['10','20','30','40'])
'10--20--30--40'
>>> # only string data is expected
>>> ################
>>> # is methods
>>> s
'hello how r u'
>>> # is typemethods of string return boolean output
>>> s.isalpha()
False
>>> # bcz of space we get here False
>>> s1 = 'good'
>>> s1
'good'
>>> s1.isalpha()
True
>>> ###########
>>> #isalnum() alpha-numeric
>>> s2 = 'good123'
>>> s2
'good123'
>>> s2.isalnum()
True
>>> s1
'good'
>>> s1.isalnum()
True
>>> s3 = '123'
>>> s3
'123'
>>> s3.isalnum()
True
>>> ######
>>> s2
'good123'
>>> s2.isnumeric()
False
>>> s2.isdigit()
False
>>> s3
'123'
>>> s3.isdigit()
True
>>> s3.isnumeric()
True
>>> # Q. difference between digit and numeric??
>>> d1 = '12'
>>> d1.isdigit()
True
>>> d1.isnumeric()
True
>>> d2 = '12.55'
>>> d2
'12.55'
>>> d2.isdigit()
False
>>> d2.isnumeric()
False
>>> #########
>>> s3
'123'
>>> s3.isidentifier()
False
>>> 'a'.isidentifier()
True
>>> '2a'.isidentifier()
False
>>> 'a2'.isidentifier()
True
>>> 'a 2'.isidentifier()
False
>>> 'a_2'.isidentifier()
True
>>> 'a_'.isidentifier()
True
>>> '_'.isidentifier()
True
>>> d2
'12.55'
>>> d2.isdecimal()
False
>>> help(d2.isdecimal)
Help on built-in function isdecimal:

isdecimal() method of builtins.str instance
    Return True if the string is a decimal string, False otherwise.
    
    A string is a decimal string if all characters in the string are decimal and
    there is at least one character in the string.

>>> # decimal mean Base10 [0-9]
>>> # maketrans
>>> s = 'hello Sam'
>>> s.maketrans('S','P')
{83: 80}
>>> s.translate(s.maketrans('S','P'))
'hello Pam'
>>> s.translate({83:80})
'hello Pam'
>>> ord('S')
83
>>> ord('P')
80
>>> ord('$')
36
>>> 
