# Script Name:                          ops06-bash.py
# Author name:                          Krystal Reid
# Date of latest revision:              12/16/2023
# Purpose:                              bash prompts in python
# Execution:                            python3 ops06-bash.py
# Additional Resources                  https://chat.openai.com/share/6ba3377b-9b6f-4d84-9765-3fc3387fa5d9

'''
In Ubuntu, create a Python script that executes a few bash commands successfully. Indicate in comments how you achieved this.

Requirements:

The Python module “os” must be utilized.
At least three variables must be declared and referenced in Python.
The Python function print() must be used at least three times.
Include execution of the following bash commands inside your Python script:

whoami
ip a
lshw -short

'''
# Import the os module
import os

# Declare three variables
user_name = os.getenv('USER')
ip_address = os.popen('ip a | grep inet | grep -v 127.0.0.1 | awk \'{print $2}\' | cut -d"/" -f1').read().strip()
hardware_info = os.popen('lshw -short').read()

# Print variable values
print(f"Username: {user_name}")
print(f"IP Address: {ip_address}")

# Execute and print the result of bash commands
print("\nExecuting 'whoami' command:")
os.system("whoami")

print("\nExecuting 'ip a' command:")
os.system("ip a")

print("\nExecuting 'lshw -short' command:")
print(hardware_info)
