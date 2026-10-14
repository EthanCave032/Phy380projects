#!/bin/bash

read -p "Enter the first integer: " first
read -p "Enter the second integer: " second

if [ "$first" -gt "$second" ]; then
    echo "$first"
elif [ "$second" -gt "$first" ]; then
    echo "$second"
else
    echo "these numbers are the same"
fi
