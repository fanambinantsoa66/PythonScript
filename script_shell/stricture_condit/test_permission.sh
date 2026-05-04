script_file="./username.sh"

if [ -f "$script_file" -a -x "$script_file" ]
then
    echo "Running deployment script..."
    ./"$script_file"
else
    echo "Deploy script not found or not executable"
fi
