#!/usr/bin/python
# ! ATTENTION: change it to your own python interpreter.
import os
import sys
from datetime import datetime

# Configuration
# ! ATTENTION: replace the BLOG_DIR with your own.
BLOG_DIR = "/home/xiyuanyang/Blog/Blog_Main/source/_posts/"
PREV_FILE = "prev.txt"
ANS_FILE = "ans.txt"
LOG_DIR = "log"


def get_blog_posts():
    """Get all markdown files in the blog directory and save their names (without extension) to ans.txt"""
    try:
        # Get all markdown files and sort them alphabetically
        posts = sorted([f[:-3] for f in os.listdir(BLOG_DIR) if f.endswith(".md")])

        # create PREV_FILE if it doesn't exist
        if not os.path.exists(PREV_FILE):
            with open(PREV_FILE, "w") as file:
                pass

        # create ANS_FILE
        with open(ANS_FILE, "w") as f:
            f.write("\n".join(posts))

        return True
    except Exception as e:
        print(f"Error getting blog posts: {e}")
        return False


def load_previous_status():
    """Load previous status from prev.txt"""
    status = {}
    if os.path.exists(PREV_FILE):
        try:
            with open(PREV_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        prefix = line[0]
                        # three emojis: ❌✅⏸️
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
        prompt = (
            f"New Blog '{title}' finished? (y/c/n): "
            if is_new
            else f"Blog '{title}' finished? (y/c/n): "
        )
        user_input = input(prompt).strip().lower()

        if not user_input:
            print("Input empty, enter again")
            continue

        if user_input == "y":
            return f"✅{title}"
        elif user_input == "n":
            return f"❌{title}"
        elif user_input == "c":
            return f"🫡{title}"
        else:
            print("Invalid Input!")


def remove_invisible_chars_encode_decode(text: str):
    """
    Remove invisible characters by encoding and decoding.
    Suitable for removing various non-ASCII or characters that cannot be represented by specific encodings.
    """
    # First encode to UTF-8 bytes (an intermediate step to ensure proper Unicode handling)
    # Then decode to ASCII and ignore characters that cannot be decoded.
    # 'ascii' encoding does not support many non-ASCII characters, including some zero-width and variant selector characters.
    return text.encode("ascii", "ignore").decode("ascii")


def main():
    if not get_blog_posts():
        sys.exit(1)

    if not os.path.exists(PREV_FILE):
        print(f"Error: {PREV_FILE} doesn't exist!")
        sys.exit(1)

    if not os.path.exists(ANS_FILE):
        print(f"Error: {ANS_FILE} doesn't exist!")
        sys.exit(1)

    create_log_dir()

    # Get timestamp for new status file
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    new_status_file = os.path.join(LOG_DIR, f"{timestamp}.txt")

    # Load previous status
    prev_status = load_previous_status()

    # Read current blog posts from ANS_FILE
    current_posts = set()
    try:
        with open(ANS_FILE, "r") as f:
            for line in f:
                title = line.strip()
                if title:
                    current_posts.add(title)
    except Exception as e:
        print(f"Error reading {ANS_FILE}: {e}")
        sys.exit(1)
    
    # Sort the current posts alphabetically before processing them
    sorted_current_posts = sorted(list(current_posts))

    # Identify deleted posts
    deleted_posts = []
    for title in prev_status.keys():
        title = remove_invisible_chars_encode_decode(str(title).strip())
        if title not in current_posts:
            deleted_posts.append(title)

    if deleted_posts:
        print("\n--- Detected Deleted Blog Posts ---")
        for post in deleted_posts:
            print(f"🗑️ Blog '{post}' has been deleted from your blog directory.")
        print("-----------------------------------\n")

    # Process current blog posts and build new_status
    new_status = []
    for title in sorted_current_posts:
        if title in prev_status:
            # Existing blog post
            if prev_status[title] == "✅":
                new_status.append(f"✅{title}")
            else:
                result = get_user_input(title)
                new_status.append(result)
        else:
            # New blog post
            result = get_user_input(title, is_new=True)
            new_status.append(result)

    # Save new status
    try:
        with open(new_status_file, "w") as f:
            f.write("\n".join(new_status))
        print(f"Update successfully into {new_status_file}")
    except Exception as e:
        print(f"Error saving new status file: {e}")
        sys.exit(1)

    # Update prev.txt
    try:
        with open(PREV_FILE, "w") as f:
            f.write("\n".join(new_status))
    except Exception as e:
        print(f"Error updating {PREV_FILE}: {e}")
        sys.exit(1)

    print("\nUpdate complete. Be productive!")


if __name__ == "__main__":
    main()