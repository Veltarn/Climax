#! /bin/bash

echo "Cleaning .pyc files"
find . -name "*.pyc" -exec rm -f {} \;
echo "Done"
