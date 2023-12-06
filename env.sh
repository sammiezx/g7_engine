#!/bin/bash

activate_virtualenv() {
    if [ -d "env" ]; then
        echo "Using 'env' as the virtual environment source."
        source env/bin/activate
    else
        echo "Error: 'env' directory not found. Please create a virtual environment first."
        exit 1
    fi
}

deactivate_virtualenv() {
    deactivate
}

if [ "$1" == "freeze" ] || [ "$1" == "sth" ]; then
    activate_virtualenv

    pip freeze > requirement.txt
    echo "Freezing dependencies to requirement.txt"

    deactivate_virtualenv

elif [ "$1" == "load" ]; then
    activate_virtualenv

    pip install -r requirement.txt
    echo "Installing dependencies from requirement.txt"

    deactivate_virtualenv

else
    echo "Error: Invalid argument. Please use 'freeze' or 'load'"
    exit 1
fi

echo "Script completed successfully."
