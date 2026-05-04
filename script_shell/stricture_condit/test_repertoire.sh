#!/bin/bash
backup_dir="/home/fanamby/script_shell/stricture_condit/Kind"

if [ -d "$backup_dir" ]
then
    echo "Kind directory exists"
else
    echo "Creating Kind directory..."
    mkdir -p "$backup_dir"
fi
