#!/bin/bash -ex

VIRT='https://pypi.python.org/packages/source/v/virtualenv/virtualenv-12.1.1.tar.gz'

mkdir -p .bootstrap

wget $VIRT -O .bootstrap/virtualenv.tar.gz

tar xfv .bootstrap/virtualenv.tar.gz -C .bootstrap/
./.bootstrap/virtualenv*/virtualenv.py ./.bootstrap/virt

sudo apt-get install -y gcc python-dev

source ./.bootstrap/virt/bin/activate
pip install -r requirements.txt
