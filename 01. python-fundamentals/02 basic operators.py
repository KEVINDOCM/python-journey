"""
Docstring for 01 python-fundamentals.02 basic operators
title   : Basic operator
date    : 2026-02-1
concept : understanding how python Operators. are special symbols used to perform operations on values or variables.
In other words, operators are “tools” that tell Python what to do with data.
=================================================================
"""

# ADD AND SUBTRACT
print("ADD AND SUBTRACT METHOD")
print("=" *20)
first:int = 8
second:int = 2
add = first + second
subtract = first - second
print(f"RESULT:> {first } + {second} = {add}")
print(f"RESULT:> {first} - {second} = {subtract}")
print("=" *20)

#MULTIPLICATION AND DIVIDE
#NOTE TIPS: Division and multiplication always produce decimal or float data types.
print("MULTIPLICATION AND DIVIDE")
a_num:float = 8
b_num:float= 4
print(f"RESULT:> {a_num} * {b_num} = {a_num * b_num}")
print(f"RESULT:> {a_num} / {b_num} = {a_num / b_num}")
print("=" *20)

#MODULUS
print("MODULUS")
x_num = 10
y_num = 5
print(f"RESULT:> {x_num} % 3 = {x_num % 3}")
print("=" *20)

#EXPONENTIAL
print("EXPONENTIAL")
print(f"RESULT:> {x_num} **3 = {x_num**3}")
print("=" *20)

#LOGICAL OPERATOR
# and    :   Returns True if both statements are true
# or	 :   Returns True if one of the statements is true
# not	 :   Reverse the result, returns False if the result is true
print("LOGICAL OPERATOR")
print(y_num > 0 and y_num < 10)
print(x_num < 5 or x_num > 10)
print(not(x_num > 3 and x_num < 10))
print("=" *20)

#EXCERCISE
celcius_is =37
farenheit_is = (celcius_is * 9/5) + 32
print(farenheit_is)

farenheit = 32
celcius = (farenheit - 32 ) * 5/9
print(celcius)


