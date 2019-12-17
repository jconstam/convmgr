#!/bin/bash

if [ ! -e "venv/" ]; then
    echo "Creating venv"
    python3 -m venv venv/
fi
echo "Activating venv"
source venv/bin/activate
echo "Installing module"
pip install -e .
echo "Running tests"
pytest