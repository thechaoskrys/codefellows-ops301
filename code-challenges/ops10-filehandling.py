#!/usr/bin/env python3

# Script Name:                          ops10-filehandling.py
# Author name:                          Krystal Reid
# Date of latest revision:              12/16/2023
# Purpose:                              python collections 
# Execution:                            python3 ops10-filehandling.py
# Additional Resources                  https://chat.openai.com/share/48a95b8e-a894-4b76-b33d-6617dbf4dfda

'''
Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.

Export your pfSense configuration.
Have your Python script open the exported file.
Code up your script to change a value inside the file.
Save the changes out to a new file name.
Re-import the modified configuraiton file, to verify that your changes will be accepted by pfSense.
'''

# Step 1: Create a new .txt file and append three lines
with open('example.txt', 'w') as file:
    file.write('This is line 1\n')
    file.write('This is line 2\n')
    file.write('This is line 3\n')

# Step 2: Print the first line to the screen
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print('First Line:', first_line)

# Step 3: Delete the .txt file
import os
os.remove('example.txt')
print("File has been deleted!")

# Stretch Goals

# Step 4: Open the exported configuration file
with open('exported_config.xml', 'r') as config_file:
    config_content = config_file.read()

# Step 5: Change a value inside the file (e.g., replace 'old_value' with 'new_value')
new_config_content = config_content.replace('old_value', 'new_value')

# Step 6: Save the changes to a new file
with open('modified_config.xml', 'w') as modified_file:
    modified_file.write(new_config_content)

# Explanation from ChatGPT - I did not fully understand this part and it was not configured to match MY pfSense
#   open('exported_config.xml', 'r'): Opens the exported configuration file in read mode.
#   config_file.read(): Reads the content of the file.
#   replace('old_value', 'new_value'): Modifies the content as needed.
#   open('modified_config.xml', 'w'): Opens a new file in write mode.
#   modified_file.write(new_config_content): Writes the modified content to the new file.
    