'''
Flow control blocks:
1. Selective/Conditional statements
- if <condition>: [we can check only 1 codition]
- if <condition>: [We can check 2 conditions]
    tasks1
  else:
    task2
if is condition based , else is conditionless
------------
if 2 == 6:
    print('If block')
else:
    print('Else block')
--------------
if we put  a condition after else then syntactically its invalid
-----------------------------
- if we want to test 3 conditions on single input
Example: temp [high,medium,low]
----------------------
temp = float(input('Enter the current temp:'))
if temp > 40:
    print('Its High Temp')
elif temp > 25:
    print('Its medium Temp')
else:
    print('Its low temp')
==========================
Multiple elif are allowed
# Example if we want to test percentage
[Distinction,1st class,2nd class.....]
Use of multiple elif is called
as elif ladder
----------------------------
name= input('ENter your name:')
per = float(input('Enter the percentage:'))
if per >= 75:
    print(name,'you got distinction')
elif per >= 65:
    print(name,'you got First class')
elif per >= 55:
    print(name,'you got Second class')
elif per >= 45:
    print(name,'you got Pass class')
else:
    print(name,'sorry you are fail')
=============================
Nested if:
if inside if is a nested if
in this, we need to test multiple
dependant conditions
===============
Scenario:
age> 65 and Female 1,2,
age> 65 and male   3,4
========================
age = int(input('Enter your age:'))
gender = input('Enter gender (Male/Female):')
if age > 65:
    if gender == 'female':
        print('you can select Seat 1,2')
    else:
        print('You can select Seat 3,4')
============================
Assignment: Solve 20 new problems base on
elif
elif ladder
nested if
-------------------------------------
at a time u want to check 2 coniditions
then:-
------------------------
citizen = input('Enter ur citizenship(indian/other):')
age = int(input('Enter the age:'))
# if indian age > 18 (adult) allow voting
if (citizen == 'indian') and (age>18):
    print('You are elegible for voting')
else:
    print('Wait for few more years/months')
=======================================
##################################
2. Iterative stetements:
- for loop
it performs iteration over the sequence
Example:
[10,20,30]--> for loop will fetch one element
at a time from this list
10
20
30
Syntax:
for variable in sequence:
    print()
    or
    logic u can use
-----------------------
candidates = ['vaibhav','amol','arti','swarupa','vishal']
for name in candidates:
    print(name,end=' ')
--------------------------
# i wwant to fetch name start with a
candidates = ['vaibhav','amol','arti','swarupa','akshay']
for n in candidates:
    if n.startswith('a'):
        print(n)
---------------------------
- while loop

'''












        
    

   










    















        

























