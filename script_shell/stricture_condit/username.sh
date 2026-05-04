#!/bin/bash

username="fanamby"
# password attendu (décommenter si besoin)
# expected_pass="mypaswd123"

# Vérification du nom d'utilisateur
if [ "$username" = "fanamby" ]; then
    echo "Administrator access granted"
fi

if [ "$username" != "guest" ]; then
    echo "Full privileges available"
fi

echo -n "Enter password : "
read -r passwd

# Vérification de la longueur du mot de passe
if [[ ${#passwd} -ge 8 ]]; then
    echo "Password length is acceptable"
else
    echo "Password is too short (minimum 8 characters)"
fi

# Optionnel : vérifier le mot de passe exact (décommenter si besoin)
# if [ "$passwd" = "$expected_pass" ]; then
#     echo "Password is correct"
# else
#     echo "Incorrect password"
# fi
