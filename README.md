# datastructs

Module created to facilitate the creation and use of data structures

[![Build Status](https://travis-ci.com/BarthJr/datastructs.svg?branch=master)](https://travis-ci.com/BarthJr/datastructs)
[![Updates](https://pyup.io/repos/github/BarthJr/datastructs/shield.svg)](https://pyup.io/repos/github/BarthJr/datastructs/)
[![Python 3](https://pyup.io/repos/github/BarthJr/datastructs/python-3-shield.svg)](https://pyup.io/repos/github/BarthJr/datastructs/)


# Installation

```Python3
pipenv install datastructs
```

# How to Use
## Binary Tree

```Python3
>>> from datastructs import BinaryTree
>>> binary_tree = BinaryTree([1, 2, 3, 4])
>>> binary_tree.print()
1 2 3 4 
>>> binary_tree.add([5, 6, 7, 8])
>>> binary_tree.print()
1 2 3 4 5 6 7 8 
>>> binary_tree.print('pre')
1 2 4 6 8 7 5 3 
>>> binary_tree.print('in')
8 6 4 7 2 5 1 3 
>>> binary_tree.print('pos')
8 6 7 4 5 2 3 1 

```
## Linked List
```Python3
>>> from datastructs import LinkedList
>>> linked_list = LinkedList([1, 2, 3, 4])
>>> linked_list.print()
1->2->3->4
>>> linked_list.add([5, 6, 7, 8])
>>> linked_list.print()
1->2->3->4->5->6->7->8

```

# How to contribute

All code follows [PEP8](https://www.python.org/dev/peps/pep-0008/), except for the line length, which accepts 120 characters.

1. Make the project fork and clone the project: `git clone git@github.com:<your_user>/datastructs.git`
2. Install pipenv: `pip install pipenv`
3. Install the dependencies for dev: `pipenv install -d`
4. Develop the feature with tests
5. Run the tests locally: `pipenv run pytest`
6. Send the pull request with tests in a single commit
7. Submit the PR for review
8. After reviewed and corrected, the PR will be accepted and the lib post in PyPi
