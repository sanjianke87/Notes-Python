#!/bin/bash

conda update conda
conda update anaconda
conda update --all
conda config --add channels obspy
conda install obspy
conda install pylint

cat << EOF > requirements.txt
ghp-import
thefuck
autopep8
EOF
pip install -r requirements.txt
rm requirements.txt
