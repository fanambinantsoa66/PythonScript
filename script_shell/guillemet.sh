#!/bin/bash
# Comparaison des types de guillemets
path="/home/user"

echo "Your home directory path is $path"
# Your home directory path is /home/user

echo 'Your home directory path is $path'
# Your home directory path is $path
price="it coasts \$50"
echo "$price"
message='He said "Hello tamby"'
echo "$message"
file_pah="/path/with spaces/guillemet.sh"
echo "$file_path"
filename="guillemet.sh"
cat "$filename"  #Correcte 
cat '$filename' #incorrecte

