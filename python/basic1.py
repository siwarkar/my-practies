Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # comment: is an information abt code/stuff which we are performing
>>> # using hash we can gie comment in python
>>> 100
100
>>> # 100
>>> #print('hi')
>>> print('hi')
hi
>>> ##############################
>>> # Identifiers: are names given to an object
>>> a = 10
>>> # a is an identifier
>>> # 100 is an object
>>> a
10
>>> # physically exists means it has a memeory
>>> # its present in the memory
>>> # to check memory allocation /address use id()
>>> id(a)
140729678550336
>>> id(100)
140729678553216
>>> id(10)
140729678550336
>>> s = 'python'
>>> s
'python'
>>> id(s)
3028133157552
>>> id('python')
3028133157552
>>> id(10)
140729678550336
>>> id(a)
140729678550336
>>> # heap manages memory in python
>>> a
10
>>> b =10
>>> b
10
>>> id(a)
140729678550336
>>> id(b)
140729678550336
>>> a + b
20
>>> c = a + b
>>> id(c)
140729678550656
>>> id(20)
140729678550656
>>> id(c)
140729678550656
>>> 

