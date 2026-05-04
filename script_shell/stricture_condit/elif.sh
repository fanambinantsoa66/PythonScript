score=85

if [ $score -ge 90 ]
then
    echo "Grade: A"
elif [ $score -ge 80 ]
then
    echo "Grade: B"
elif [ $score -ge 70 ]
then
    echo "Grade: C"
else
    echo "Grade: F"
fi
