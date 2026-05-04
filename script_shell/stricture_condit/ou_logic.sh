day="Saturday"
weather="sunny"
if [ "$day" = "Saturday" ] || [ "$day" = "Sunday" ] || [ "$weather" = "sunny" ]
then
    echo "Great day for outdoor activities"
else
    echo "Better stay indoors"
fi
