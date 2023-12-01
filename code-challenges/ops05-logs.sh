#!/bin/bash

# Script Name:                  ops05-logs.sh
# Author:                       Krystal Reid
# Date of latest revision:      12/01/2023
# Purpose:                      clearing logs
# Execution                     bash ops05-logs.sh or ./ops05-logs.sh or chmod +x ops05-logs.sh
# Citations:                    ops301 repo https://github.com/codefellows/seattle-ops-301d14/blob/main/class-05/challenges/ASSIGNMENT.md, [ChatGPT](https://chat.openai.com/share/a039d9e6-30af-42ec-bf99-4a1f0064edbe)

# Identify variables: log files, backup directory, and timestamp
logfiles=("/var/log/syslog" "/var/log/wtmp")
backupdir="/var/log/backups/"
timestamp=$(date "+%Y%m%d%H%M%S")

# Print to the screen the file size of the log files before compression
print_file_size(){
    file=$1
    size=$(du -h "$file" | awk '{print $1}')
    echo "File size of $file: $size"
}

# Creating a backup directory if it doesn't already exist
mkdir -p $backupdir

# Compress the contents of the log files listed below to a backup directory - the file name should contain a time stamp
compress_log_file() {
    file=$1
    compressed_file="$backupdir/$(basename "$file")-$timestamp.zip"
    gzip -c "$file" > "$compressed_file"
    echo "Compressed $file to $compressed_file"
    print_file_size "$compressed_file"
    print_compressed_file_size "compressed_file"

    # Compare the size of the compressed files to the original log files.
    ogsize=$(du -h "$file" | awk '{print $1}')
    compressedsize=$(du -h "$compressed_file" | awk '{print $1}')
    echo "Compare the OG size: $ogsize to the compressed size: $compressedsize"
}

# Clear the contents of the log file
clear_log_file() {
    file=$1
    echo "" > "$file"                              
    echo "Contents of $file has been cleared."
}
