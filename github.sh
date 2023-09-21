#!/bin/bash

git add .

echo "Enter message"
read message

git commit -m "$message"

git push
