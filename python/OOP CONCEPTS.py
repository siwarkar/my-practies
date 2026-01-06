******************************************************************OP1.PY*************************************************************************
"""
OOP: Object Oriented Programming
Class:
it is template, blueprint, structure, design which is composed of 2 things
- Properties ( Data Members/ variables )
- behavior ( Methods )
Example: Mobile
- variables: RAM ROM Screensize, OS, Camera etc
- behaviour: Power on, shutdown, silent (operations/actions)
class Icecream:
    var: ingredients
    action: boiling, mixing. etc
--------------------------------------------
class Cake:
    sugar = 1
    milk = .5

    def baking(self):
        print('Its baking process')

    def icing(self):
        print('Icing process')
# calling of class Cake is important
# bcz it will give u an access to the members of a class
# u can able to call methods using class calling
#Cake()
# this calling make everything available outside the class
print(Cake().milk,Cake().sugar)
# call the methods inside a  class
Cake().baking()
Cake().icing()
------------------------------------------
class Cake:
    sugar = 1
    milk = .5

    def baking(self):
        print('Its baking process')

    def icing(self):
        print('Icing process')
#print(dir(Cake()))
print(id(Cake()))
print(id(Cake()))
a = Cake()
b = Cake()
print(id(a),id(b))
# Rather than calling a class multiple times it will create multiple objects
# so we have an option for this
==========================================================
class Cake:
    sugar = 1
    milk = .5

    def baking(self):
        print('Its baking process')

    def icing(self):
        print('Icing process')
c1 = Cake()
print(c1.milk)
c1.baking()
print('------------------------')
c2 = Cake()
c2.milk = 2
c2.sugar = 2.5
c2.issence = 'orange'
print(c2.milk,c2.sugar)
c2.icing()
# lets check directory structure of both objects
print('--------------------')
print(dir(c1))
print(dir(c2))
print(c2.__dict__) #used to check variables currently present in object
print('-lets delete some variables-----')
del c2.sugar
print(c2.__dict__)
del c2.issence
print(c2.issence)
========================================================
"""
******************************************************************OP2.PY*******************************************************
"""
OOP:
class class_name:
    properties
    behaviour
--------------------------------
Convention
Use class name in Title case if its a single word
class Bank:
    pass

if its a combi. of 2 words then use CamelCase
class BankDetails:
    pass
========================================================
Recall:
class
class calling
object
--------------------------
class calling--> Constructor calling
-----------------------------------
class Bank:
    ifcs = 'BKID2324'
    def deposit(self):
        pass
    def withdraw(self):
        pass
b = Bank()
b.deposit()
# constructor: is used to allocate a memory
# Feature:
# Constructor has same name as that of class Name
# it allocates a memory
# Constructor can be empty or parameterized
print(dir())
------------------------------------------
# Create an empty constructor
class Sample:
    def __init__(self): #initializes memory
        print('Constructor method')
    def display(self):
        pass
Sample()
Sample()
# Q. what is constructor
# Q. what is __init__
# Q. differentiate method vs constructor
Sample().__init__()
------------------------------------
Parameterized constructor
----------------------
class Sample:
    def __init__(self,name,age):
        print('Name is:',name,'& age is:',age)

Sample('Priya',25)
Sample(24,'Renuka')
# above are positional args.
----------------------------
Use keyword argument
------------------------
class Sample:
    def __init__(self,name,age):
        print('Name is:',name,'& age is:',age)

#Sample('Priya',25)
Sample(age=24,name='Renuka')
# above arg type is keyword agrs..
=========================================
Use default args
-------------------------
class Sample:
    def __init__(self,name,age=18):
        print('Name is:',name,'& age is:',age)

# default age values is set to 18
Sample(name='Renuka')
Sample('Suhas',26)
--------------------------------
*args , **kwargs: Variable length argument
class Sample:
    def __init__(self,*args):
        print(args)

# default age values is set to 18
Sample('Dipti',22)
Sample('Suhas',26,'Pune')
-----------------------------------
class Sample:
    def __init__(self,**kwargs):
        print(kwargs)

# default age values is set to 18
Sample(name='Dipti',age=22)
Sample(name='Suhas',age=26,place='Pune')
Sample()
-----------------------------------
Is the init only option to supply arguments???
Answer is NO
We can suppply arguments to any normal method
---------------------------------------------
class Sample:
    def info(self,roll_no,name,std):
        print(roll_no,name,std,sep='\n')

Sample().info(12,'Ashwin',10)
--------------------------------------------
class Sample:
    def info(self,roll_no,name):
        # roll_no and name are local to info
        # we need to make them instance variables
        # using self we can make it
        self.roll_no = roll_no
        #(instance)    (local)
        self.name = name

    def display(self):
        print('Details provide by user:')
        print(self.roll_no)
        print(self.name)

s = Sample()
s.info(10,'A')
s.display()
# s--> Sample()--> info--> display()

#Sample().info(100,'abc')
#Sample().display()

# right way
#Aap-->Father--->Yameen-->Money
#object-->Constructor--> info-->display

# wrong way
#Constructor--> info
#Constructor---->display
------------------------------------------
self:
it works like a reference variable inside a class
it is active only inside a method
it wont work outside the method and class

Inside a method we can access and call any of the member of a class
------------------------
Task we can perform using self
1. add new instance variable using self
-------------------------------------------
class Test:
    pin = 1234
    def register(self,name):
        print(name) #name is local to register method
        self.name = name


    def task(self):
        print('welcome',self.name,'to a task')
        print(Test.pin)
        # className acts a a ref for variables declared inside a class
        # and outside a method
    def task2(self):
        print(self.name)
        # lets add new variables
        # we add using self
        self.age = 45
        self.pincode = 411008

t = Test()
t.register('XYZ')
t.task()
t.task2()
print(t.__dict__)
#print(t.age)

# We have 3 reference variables
# - self: inside a class+method
# - object: outside a class
# - className: inside a class method
------------------------------------------------
"""
***********************************************************************OP3.PY********************************************************************
"""
explore self:
it acts as pointer/a reference variable which is responcible for
accessing everything inside class into a method
----------------------------------
class Sample:
    def __init__(self,name,age,salary):
        # make instance variable
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        # fetch details from init and display here
        print(self.name,self.age,self.salary)

s = Sample('A',22,80000)
s.display()
# we can check instance var using __dict__
print(s.__dict__)
-----------------------------------------
If I want to change var. inside a method
- yes it is possible using self
self makes variables as a instance
and instance var. are those whose value changes from object to object
--------------------------------------------
class Sample:
    def __init__(self,name,age,salary):
        # make instance variable
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        # fetch details from init and display here
        self.name= 'Akshay'
        print(self.name,self.age,self.salary)

s = Sample('A',22,80000)
s.display()
# we can check instance var using __dict__
print(s.__dict__)

s2 = Sample('Swapnil',24,78000)
print(s2.__dict__)
# from outside change salary
s2.salary = 98000
print(s2.__dict__)
# swapnil want bonus
s2.bonus = 10000
print(s2.__dict__)
---------------------------------------------
# Types of variables in OOP
- Local: method level
- Global: outside class
- instance: inside instance method
- static/class level variable: inside a class and outside a method
============================================
Local var:
class Sample:
    def m1(self):
        x = 100 #local to m1
        print(x)
    def m2(self):
        #print(x) #wont be available in m2
        pass

s = Sample()
print(s.x) # local var. nt accessible outside a class
-----------------------------------------------
Global variable:
x = 'global'
class Sample:
    print(x)

    def m1(self):
        print(x)

print(x)
s = Sample()
s.m1()
------------------------------
- instance var: inside instance method
----------------------
class Sample:
    def m1(self):
        self.x = 12
    def m2(self):
        print(self.x)

s = Sample()
s.m1()
print(s.x)
s.m2()
---------------------------------
static/class level variable: inside a class and outside a method
------------------------------------
class Sample:
    st = 'static'
    def m1(self):
        #print(st)
        # static var will nt be available inside instance method
        pass
    def m2(self):
        # to access st inside m2 take the help of className ref
        print(Sample.st)
s = Sample()
s.m2()
# can we access static var outside a class
print(s.st)
# use className outside as well to access static var
print(Sample.st)
# className acts as a reference for a static var.
# which works inside a method and outside a class also
-----------------------------------
# lets try to change static variable using className as a ref.
class Bank:
    ifsc = 'SBI76523' # static var
    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc
        Bank.ifsc = 'PNB45678'
print(Bank.ifsc)
b = Bank()
print(b.ifsc)
# now call m1
b.m1()
print(b.ifsc)
----------------------------------------
# lets try to change static variable using self as a ref.
class Bank:
    ifsc = 'SBI76523' # static var
    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc using self
        self.ifsc = 'PNB45678'
print(Bank.ifsc)
b = Bank()
print(b.__dict__)
b.m1()
print(b.__dict__)
# lets check ifsc using object
print(b.ifsc)
print(Bank.ifsc)
-----------------------------------------
class Bank:
    ifsc = 'SBI76523' # static var
    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc using self
        #Bank.ifsc = 'PNB45678'
        self.ifsc = 'PNB45678'
b1 = Bank()
b1.m1()
print(b1.ifsc)

b2 = Bank()
print(b2.ifsc)
-----------------------------
class Bank:
    print('hello')

    def m1(self):
        print('m1 called')
    def m2(self):
        print('m2 called')

b = Bank()
b.m1()
b.m2()
========================================================================================
IQ:
q1) Differentiate local,global,instance, static variables
ans:
#global, local, static, instance variable.
#global variable are defined at the top of program or defined using keyword:global

global global_var1 = 0
global_var2 = 1

def local_variable:
    #local variable are defined inside of a function.
    local_var1 = 2

class static_instance:
    #static/classs variable are defined inside of a class.
    static_var1 = 3

    def __init__(self):
        #all variables defined in the function of a class starting with self.
        self.instance_var1 = 4

    def static(self):
        self.instance_var2 = 5

        local_var2 = 6         #local variable as it is in a function.
=============================================================================================
Q2)Can we change value of static variable? How?
Ans:- We can modify the value of the static variable anywhere (either within the class or outside the class) by using the
           class name. We cannot modify the static variable value by using the self variable or object reference.
==============================================================================================
Q3:self vs object
Ans:-The difference is that in one case you called the variable that holds the instance self and in another case
          you called it object . That's the only difference. The self variable is explicit in 
          Python, and you can call it whatever you want. self is just the convention everyone uses for readability
=============================================================================================
Q4: method vs constructor
Q5: __init__(self) means what? what is the purpose
Q6:How class gets executed using an object
Q7: How many objects we can create
Q8: Explain call by value and call by reference
Ans:-Call by Value means calling a method with a parameter as value. Through this, the argument value is passed 
          to the parameter. While Call by Reference means calling a method with a parameter as a reference. Through
          this, the argument reference is passed to the parameter.
Q9: Can we delete instance var?
Q10: How we can use className as a ref. variable
Q11: what is self
"""
****************************************************************OPO4.PY*******************************************************************
"""
Bank application using OOP:
"""
import time
class Bank:
    bank_name = 'ICICI BANK'
    # ZERO BALANCE ACCOUNT
    def __init__(self,name,balance = 0.0):
        self.name = name
        self.bal = balance
    def deposit(self,amt):
        self.bal += amt
        time.sleep(2)
        print('Total Balance after credit is Rs.',self.bal)
    def withdraw(self,amt):
        self.bal -= amt
        time.sleep(2)
        print('Total Balance after debit is Rs.', self.bal)
nm = input('Enter your Name:')
b = Bank(nm)
while True:
    print('--------------------------')
    time.sleep(2)
    print('Hello',nm, 'Welcome to',Bank.bank_name)
    print('--------------------------')
    time.sleep(2)
    print('Which operation would you like to perform')
    time.sleep(3)
    print('1.Deposit\n2.Withdraw\n3.Current Balance\n4.Exit')
    time.sleep(2)
    choice = input('Enter your choice:')
    if choice == '1':
        print(nm,'you have selected Credit option')
        time.sleep(2)
        amt = float(input('Please enter amount in Rs.'))
        time.sleep(2)
        b.deposit(amt)
    elif choice == '2':
        print(nm,'you have selected Debit option')
        time.sleep(2)
        amt = float(input('Please enter amount in Rs.'))
        time.sleep(2)
        b.withdraw(amt)
    elif choice == '3':
        print(nm, 'Please wait we are fetching your current balance')
        time.sleep(2)
        print('Your Current Balance is Rs:',b.bal)
    else:
        print(nm,'Thank you for your time')
        print('Visit again...!!!!!')
        #break
        exit()
print('Do the next step....')
for i in range(4):
    print(i)

# Assignment: Create a DMart application
# Assignment: Covid19 registration application

*************************************************************************OP5.PY***********************************************************************
"""
OOP Properties:
Pillars of OOP
- Inheritance
- Encapsulation
- Abstraction
- Polymorphism
-------------------------------
Inheritance:
Building a parent and child relationship
in which we have basically 2 classes
1. Parent class ( Base/root class)
2. Child class ( Derived class)
---------------------------
There are 4 different types of Inheritance:
- Simple/single inheritance
- Multilevel inheritance
- Multiple inheritance
- Hybrid
=====================================
1. Simple inheritance:
-in which we wil have only one parent and one child
- to build a relation we need to inherit Father class in child class
=============================
class Father:
    x = 100
    def money(self):
        print('Money of Father')
class Child(Father):
    pass

c = Child()
c.money()
print(c.x)
==================================
# suppose child class only has money method
# and Father class has x, car method
class Father:
    x = 100
    def car(self):
        print('Fathers car')

class Child(Father):
    def money(self):
        print('Money of Child')

c = Child()
c.money()
c.car()
=========================================
# Multiple inheritance

class Central_gov: # suepr_parent
    def funds(self):
        print("central gov funds")
class State_gov(Central_gov): # Parent
    def s_funds(self):
        print('State gov fund')
    def funds(self):
        print('Central fund in State')
        super().funds()

class Local_gov(State_gov): # child
    pass
l = Local_gov()
l.funds()
l.s_funds()
--------------------------------------
Examples:
Multilevel inheritance:
Super Parent

Parent

child

Multiple inheritance

Father Mother
    child
==============================
# we can use a super() to access members of a super parent or parent
# if tht method or member is already present
# super we can use inside a method
class PM:
    def help(self):
        print('Help from PM')

class CM(PM):
    def help(self):
        print('Help from CM')
        #super().help()
        super(CM, self).help()
class MLA(CM):
    def fund(self):
        print('MLA fund')


m = MLA()
m.fund()
m.help()
=======================================
VVIMP:
Meth-od overriding:
If child and parent contains a method with same name,
so method in child overrides method in parent
and method in parent overriden in child

Overriding is completely a part of inheritance
without inheritance its nt possible
"""
class Father:
    def info(self):
        print('Father info')

class Child(Father):
    def info(self):
        print('Self.info')
        super().
c = Child()
c.info()

******************************************************************OP6.PY*******************************************************
"""
class A:
    def m1(self):
        print('m1 A')

class B(A):
    def m1(self):
        print('m1 B')

class C(B):
    def m2(self):
        super().m1()
        A.m1(self)

c = C()
c.m2()
===============================
class A:
    def m1(self):
        print('m1 A')

class B(A):
    def m1(self):
        print('m1 B')

class C(A):
    def m2(self):
        super().m1()
        A.m1(self)

c = C()
c.m2()

   A
B     C
=========================================
# Multiple inheritance:
We have more than one parent and from these parent we can create a child class
Example:

Mother   Father
     Child

In case of multiple inheritance we must need to folow hierarchy
means class are to be prioritised

This priority we can manage by supplyng parent class sequence
in child class from left to right
-----------------------------
class Mother:
    def m1(self):
        print('Access mother')
    def common(self):
        print('M- common')
class Father:
    def m2(self): print('Access Father')
    def common(self):
        print('F-common')
class Child(Mother,Father):
    def m3(self):
        super().common()
        Father.common(self)
c = Child()
c.m1()
c.m2()
c.common()
c.m3()
=====================================
class Mother:
    def m1(self):
        print('Access mother')
    def common(self):
        print('M- common')
class Father:
    def m2(self): print('Access Father')
    def common(self):
        print('F-common')
class Child(Mother,Father):
    pass
c = Child()
# i want to execute common method from both classes
Father.common(c)
Mother.common(c)
---------------------------------------------

class A:
    def m1(self):
        print('m1-A')
class B:
    def m1(self):
        print('m1-B')
    def m2(self):
        print('m2-B')
class C:
    def m2(self):
        print('m2-C')
class Child(B,A,C):
    pass

ob = Child()
ob.m1() # CLASS B
ob.m2() # class B
==========================
class Mother:
    def m1(self):
        print('Access mother')
    def common(self):
        print('M- common')
class Father:
    def m2(self): print('Access Father')
    def common(self):
        print('F-common')
class Child():
    pass
c = Child()
# i want to execute common method from both classes
# without inheritance also we can access member from other class
Father.common(c)
Mother.common(c)
====================================
class Bank:
    def debit(self):
        print('Debit operation')

#Bank().debit()

#b = Bank()
#b.debit()

sbi = Bank()
Bank.debit(sbi)

hdfc = Bank()
Bank.debit(hdfc)

"""
********************************************************************OP7.PY*******************************************************************
"""
Encapsulation
Means its Data hiding
Members of a program are bind inside a container
-------------------------------------------
class Sample:
    x = 10
    y = 'simba'

    def m1(self):
        pass
# m1() and x,y presents inside a class
# those r nt accessible outside directly
# bcz they are encapsulated inside a container and that container is
# a class
m1()
print(x,y)
s = Sample()
-------------------------------------
Q. What is encapsulation?
---------------------------------------------
Access modifiers: public, private, protected
Public: these variables or methods available anywhere within the program and
to its subclass as well

Private: these variables or methods are available only within the class
outside the class it wont be available

Protected: these variables or methods are available within the same class and to its
subclass


Do we have access modifiers? ==> NO
But we can implement it using _ underscore convention
======================================
class Sample:
    x = 'public'
    _y = 'protected'
    __z = 'private'
    def m1(self):
        print(Sample.__z)
Sample().m1()
class Test:
    print(Sample.x,Sample._y)
    print(Sample._y)
    #print(Sample.__z)
=====================================

class Sample:
    x = 'public' #directly anywhere
    _y = 'protected' # indirectly anywhere
    __z = 'private'
s  = Sample()
print(s.x) #accessible
print(s._y) # accessible indirectly
print(s.__z) # not accessible
======================================
Methods?

class Sample:
    def m1(self):
        print('public method')
    def _m2(self):
        print('Protected method')
    def __m3(self):
        print('Private method')

# try to access using object
s =  Sample()
# public and protected methods will be available
s.m1()
s._m2()
# but private nt
#s.__m3()
=======================================
# Still if i want to access private method outside
then use 'Name Mangling technique'
It is used to store a private variable in dir strcuture
and same is used to access private members outside a class

ex. _className__variableName
    _className__methodName()
============================================
class Sample:
    a = 40
    b = 60
    __x = 'private variable'

    def __m1(self):
        print('Private method')
s = Sample()
#s.__m1()
print(dir(Sample))
print(s._Sample__x)
s._Sample__m1()
==========================================
_m1() __m1()
Q. Differentiate public private protected
Q. Name mangling technique? how to access private member outside a class
########################################################################
Abstraction: Its information hiding
--------------------------------------
Abstraction is associated with class and its methods
Rule:
- In order to make a normal class as an abstract class we need to do 2 things
    1. import ABC(Abstract Base class) class from abc module, then inherit this
    ABC into a normal class
    2. Create an abstract method using asbtractmethod() decorator
"""
from abc import ABC,abstractmethod
class Sample(ABC):

    @abstractmethod
    def m1(self): # an abstract method
        pass
#Rule: we cant create an object of abstract class Sample
class Info(Sample):
    def m1(self):
        print('Implemented Abstract method in Child')
i = Info()
i.m1()
# Rule 2: When we have any abstract method present in abstarct class
# then its implementation must be provided in Child class

*****************************************************************MRO*****************************************************************


























