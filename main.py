#!/usr/bin/env python3
import os
import sys
from datetime import datetime

# Configuration
BLOG_DIR = "/mnt/d/Blog/source/_posts"
PREV_FILE = "prev.txt"
ANS_FILE = "ans.txt"
LOG_DIR = "log"

def get_blog_posts():
    """Get all markdown files in the blog directory and save their names (without extension) to ans.txt"""
    try:
        posts = [f[:-3] for f in os.listdir(BLOG_DIR) if f.endswith('.md')]
        with open(ANS_FILE, 'w') as f:
            f.write('\n'.join(posts))
        return True
    except Exception as e:
        print(f"Error getting blog posts: {e}")
        return False

def load_previous_status():
    """Load previous status from prev.txt"""
    status = {}
    if os.path.exists(PREV_FILE):
        try:
            with open(PREV_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        prefix = line[0]
                        title = line[1:]
                        status[title] = prefix
        except Exception as e:
            print(f"Error reading {PREV_FILE}: {e}")
            sys.exit(1)
    return status

def create_log_dir():
    """Create log directory if it doesn't exist"""
    if not os.path.exists(LOG_DIR):
        try:
            os.makedirs(LOG_DIR)
        except Exception as e:
            print(f"Error creating {LOG_DIR}: {e}")
            sys.exit(1)

def get_user_input(title, is_new=False):
    """Get user input for a blog post"""
    while True:
        prompt = f"New Blog '{title}' finished? (y/n): " if is_new else f"Blog '{title}' finished? (y/n): "
        user_input = input(prompt).strip().lower()
        
        if not user_input:
            print("Input empty, enter again")
            continue
        
        if user_input == 'y':
            return f"✅{title}"
        elif user_input == 'n':
            return f"❌{title}"
        else:
            print("Invalid Input!")

def main():
    print("Getting updated.")
    
    if not get_blog_posts():
        sys.exit(1)
    
    print("Checking the file exists")
    
    if not os.path.exists(PREV_FILE):
        print(f"Error: {PREV_FILE} doesn't exist!")
        sys.exit(1)
    
    if not os.path.exists(ANS_FILE):
        print(f"Error: {ANS_FILE} doesn't exist!")
        sys.exit(1)
    
    create_log_dir()
    print("File Exists")
    
    # Get timestamp for new status file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_status_file = os.path.join(LOG_DIR, f"{timestamp}.txt")
    
    print("Getting ready for updated.")
    
    # Load previous status
    prev_status = load_previous_status()
    
    # Process current blog posts
    new_status = []
    
    try:
        with open(ANS_FILE, 'r') as f:
            for line in f:
                title = line.strip()
                if not title:
                    continue
                
                if title in prev_status:
                    if prev_status[title] == "✅":
                        new_status.append(f"✅{title}")
                    else:
                        result = get_user_input(title)
                        new_status.append(result)
                else:
                    result = get_user_input(title, is_new=True)
                    new_status.append(result)
    except Exception as e:
        print(f"Error processing {ANS_FILE}: {e}")
        sys.exit(1)
    
    # Save new status
    try:
        with open(new_status_file, 'w') as f:
            f.write('\n'.join(new_status))
        print(f"Update successfully into {new_status_file}")
    except Exception as e:
        print(f"Error saving new status file: {e}")
        sys.exit(1)
    
    # Update prev.txt
    try:
        with open(PREV_FILE, 'w') as f:
            f.write('\n'.join(new_status))
        print("Overwrite to prev.txt successfully, Done!")
    except Exception as e:
        print(f"Error updating {PREV_FILE}: {e}")
        sys.exit(1)
    
    print("Be productive!")

if __name__ == "__main__":
    main()