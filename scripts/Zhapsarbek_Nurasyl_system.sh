#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Nurasyl"
echo "Surname: Zhapsarbek"
echo "Group: IT2-2308"
echo "Student ID: 37841"

echo "=============================="
echo "System Information"
echo "=============================="
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -a)"

echo "Disk Usage:"
df -h .

echo "Memory Usage:"
free -h

echo "=============================="
if [ -f "Zhapsarbek_Nurasyl_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
