"""
Function:
Variables in a function:
Global var:
it is a var. which is accesible anywhere
within the program
----------------
x = 30 # global var.
def sample():
    print('Inside:',x)

print('outside:',x)
# call func
sample()
----------------------
Suppose we try to change a value of global variable
inside a function
-------------------------
# outside a function means Global
# inside a function mmeans local

x = 30 # global var.
def sample():
    # lets change value of global x
    # x = 10
    # use global keyword to change global x
    global x
    x += 100
    print('Inside:',x)

print('outside:',x)
# call func
sample()
# hence using global keyword
# we can change value  of global var inside a local scope

---------------------------
# Problem with global keyword
----------
# outside a function means Global
# inside a function mmeans local

x = 30 # global var.
def sample():
    # lets change value of global x
    # x = 10
    # use global keyword to change global x
    global x
    x += 100
    print('Inside:',x)

print('before outside:',x)
# call func
sample()
print('After outside:',x)
# u changes value of global var inside a local
# scope
# now updated global x will be available further
-----------------------
local var:
x = 30 # global var.
def sample():
    x = 100 # local var.
    print('Inside:',x)

print('outside:',x)
# call func
sample()
-----------------------
# can we access local variable
# outside a function: NO
def sample():
    x = 100 # local var.
    print('Inside:',x)

sample()
print('outside:',x)
# local var is only available within the
# scope , outside it wont be available

--------------------
# Function with return:
syntax of function:
def func_name(x,y):
    return x + y # optional
func_name(10,20)
----------------------

def add(x,y):
    #print(x+y)
    # dont print output of x+y INSIDE
    # we want ouput of it outside
    # then use return
    return x+y
    #pass
    
print(add(20,30))
# return: if we perform some calculations
# inside a function n we wwnt the output
# outside function then
# then use return

------------------------
def sample(name,age,sal):
    return sal,name,age
#print(sample('Vrushali',25,45000))
result = sample('Pankaj',25,56000)
print(result)
a1,a2,a3 = result
print(a2)
# if we want values from local to global scope
# then return is there to help u in this regard
-------------------------
# can we perfrom multiple opeerations
# n multiple returns?==> YES
def test(a,b):
    #return a+b,a-b,a*b,a/b
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b

    return add,mul
    #only 2 ops i want outside
result = test(10,20)
print(result)
--------------------
Q. what is return
Q. why we use it/ need?
Q. can we return multiple values... yes
Q. WHen no return then function gives wht? => None
-------------------------
Function Aliasing:
Giving a nick name/short name to a function
a new function name will act like a ref
============
def structural_design(s1,s2,s3):
    print(s1,s2,s3)
structural_design(10,20,30)
# lets use a short/alias
sd = structural_design
print(sd)
sd(1,2,3)
========================
def structural_design(s1,s2,s3):
    print(s1,s2,s3)
structural_design(10,20,30)
# lets use a short/alias
sd = structural_design
print(sd)
sd(1,2,3)
structural_design('A','B','C')
# delete one ref
del structural_design
#structural_design('AA','BB','CC')
sd('AA','BB','CC')

print(dir())
---------------------
"""
















