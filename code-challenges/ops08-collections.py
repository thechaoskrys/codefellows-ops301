#!/usr/bin/env python3

# Script Name:                          ops08-collections.py
# Author name:                          Krystal Reid
# Date of latest revision:              12/16/2023
# Purpose:                              python collections 
# Execution:                            python3 ops08-collections.py
# Additional Resources                  https://chat.openai.com/share/82b7fb01-e0c4-4d5e-b97e-afbc2dd60510

'''
Create a Python script that includes the following:

Assign to a variable a list of ten string elements.
Print the fourth element of the list.
Print the sixth through tenth element of the list.
Change the value of the seventh element to “onion”.
'''

# Creating a list of ten string elements
ten_elements = ["apricot", "blackberry", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Printing the fourth element of the list
print("fourth element of the list:", ten_elements[3])

# Printing the sixth through tenth elements of the list
print("sixth to tenth elements of the list:", ten_elements[5:])

# Changing the value of the seventh element to "onion"
ten_elements[6] = "onion"
