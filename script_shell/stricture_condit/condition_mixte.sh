#!/bin/bash
filename="test_permission.sh"
if [[ -f "$filename" && -r "$filename" && ${#filename} -gt 5 ]]
then
    echo "File exists, is readable, and has a descriptive name"
    cat "$filename"
else
    echo "File doesn't meet processing requirements"
fi
