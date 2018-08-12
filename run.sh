#!/bin/bash

echo "Installing necessary packages"
python3 -m pip install --user --upgrade pip==9.0.3
python3 install_packages.py requirements.txt
echo "Done installing"

echo "Run project file"
python3 author_auth.py
echo "result"


