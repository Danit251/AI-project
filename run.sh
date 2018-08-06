#!/bin/bash

echo "Installing necessary packages"
python -m pip install --upgrade pip==9.0.3
python install_packages.py requirements.txt
echo "Done installing"

echo "Run project file"
python author_auth.py
echo "result"
sleep 100


