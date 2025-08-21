# Blog Update Fetching Script

## My Blog Updating Status

<!-- BEGIN -->
```text
🫡AI-Paper-2024
✅AIBasis-Neural-Networks
✅Above-All-ZH
✅Above-All-en
✅Agents-in-Coding-A-survey
✅Algorithm-BFS-DFS
✅Algorithm-BinaryTree
✅Algorithm-Chunking
✅Algorithm-Introduction
✅Algorithm-MCTS
✅Algorithm-Memo
✅Algorithm-Sorting
✅Andrew-Ng-Building-Faster-with-AI
✅Announcement
✅Automaton-NFA
✅Bash-commands
✅Bash-exercises
✅Blog-Update-Fetching-Script
✅Blog-Word-Counter
✅C-plus-plus-Primer-Plus-tutorial
✅CLI-Roadmap
✅CMake-tutorial-episode2
✅CMake-tutorial1
✅CS294-1-LLM-Reasoning
✅CS294-3-Autogen
✅CamelAI-automatic-essay-modification
✅Class-Inheritance
✅Code-Line-Counter
✅Code-Reuse-in-OOP
✅DataStructure-AVL-Tree
✅DataStructure-Awesome
✅DataStructure-B-and-B-plus-Tree
✅DataStructure-Disjoint-Set
✅DataStructure-Fenwick-Tree
✅DataStructure-Graph-AOE-and-AOV-Network
✅DataStructure-Graph-Introduction
✅DataStructure-Graph-MST-problem
❌DataStructure-Graph-Network-Flow-problem
✅DataStructure-Graph-SCC
✅DataStructure-Graph-SSSP-problem
✅DataStructure-Hash-Table
✅DataStructure-LCA
✅DataStructure-LinearList
✅DataStructure-Queue
✅DataStructure-RBT-Tree
✅DataStructure-Segment-Tree
✅DataStructure-Sparse-Table
✅DataStructure-Splay-Tree
✅DataStructure-Stack
✅DataStructure-Stack-Queue-Advanced
✅DataStructure-String
✅DataStructure-Tree
✅DataStructure-Tree-Binary-Heap
✅DataStructure-Tree-Binary-Search-Tree
✅DataStructure-Tree-Binary-Tree
✅DataStructure-Tutorial
✅Deep-Learning-Memo
✅Docker-Tutorial
✅Dynamic-Memory-and-Classes
✅Exception-Handling-in-C-plus-plus
✅Factor-Mining-in-Quantitative-Investing-A-Survey
✅Feishu-GPU-Auto-Monitoring
✅Git-Advanced-Memo
✅Imagenet
✅Input-and-Output-in-C-plus-plus
✅Introduction-to-OOP
✅Javascripts-Advanced
✅Javascripts-Memo
✅Jotting-References-and-Encapsulation-in-OOP
✅LLM-Evaluating
✅LLM-Learning-Initial
✅LLML-Attention
✅LLML-CS336-Lecture-1-Overview-and-Tokenization
✅LLML-CS336-Lecture-2-Pytorch-Resource-Accounting
✅LLML-CS336-Lecture-3-1-Architectures
🫡LLML-CS336-Lecture-3-2-Hypeparameters
✅LLML-Transformer
✅LaTeX-tutorial
✅Leetcode-Mistake-collection
✅Leetcode-Mistake-collection-1-10
✅Leetcode-Mistake-collection-11-20
✅Leetcode-Mistake-collection-21-30
✅Leetcode-Mistake-collection-31-40
✅Life-musings
✅Lightweight-speech-recognition-conversion-model
✅Linked-List-Implementation-Based-on-Structs
✅Linux-Bash-Introduction
✅Math-Integral-Cheatsheet
✅Missing-Semester-Notes
✅Modern-C
✅My-Bloging-Workflow
✅My-Memo
✅My-Multi-Agents
✅My-Posts
✅My-ToolZoo
✅My-WorkFlow
✅One-year-of-Programming
✅Pointers-Arrays-and-Functions
✅Pre-training-Is-Dead
✅Profiling-and-Debugging
✅Python-Advanced-Programming
✅Python-Architecture-Patterns
✅Python-Architecture-Patterns-Multi-file-Progarmming
✅Python-Environment-Modules-Tutorial
✅Python-File-Management
✅Python-Package-Manager
✅Python-Pipe
✅Python-Scraping-Tutorial
✅Python-Threadings
✅Python-cheatsheet
✅Python-numpy-cheatsheet
✅Python-visualization
✅Pythonic-Functional-Programming
✅Quick-GPT-A-fast-and-simple-CLI-LLM-calling-function
✅RAG-Blog-Content-Retrieval
✅RAG-tutorial
🫡RL-speeches
✅Regular-Expression
✅Rust-OwnerShip
✅Secure-Shell-and-Encryption
✅Taking-Notes
✅The-New-Code-Sean-Grove-OpenAI
✅Tools-Tutorial
✅Torch-Memo-Tensor-Operations
✅Torch-Memo-TensorBoard
✅Torch-memo
✅Vim-tutorial
✅WSL-Proxy
✅hello-world
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