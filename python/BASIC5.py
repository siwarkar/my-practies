Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Typecasting
>>> # Implicit and explicit typecasting
>>> # Implicit is  performed by Python itself
>>> # example
>>> 10 + 4.0
14.0
>>> # numbers: int--> float --> complex
>>> 1 + 3+4j #addition of int + complex
(4+4j)
>>> # exmple
>>> 10/2
5.0
>>> # at runtime/it dynamically decide datatype
>>> # based on it precision
>>> 10 + 20
30
>>> '10'+ '20' #it we concatenate 2 strings
'1020'
>>> [1,2,3] + [4,5]
[1, 2, 3, 4, 5]
>>> ############
>>> # Explicit conversion
>>> # casting performed by a user is explicit
>>> # Example
>>> 10/2 # gives float output
5.0
>>> # but i wnt in int
>>> int(10/2)
5
>>> '10' + '20'
'1020'
>>> float('10') + float('20')
30.0
>>> ###############
>>> # String
>>> # syntax
>>> ''
''
>>> ""
''
>>> type('')
<class 'str'>
>>> #-----------------
>>> # Features of String
>>> # Its a global datatype which accepts eveything u give inside a quotes
>>> 'jbhkjhjkasdjkasd'
'jbhkjhjkasdjkasd'
>>> '23343435456546'
'23343435456546'
>>> '#$@&*#$*&@^@#$<>?:"{}{'
'#$@&*#$*&@^@#$<>?:"{}{'
>>> '[1,2,3]'
'[1,2,3]'
>>> #######
>>> # Background data structure of a string is Array
>>> s = 'Python'
>>> s
'Python'
>>> # Each element is stored in a separate block of memeory
>>> # and we can fetch each element using index
>>> # String has an index support to access each block from it
>>> # using index we can access individual element
>>> s
'Python'
>>> #Indexing is of 2 types
>>> # +ve/forward direction indexing
>>> # it starts from left to right
>>> # starts from 0 and stops at (n-1)
>>> # here n means total number of elements in a string
>>> #check total elements in s
>>> len(s)
6
>>> len(s) -1
5
>>> s
'Python'
>>> # what is use of index
>>> # usiing index we can access each element
>>> s
'Python'
>>> # to do indexing use []
>>> s[0]
'P'
>>> s[2]
't'
>>> s[5]
'n'
>>> s[1]
'y'
>>> # -ve indexing is also present
>>> # backward direction indexing
>>> # moves from right to left
>>> # starts at -1 and stop at -n
>>> s
'Python'
>>> s[-1] # gives last element
'n'
>>> s[-3]
'h'
>>> s[-6]
'P'
>>> # -ve indexing is to fetch elements in reverse order
>>> # Using index we can access one element at a time
>>> k = 'google.com'
>>> k
'google.com'
>>> k[0]
'g'
>>> k[2]
'o'
>>> k[-1]
'm'
>>> k[-4]
'.'
>>> k
'google.com'
>>> k[-8]
'o'
>>> k[5]
'e'
>>> # But if i want to access multiple elements from a string
>>> s
'Python'
>>> # access thon
>>> # to get this result we have SLICING
>>> # syntax: [:]
>>> # [start:stop] #index u have to put
>>> s[:]#no start no stop
'Python'
>>> s[0:]
'Python'
>>> # in this: stop is exclusive
>>> # means index we supply in stop, that element wont be present in output
>>> s[0:-1]# n will nt be in output
'Pytho'
>>> s[:]
'Python'
>>> s[0:6]
'Python'
>>> s
'Python'
>>> s[2:] #start from 2 index
'thon'
>>> s[2:4]
'th'
>>> s[4]
'o'
>>> k
'google.com'
>>> k[:3]
'goo'
>>> k[6:]
'.com'
>>> # gle
>>> k[3:6]
'gle'
>>> # google.
>>> k[:7]
'google.'
>>> # We can use -ve index in slicing
>>> s
'Python'
>>> s[-4:]
'thon'
>>> # on
>>> s[-2:]
'on'
>>> # Py
>>> s[-6:-4]
'Py'
>>> # if we want to read in reverse order then use -ve stepping
>>> # s[::]
>>> # s[start:stop:step]
>>> s[::]
'Python'
>>> s[::1]
'Python'
>>> s[::1] # means forward direction left to right
'Python'
>>> s[::-1] # means backward direction/reverse order, right to left
'nohtyP'
>>> s
'Python'
>>> k
'google.com'
>>> k[::-1]
'moc.elgoog'
>>> s
'Python'
>>> k
'google.com'
>>> k[-1:-7]# le.com
''
>>> k[-1:-7:-1]# le.com
'moc.el'
>>> #k[start:stop:step]
>>> k
'google.com'
>>> k[-2:-6:-1]
'oc.e'
>>> k[-4:]
'.com'
>>> # Step 1 means left to right
>>> # Step -1 means right to left in reverse order
>>> k
'google.com'
>>> k[:-3]
'google.'
>>> k[-2::-1]
'oc.elgoog'
>>> # read google in reversse
>>> k
'google.com'
>>> k[-5::-1]
'elgoog'
>>> # com in reverse
>>> k[-1:-4:-1]
'moc'
>>> # select google by +ve index
>>> k
'google.com'
>>> k[:6]
'google'
>>> k[:6][::-1]
'elgoog'
>>> 'google'[::-1]
'elgoog'
>>> k[:6]
'google'
>>> k[:6][3:]
'gle'
>>> # [] output in slicing means out logic is wrong
>>> k
'google.com'
>>> k[-2:-6]
''
>>> k[-2:-6:-1]
'oc.e'
>>> 
