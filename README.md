# Blog Update Fetching Script

## My Blog Updating Status

<!-- BEGIN -->
```text
✅Modern-C
✅DataStructure-Splay-Tree
✅Leetcode-Mistake-collection-11-20
✅DataStructure-Graph-Introduction
✅C-plus-plus-Primer-Plus-tutorial
✅AIBasis-Neural-Networks
✅Torch-Memo-Tensor-Operations
✅Taking-Notes
✅Regular-Expression
✅My-Multi-Agents
✅Linux-Bash-Introduction
✅Python-numpy-cheatsheet
✅Javascripts-Memo
✅DataStructure-Graph-AOE-and-AOV-Network
✅CS294-3-Autogen
✅Leetcode-Mistake-collection-1-10
✅Python-Pipe
✅Python-visualization
✅DataStructure-Tree-Binary-Search-Tree
✅Above-All-en
✅Python-Architecture-Patterns
✅DataStructure-Set
✅My-WorkFlow
✅WSL-Proxy
✅Algorithm-BinaryTree
✅Docker-Tutorial
✅Blog-Word-Counter
✅DataStructure-Stack
✅Imagenet
✅Python-Architecture-Patterns-Multi-file-Progarmming
✅Pythonic-Functional-Programming
✅DataStructure-AVL-Tree
✅DataStructure-Tree-Binary-Heap
✅Algorithm-Memo
✅Python-cheatsheet
✅hello-world
⏸️LLML-CS336-Lecture-1-Overview-and-Tokenization
✅DataStructure-Disjoint-Set
✅Torch-Memo-TensorBoard
✅Python-Threadings
✅DataStructure-Queue
✅CamelAI-automatic-essay-modification
✅Linked-List-Implementation-Based-on-Structs
✅Leetcode-Mistake-collection-31-40
✅DataStructure-Segment-Tree
✅Vim-tutorial
✅LLML-Attention
✅DataStructure-Hash-Table
✅DataStructure-RBT-Tree
✅Algorithm-MCTS
✅Python-File-Management
✅Automaton-NFA
✅RAG-Blog-Content-Retrieval
✅Feishu-GPU-Auto-Monitoring
✅Introduction-to-OOP
✅Blog-Update-Fetching-Script
❌DataStructure-Graph-Network-Flow-problem
✅My-Memo
✅Announcement
✅DataStructure-Tutorial
✅Algorithm-Introduction
✅Life-musings
✅DataStructure-Tree-Binary-Tree
✅Python-Scraping-Tutorial
✅My-Bloging-Workflow
✅Bash-commands
✅Pre-training-Is-Dead
✅CS294-1-LLM-Reasoning
✅DataStructure-Fenwick-Tree
✅DataStructure-Graph-Mathematical-Basis
✅RAG-tutorial
✅Input-and-Output-in-C-plus-plus
✅Missing-Semester-Notes
✅Math-Integral-Cheatsheet
✅Exception-Handling-in-C-plus-plus
⏸️RL-speeches
⏸️AI-Paper-2024
✅CLI-Roadmap
✅DataStructure-B-and-B-plus-Tree
✅DataStructure-Sparse-Table
✅Dynamic-Memory-and-Classes
✅Tools-Tutorial
✅Class-Inheritance
✅LLM-Learning-Initial
✅Bash-exercises
✅Profiling-and-Debugging
✅Above-All-ZH
✅CMake-tutorial-episode2
✅Leetcode-Mistake-collection
✅DataStructure-LCA
✅DataStructure-LinearList
✅My-Posts
✅CMake-tutorial1
✅Algorithm-Sorting
✅Python-Environment-Modules-Tutorial
✅Algorithm-Chunking
✅Algorithm-BFS-DFS
✅DataStructure-Graph-SCC
✅Python-Package-Manager
✅Pointers-Arrays-and-Functions
✅LaTeX-tutorial
✅Python-Advanced-Programming
✅DataStructure-Stack-Queue-Advanced
✅Secure-Shell-and-Encryption
✅Deep-Learning-Memo
✅DataStructure-Graph-SSSP-problem
✅Rust-OwnerShip
✅DataStructure-Awesome
✅Javascripts-Advanced
✅Factor-Mining-in-Quantitative-Investing-A-Survey
✅LLM-Evaluating
✅Leetcode-Mistake-collection-21-30
✅DataStructure-Tree
✅Lightweight-speech-recognition-conversion-model
✅Torch-memo
✅Code-Reuse-in-OOP
✅Jotting-References-and-Encapsulation-in-OOP
✅Code-Line-Counter
✅DataStructure-String
✅Agents-in-Coding-A-survey
✅LLML-Transformer
✅DataStructure-Graph-MST-problem
✅Quick-GPT-A-fast-and-simple-CLI-LLM-calling-function
```
<!-- END -->

## Introduction

This is an automation script I implemented in the Hexo blog update to automatically fetch blog updates, compare them with previous update statuses, and allow users to manually determine the update status of unfinished and newly added blogs, thus obtaining the new blog update status.

All Blogs are classified into three major categories:

- ⏸️(Still working)

- ✅(Mostly finished)

- ❌(Barely completed)

## Preliminaries

<div style="padding: 10px; background-color: #E7F5FF; border-left: 5px solid #4DABF7; border-radius: 4px; margin: 10px 0;">
ℹ️ For the latest version, we strongly recommend you to run `main.py` (or `run.sh` directly)! The old version of `main.sh` will no longer be maintained.
</div>

For the latest version, you need to get the **Absolute address** of your `hexo` directories which stores all your **Markdown** files and replace it with the variable of `BLOG_DIR`.

For example, in `main.py`:

```python
#!/home/xiyuanyang/anaconda3/bin/python
# ! ATTENTION: change it to your own python interpreter.
import os
import sys
from datetime import datetime

# Configuration
# ! ATTENTION: replace the BLOG_DIR with your own.
BLOG_DIR = "/mnt/d/Blog/source/_posts"
```

## Usage

### For the new version

You can run the original python scripts:

```bash
python main.py
```
And you will see the answers and the output! Go to [Demo](#Demo) for more details.

Or you can run the bash scripts `run.sh` to achieve more refined output control!

```bash
bash run.sh
```

<details>
<summary>For the old version (not recommended)</summary>


In `main.sh`, change the directory into your own directory:

```bash
DIR="/mnt/d/Blog/source/_posts"

# Change this line into your own directory!
```

Then create a new dir containing logs.

```bash
touch log
```

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

For **Hexo** Blog users, the directory which stores your Blog posts may be like as follows:

- Several `.md` files
- Several directories which has the same name with `.md` files

The `main.sh` will automatically get all file names using the `grep` command:

```bash
ls $DIR | grep -v ".*\.md" | grep -v ".*\.sh" > ans.txt
```

> `grep -v ".*\.sh"` is because I add several `.sh` files into it. You can modify it with your own needs.

Then, the file will compare the new status with the previous status stored in the `prev.txt`. Then the file will ask users to manually determine the update status of unfinished and newly added blogs.


Finally, the scripts will update `prev.txt` and generate a new blog status named `20250330_200559.txt` and you can see the updated status there!

</details>




## Demo

![Demo 1](./img/demo1.png)

![Demo 2](./img/demo2.png)

**Enjoy Coding**

## Discussion

Just for fun, and just for `hexo` users.

Welcome PRs.