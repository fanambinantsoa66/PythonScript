#!/bin/bash
while [ ! -f "while1.sh" ]
do
  echo "Waiting for while1.sh to apear "
  sleep 100
done
echo "file found while1.sh! and this is their's content 😂😂: "
./while1.sh
