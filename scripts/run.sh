#!/bin/bash

handle_interrupt() {
    echo -e "\nOperation cancelled by user."
    exit 1
}

trap handle_interrupt SIGINT

echo "Current time: $(date)"

if python src/main.py; then
    # cat prev.txt
    echo "Done"
else
    echo "Error: Python program failed to execute."
    exit 1
fi

# run update_readme.py
python src/update_readme.py

