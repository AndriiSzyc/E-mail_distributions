#!/bin/bash

git add .

echo "Enter message"
read message

git commit -m '"$read"'

git push
