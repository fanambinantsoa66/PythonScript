#!/bin/bash
answer=""
until [ "$answer" = "stop" ]
do
    echo "Type 'stop' to exit:"
    read answer
    echo "You typed: $answer"
done
echo "Loop finished!"

