#!/bin/bash

# Auto scripts for getting Blog posts

# Using Diff and Git merge for getting updated for Blog posts

DIR="/mnt/d/Blog/source/_posts"

echo "Getting updated."

ls $DIR | grep ".*\.md" | sed 's/\.md$//' > ans.txt

# define directory
PREV_FILE="prev.txt"
ANS_FILE="ans.txt"
LOG_DIR="log"

echo "Checking the file exists"

# check whether the file exists
if [[ ! -f "$PREV_FILE" ]]; then
    echo "Error: $PREV_FILE doesn't exist!"
    exit 1
fi

if [[ ! -f "$ANS_FILE" ]]; then
    echo "Error: $ANS_FILE doesn'y exist!"
    exit 1
fi

if [[ ! -d "$LOG_DIR" ]]; then
    echo "Creating $LOG_DIR..."
    mkdir -p "$LOG_DIR"
    if [[ $? -ne 0 ]]; then
        echo "Error, cannot to create $LOG_DIR！"
        exit 1
    fi
fi

echo "File Exists"

# Getting time stamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
NEW_STATUS_FILE="$LOG_DIR/$TIMESTAMP.txt"

# Create a new file
touch "$NEW_STATUS_FILE"
if [[ $? -ne 0 ]]; then
    echo "Error, could not establish $NEW_STATUS_FILE！"
    exit 1
fi

echo "Getting ready for updated."

# read prev.txt and stores it as an array
declare -A prev_status
while IFS= read -r line; do
    # Get the title
    prefix="${line:0:1}"
    title="${line:1}"
    prev_status["$title"]="$prefix"
done < "$PREV_FILE"

# Read ans.txt
exec 3< "$ANS_FILE"  # Use 3 for reading the file
while IFS= read -r -u 3 title; do
    if [[ -n "${prev_status[$title]}" ]]; then
        # if the title exists
        if [[ "${prev_status[$title]}" == "✅" ]]; then
            # ✅ remains unchanged
            echo "✅$title" >> "$NEW_STATUS_FILE"
        else
            # ❌ ask for users
            while : ; do
                echo -n "Blog '$title' finished? (y/n): "
                read -r user_input
                user_input=$(echo "$user_input" | tr -d '[:space:]')
                if [[ -z "$user_input" ]]; then
                    echo "Input empty, enter again"
                    continue
                fi
                case "$user_input" in
                    y|Y)
                        echo "✅$title" >> "$NEW_STATUS_FILE"
                        break
                        ;;
                    n|N)
                        echo "❌$title" >> "$NEW_STATUS_FILE"
                        break
                        ;;
                    *)
                        echo "Invalid Input!"
                        ;;
                esac
            done
        fi
    else
        # For new blog
        while : ; do
            echo -n "New Blog '$title' finished? (y/n): "
            read -r user_input
            user_input=$(echo "$user_input" | tr -d '[:space:]')
            if [[ -z "$user_input" ]]; then
                echo "Input empty, enter again"
                continue
            fi
            case "$user_input" in
                y|Y)
                    echo "✅$title" >> "$NEW_STATUS_FILE"
                    break
                    ;;
                n|N)
                    echo "❌$title" >> "$NEW_STATUS_FILE"
                    break
                    ;;
                *)
                    echo "Invalid Input"
                    ;;
            esac
        done
    fi
done
exec 3<&- 

echo "Update successfully into $NEW_STATUS_FILE"

# Update prev.txt

cat $NEW_STATUS_FILE > prev.txt

echo "Overwrite to prev.txt successfully, Done!"

echo "Be productive!"
