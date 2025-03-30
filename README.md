# Blog Update Fetching Script

## Introduction

This is an automation script I implemented in the Hexo blog update to automatically fetch blog updates, compare them with previous update statuses, and allow users to manually determine the update status of unfinished and newly added blogs, thus obtaining the new blog update status.

## Preliminaries

Due to the strict formatting requirements of the automation script for the text, please make sure to complete the following modifications before use!

### Modify to your blog directory

In `main.sh`, change the directory into your own directory:

```bash
DIR="/mnt/d/Blog/source/_posts"

# Change this line into your own directory!
```

### Create a new directory

```bash
touch log
```

### Initialize `prev.txt`

You need to initialize `prev.txt` for your own blog!

For this document, please maintain the following format: Each line should include a prefix status emoji and the title name. The prefix status emojis include ✅ and ❌, indicating the completion status of the blog. 

An example text is as follows:  

```
❌AI-Paper-2024
❌AI-indepth-reading-AlexNet
✅Above-All
❌Algorithm-BFS-DFS
✅Algorithm-BinaryTree
❌Algorithm-Chunking
✅Algorithm-Introduction
✅Algorithm-Memo
✅Algorithm-Sorting
✅Bash-commands
✅Bash-exercises
✅C-plus-plus-Primer-Plus-tutorial
✅CMake-tutorial-episode2
✅CMake-tutorial1
✅CS294-1-LLM-Reasoning
```

Please ensure that your output structure maintains alphabetical order. You can use the following command line to achieve this: 

```bash
ls $DIR | grep -v ".*\.md" | grep -v ".*\.sh" > ans.txt
```

You only need to initialize it once! The scripts will update it later.

## Usage

For **Hexo** Blog users, the directory which stores your Blog posts may be like as follows:

- Several `.md` files
- Several directories which has the same name with `.md` files

The `main.sh` will automatically get all file names using the `grep` command:

```bash
ls $DIR | grep -v ".*\.md" | grep -v ".*\.sh" > ans.txt
```

> `grep -v ".*\.sh"` is because I add several `.sh` files into it. You can modify it with your own needs.

Then, the file will compare the new status with the previous status stored in the `prev.txt`. Then the file will ask users to manually determine the update status of unfinished and newly added blogs.

The output log looks as follows:

```bash
Getting updated.
Checking the file exists
File Exists
Getting ready for updated.
Blog 'AI-Paper-2024' finished? (y/n): n
Blog 'AI-indepth-reading-AlexNet' finished? (y/n): n
Blog 'Algorithm-BFS-DFS' finished? (y/n): n
Blog 'Algorithm-Chunking' finished? (y/n): n
Blog 'CS294-3-Autogen' finished? (y/n): n
New Blog 'DataStructure-Fenwick-Tree-Sparse-Table' finished? (y/n): n
Blog 'DataStructure-Tree-Binary-Search-Tree-AVL-Tree' finished? (y/n): n
Blog 'Python-tutorial' finished? (y/n): n
Blog 'Python-visualization' finished? (y/n): n
Blog 'RAG-tutorial' finished? (y/n): n
Blog 'Taking-Notes' finished? (y/n): n
Blog 'Tools-Tutorial' finished? (y/n): n
Update successfully into log/20250330_200559.txt
Overwrite to prev.txt successfully, Done!
Be productive!
```

Finally, the scripts will update `prev.txt` and generate a new blog status named `20250330_200559.txt` and you can see the updated status there!

Demo:

```
❌AI-Paper-2024
❌AI-indepth-reading-AlexNet
✅Above-All
❌Algorithm-BFS-DFS
✅Algorithm-BinaryTree
❌Algorithm-Chunking
✅Algorithm-Introduction
✅Algorithm-Memo
...
✅RAG-Blog-Content-Retrieval
❌RAG-tutorial
✅RL-speeches
✅Regular-Expression
❌Taking-Notes
❌Tools-Tutorial
✅Vim-tutorial
```

**Enjoy Coding**

## Discussion

Just for fun, and just for hexo` users.