# datastructs

Module created to facilitate the creation and usage of data structures

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
>>> linked_list = LinkedList()

```
