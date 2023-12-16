#!/usr/bin/env python3

# Script Name:                          ops09-boolean.py
# Author name:                          Krystal Reid
# Date of latest revision:              12/16/2023
# Purpose:                              python collections 
# Execution:                            python3 ops09-boolean.py
# Additional Resources                  https://chat.openai.com/share/f6f0fe94-6113-4a40-ab9f-1c3252cbe125

'''
Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

Create an if statement that includes both elif and else to execute when both if and elif are not met.
'''

# Sample values for a and b
a = 5
b = 10

# Equals: a == b
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Not Equals: a != b
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# Less than: a < b
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# Less than or equal to: a <= b
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is greater than b")

# Greater than: a > b
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Greater than or equal to: a >= b
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is less than b")

# If statement with logical condition of your choice and elif
if a % 2 == 0:
    print("a is an even number")
elif a % 2 != 0:
    print("a is an odd number")
else:
    print("This should not happen!")

# If statement with both elif and else
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
