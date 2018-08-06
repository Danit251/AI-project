#!/bin/bash

python author_auth.py
echo "result"
sleep 100

echo "installing necessary packages"
python -m pip install --upgrade pip==9.0.3
python install_packages.py requirements.txt
echo "done installing"