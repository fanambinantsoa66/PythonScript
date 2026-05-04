#!/bin/bash
if [ ! -f "important_file.txt" ]; then
  echo "error: Required file not found"
  exit 1
fi
echo "file found continuing..."
exit 0
