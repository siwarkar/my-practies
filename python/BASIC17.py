"""
Functions:
syntax:
#declaration
def function_name(parameters):
    .
    .
    .
# calling
function_name()
-------------------

def sample(a,b):
    print(a,b)
sample('A','B')
sample(12,33)
sample(-4,5)
-------------------
# supply same number of values from calling
def sample(a,b): # 2 arguments a,b
    print(a,b)
sample('A') #expected 2 but we are supplying 1 valuue
-------------------------------
Types of Arguments:
1. positional argument: in which sequence order matters,
if we change sequence then it changes output
---------------------
def info(name,age,place):
    print('Your name is:',name)
    print('Your age is:',age)
    print('Your place is:',place)

info('Vrunda',22,'Pune')
info(24,'Satara','Sagar')#sequence changed==>will change output
---------------------------
2. Keyword arguments: sequence order doesnt matter
bcz it maps values with keys present in declaration
Example:-
--------------------
def info(name,age,place):
    print('Your name is:',name)
    print('Your age is:',age)
    print('Your place is:',place)

info('Vrunda',22,'Pune')
info(age = 24,place = 'Satara',name = 'Sagar')#sequence changed
====================================
3. default argument:
is an argument which can be used as a constant but its changable
-------------------------
def bank(name,cust_id,branch='SBI'): #branch is default argument
    print(name,cust_id,branch)
bank('Shital',123)
bank('Swati',345,'BOI')
-------------------------------
4. Variable length argument
- Variable length positional args

def add(*n): #accept multiple values
    print(n)
    print(sum(n))

add(1,2)
add(10,20,30)
add()
add(-23,4,5,6,7)
-------------------------
def sample(*args):
    print(args)
sample(10,20)
sample()
sample('A','B','C','D')
------------------------------------
- Variable length keyword args
def details(**kwargs):
    print(kwargs)
# in calling supply keyword arguments
details(name ='Pankaj',place='Kolhapur')
details(id=12,amt = 45000,pin=411223)
details()
=============================
Q.  Explain differnt types of arguments in function
Q. What is default argumnt?
Q. explain *args,**kwargs
Q. differentiate *args,**kwargs
Q. when to use variable length args
--------------------------
# problem associated with positional +keyword
def info(name,age):
    print(name,age)
# info(name='python',31)
#info(31,name='python')
# Rule: if we r using combination of pos+keywrd then
# keyword args should be declared at the end
#in calling
info('python',age= 31)
------------------
def sample(b,c,a=100):
    print(a,b,c)
sample(10,20,'A')
# in declaring default args, it must be at the end

"""












































    
    





