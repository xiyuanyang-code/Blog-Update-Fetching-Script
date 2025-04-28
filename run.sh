#!/bin/bash

handle_interrupt() {
    echo -e "\nOperation cancelled by user."
    exit 1
}

trap handle_interrupt SIGINT

echo "Current time: $(date)"

if python main.py; then
    cat prev.txt
else
    echo "Error: Python program failed to execute."
    exit 1
fi

echo "Finished."
