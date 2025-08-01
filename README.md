# Blog Update Fetching Script

## My Blog Updating Status

<!-- BEGIN -->
```text
✅Python-Threadings
✅DataStructure-Stack
✅Algorithm-Sorting
✅AIBasis-Neural-Networks
✅Imagenet
✅Bash-exercises
✅Exception-Handling-in-C-plus-plus
✅My-WorkFlow
✅Introduction-to-OOP
✅Code-Line-Counter
✅Algorithm-BFS-DFS
✅Algorithm-Memo
✅CMake-tutorial1
✅CLI-Roadmap
⏸️LLML-CS336-Lecture-2-Pytorch-Resource-Accounting
✅DataStructure-B-and-B-plus-Tree
✅Pointers-Arrays-and-Functions
✅DataStructure-Splay-Tree
✅DataStructure-Segment-Tree
✅DataStructure-Tree-Binary-Tree
✅Profiling-and-Debugging
✅DataStructure-Fenwick-Tree
✅Blog-Update-Fetching-Script
⏸️AI-Paper-2024
✅DataStructure-Hash-Table
✅My-Memo
✅Leetcode-Mistake-collection-11-20
✅DataStructure-Stack-Queue-Advanced
✅Leetcode-Mistake-collection-31-40
✅Python-Pipe
✅Deep-Learning-Memo
✅Javascripts-Advanced
✅My-Multi-Agents
✅CamelAI-automatic-essay-modification
✅Linux-Bash-Introduction
✅Bash-commands
✅Feishu-GPU-Auto-Monitoring
✅Python-Scraping-Tutorial
✅Tools-Tutorial
✅Modern-C
✅C-plus-plus-Primer-Plus-tutorial
✅Algorithm-BinaryTree
✅Dynamic-Memory-and-Classes
❌DataStructure-Graph-Network-Flow-problem
✅LLML-Attention
✅Code-Reuse-in-OOP
✅Taking-Notes
✅Leetcode-Mistake-collection-1-10
✅CS294-1-LLM-Reasoning
✅DataStructure-LinearList
✅Secure-Shell-and-Encryption
✅Python-Environment-Modules-Tutorial
✅RAG-tutorial
✅My-Posts
✅CMake-tutorial-episode2
✅Python-Architecture-Patterns
✅Missing-Semester-Notes
✅DataStructure-Graph-Introduction
✅Vim-tutorial
✅Announcement
✅Class-Inheritance
✅My-Bloging-Workflow
✅DataStructure-Awesome
✅DataStructure-Tutorial
✅DataStructure-String
✅Math-Integral-Cheatsheet
✅LLM-Learning-Initial
✅Quick-GPT-A-fast-and-simple-CLI-LLM-calling-function
✅hello-world
✅DataStructure-Tree-Binary-Heap
✅Automaton-NFA
✅DataStructure-Graph-MST-problem
✅Leetcode-Mistake-collection-21-30
✅Python-Advanced-Programming
✅Linked-List-Implementation-Based-on-Structs
✅Python-Architecture-Patterns-Multi-file-Progarmming
✅Torch-Memo-Tensor-Operations
✅DataStructure-RBT-Tree
✅Jotting-References-and-Encapsulation-in-OOP
✅Python-File-Management
✅Lightweight-speech-recognition-conversion-model
✅Python-visualization
✅Life-musings
✅Algorithm-Introduction
✅DataStructure-Set
✅Regular-Expression
✅Python-numpy-cheatsheet
✅Algorithm-MCTS
✅LLM-Evaluating
✅LLML-Transformer
✅DataStructure-Graph-Mathematical-Basis
✅DataStructure-AVL-Tree
✅DataStructure-LCA
✅DataStructure-Disjoint-Set
✅Docker-Tutorial
✅Javascripts-Memo
✅DataStructure-Queue
✅Pythonic-Functional-Programming
✅Rust-OwnerShip
✅Factor-Mining-in-Quantitative-Investing-A-Survey
✅Above-All-en
✅DataStructure-Graph-AOE-and-AOV-Network
✅Agents-in-Coding-A-survey
✅RAG-Blog-Content-Retrieval
✅DataStructure-Graph-SCC
⏸️RL-speeches
✅Blog-Word-Counter
✅Torch-Memo-TensorBoard
✅Input-and-Output-in-C-plus-plus
✅DataStructure-Graph-SSSP-problem
✅DataStructure-Tree-Binary-Search-Tree
✅Python-Package-Manager
✅Python-cheatsheet
✅DataStructure-Tree
✅LaTeX-tutorial
✅Torch-memo
✅Algorithm-Chunking
✅Pre-training-Is-Dead
✅CS294-3-Autogen
✅Leetcode-Mistake-collection
✅LLML-CS336-Lecture-1-Overview-and-Tokenization
✅WSL-Proxy
✅DataStructure-Sparse-Table
✅Above-All-ZH
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