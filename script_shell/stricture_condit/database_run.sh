#!/bin/bash
db_running=false
connected=true

if [[ $db_running == true ]] && [[ $connected == true ]]
then
    echo "Ready to process data"
else
    echo "System not ready - checking individual components"
    [[ $db_running == false ]] && echo "Database is down"
    [[ $connected == false ]] && echo "Network connection lost"
fi
