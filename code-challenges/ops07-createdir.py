#!/usr/bin/env python3

# Script Name:                          ops07-createdir.py
# Author name:                          Krystal Reid
# Date of latest revision:              12/16/2023
# Purpose:                              directory creation
# Execution:                            python3 ops07-createdir.py
# Additional Resources                  https://chat.openai.com/share/9137862f-ad7b-417d-a800-41287f712a25

'''
Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

Script must ask the user for a file path and read a user input string into a variable.
Script must use the os.walk() function from the os library.
Script must enclose the os.walk() function within a python function that hands it the user input file path.
'''
# Import libraries
import os

# Declaration of functions
def generate_directory_structure(user_path):
    for (root, dirs, files) in os.walk(user_path):
        # Print the current root directory
        print("==root==")
        print(root)
        
        # Print the sub-directories in the current root
        print("==dirs==")
        print(dirs)
        
        # Print the files in the current root
        print("==files==")
        print(files)

# Main
if __name__ == "__main__":
    # Declaration of variables
    user_input = input("Enter a directory path: ")

    # Pass the variable into the function
    generate_directory_structure(user_input)
