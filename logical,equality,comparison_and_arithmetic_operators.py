# -*- coding: utf-8 -*-
"""Logical,Equality,Comparison and Arithmetic Operators.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mNdl79kMhV-xIovvs6wpCgpewFeTMlX5

Python Operators



*   Logical
*   Equality
*   Comparision
*   Arithmetic
"""

type(False)

bool(1)

a = True
b = False

True and False

True or False

not True

age =int(input("Enter the age"))
if age > 18 and age <=35:
  print("Mid age")

age =int(input("Enter the age"))
if age <18 or age>=35:
  print("Succesful execution")

#Equality
a ='krish'
b ='krish'

a==b

age=int(input("enter the age"))

if age == 18:
  print("you are in the teenager age")

a='krish'
b='krish'
print(id(a))
print(id(b))

a is b

lst=[1,2,3]
lsdt1=[1,2,3]
print(id(lst))
print(id(lsdt1))

lst is lsdt1

lst is not lsdt1

'krish'!='Krish'

#Comparision
marks = float(input("Enter the marks"))

if marks>35:
  print("Pass")
  if marks >= 50 and marks <= 70:
   print("First")
elif marks<35:
  print("Fail")

#Arithmetic
24+24

12-24

45*65

48/4

46//2

53%2