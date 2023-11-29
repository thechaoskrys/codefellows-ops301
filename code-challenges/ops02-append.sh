#!/bin/bash

# Script Name:                  ops2-append.sh
# Author:                       Krystal Reid
# Date of latest revision:      11/28/2023
# Purpose:                      copy /var/log/syslog to current working dir. appends the current date & time to filename.
# Execution                     bash ops2-append.sh or ./ops2-append.sh or chmod +x ops2-append.sh
# Citations:                    [roger's class demo](https://zoom.us/rec/play/U6JEPIz5wCjE_YE-VDMa6U6Gpj3AP3jBPICRxkdkTfkhl3is1gJYs5njMjoQkCF9cXF7P1QA8KpTlZMh.fFMgazytyshoSpjA?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FvusFAfXto0iremz2jIq__2uAiIdCm9aOiMDug11YUbCEtbyZpFgsNADj_7tRaCln.O_I7iduaD2Q8Xpyg), class repo and chatgpt for understanding https://chat.openai.com/share/86471729-3376-4877-8050-64747257f990

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
