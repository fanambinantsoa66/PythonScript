#!/bin/bash
while true
do 
 echo "enter 'quit' to exit"
 read input
 if [ "$input" = "quit" ]
 then
   break 
 fi
 echo "enter $input"
done

