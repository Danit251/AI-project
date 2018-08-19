#!/bin/bash

ARGS_LIST=$1

echo "Installing necessary packages"
python3 -m pip install --upgrade pip==9.0.3
python3 dependencies/install_packages.py dependencies/requirements.txt
echo "Done installing"

echo "Run project file"
python3 author_auth.py $ARGS_LIST
echo "Output results to results.txt"
sleep 50


