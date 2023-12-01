#!/bin/bash

# Script Name:                  ops05-logs.sh
# Author:                       Krystal Reid
# Date of latest revision:      12/01/2023
# Purpose:                      clearing logs
# Execution                     bash ops05-logs.sh or ./ops05-logs.sh or chmod +x ops05-logs.sh
# Citations:                    ops301 repo https://github.com/codefellows/seattle-ops-301d14/blob/main/class-05/challenges/ASSIGNMENT.md

# Identify variables: log files
log_files=("/var/log/syslog" "/var/log/wtmp")

# Print to the screen the file size of the log files before compression
