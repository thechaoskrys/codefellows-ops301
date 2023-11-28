#!/bin/bash

# Script Name:                  ops2-append.sh
# Author:                       Krystal Reid
# Date of latest revision:      11/28/2023
# Purpose:                      copy /var/log/syslog to current working dir. appends the current date & time to filename.
# Execution                     bash ops2-append.sh or ./ops2-append.sh or chmod +x ops2-append.sh
# Citations:                    roger's class demo, class repo and chatgpt for understanding https://chat.openai.com/share/86471729-3376-4877-8050-64747257f990

# copy syslog to the current directory
cp /var/log/syslog .

# Declaration of Variables
current_datetime=$(date +"%Y%m%d_%H%M%S")

# Append date and time to filename
syslogfile="syslog_${current_datetime}.log"
mv syslog "$syslogfile"

# Main
echo "File copied to $syslogfile"
# End