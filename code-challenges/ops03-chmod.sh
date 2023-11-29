#!/bin/bash

# Script Name:                  ops03-chmod.sh
# Author:                       Krystal Reid
# Date of latest revision:      11/28/2023
# Purpose:                      changing file permissions
# Execution                     bash ops03-chmod.sh or ./ops03-chmod.sh or chmod +x ops03-chmod.sh
# Citations:                    ops301 repo https://github.com/codefellows/seattle-ops-301d14/, ChatGPT https://chat.openai.com/share/4a673f8d-61e2-4822-a588-989e77df4c49

# Prompts user for input directory path
echo "Please enter the path to the directory:"
read -r input_directory

# Prompt the user for the permissions number
echo "Please enter the permissions number:"
read -r permissions_number

# Navigate to the directory input by the user and the files within to input setting
cd "input_directory"
chmod -R "permissions_number" *

# Print the contents of the directory and the new permission settings for what is in the directory
echo "Contents of the directory:"
ls -l

echo "New permission settings:"
ls -l | awk '(print $1, $9)

