#!/bin/bash
echo "Quelle est le fruit que vous aime,on donne son couleur"
read fruit

case $fruit in
    "apple")
        echo "Red or green fruit"
        ;;
    "banana")
        echo "Yellow curved fruit"
        ;;
    "orange")
        echo "Citrus fruit"
        ;;
    *)
        echo "Unknown fruit"
        ;;
esac
