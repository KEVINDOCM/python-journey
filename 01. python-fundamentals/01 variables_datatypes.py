"""
Docstring for 01. python-fundamentals.variables_datatypes
title   : Learn basic variable and data type.
concept : understanding how python stores in memory and handles
dynamic typing.
=================================================================
This script demonstrates:
1. Name conventions (snake case)
2. Different data type(string, int, float, bool)
3. type conversion (casting)
4. formatted-string method
"""

#BASIC VARIABLE (INT,STR,FLOAT):

name:str = "John Doe"
age:int = 15
city:str = "New York"
status:str = "Student"
balance_usd:float = 2600
is_license = False



#CHECKING VARIABLE TYPE DATA
print("CHECKING CLASS DATA TYPE")
print("=" *20) #ignore
print(type(name))              #<class 'str'>
print(type(age))               #<class 'int'>
print(type(city))              #<class 'str'>
print(type(status))            #<class 'str'>
print(type(balance_usd))      #<class 'float'>
print(type(is_license))        #<class 'bool'>
print("=" *20) #ignore



#TYPE CONVERSION (CASTING)
print("CONVERSION TYPE")
print("=" *20) #ignore
ballance_usd_string = str(balance_usd)     #>Create a new variable and change the data type to string
print(type(ballance_usd_string))

#f-string / FORMATED STRING METHOD
print("FORMATED STRING")
print("=" *20)
print(f"Hello, my name is {name}, I am 15 years old and I come from {city}.\nI am a diligent {status} with an allowance of ${balance_usd:,.2f}. Do I have a driver's license? {is_license}.")






