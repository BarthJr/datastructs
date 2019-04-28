from typing import List, Union

NOTHING = object()


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        left = None if self.left is None else self.left.value
        right = None if self.right is None else self.right.value
        return '(D:{}, L:{}, R:{})'.format(self.value, left, right)


class BinaryTree:
    def __init__(self, value: Union[int, List] = None):
        self.root = None
        if value:
            self.add(value)

    def print(self, order: str = None) -> None:
        """Prints binary tree according to the type of the chosen order"""
        if order is None:
            order = 'lvl'

        if order == 'pre':
            self._print_pre_order()
        elif order == 'in':
            self._print_in_order()
        elif order == 'pos':
            self._print_post_order()
        elif order == 'lvl':
            self._print_level_order()

        else:
            raise AttributeError('This order type is not supported.')

    def add(self, value: Union[int, List]) -> None:
        """Add a element or list of elements in tree by level order"""
        if type(value) == int:
            self._insert_node(value)
        elif type(value) == list:
            self._insert_list(value)

    def _print_pre_order(self, node: Node = NOTHING) -> None:
        if node is NOTHING:
            node = self.root
        if node:
            print(node.value, end=' ')
            self._print_pre_order(node.left)
            self._print_pre_order(node.right)

    def _print_in_order(self, node: Node = NOTHING) -> None:
        if node is NOTHING:
            node = self.root
        if node:
            self._print_in_order(node.left)
            print(node.value, end=' ')
            self._print_in_order(node.right)

    def _print_post_order(self, node: Node = NOTHING) -> None:
        if node is NOTHING:
            node = self.root
        if node:
            self._print_post_order(node.left)
            self._print_post_order(node.right)
            print(node.value, end=' ')

    def _print_level_order(self) -> None:
        h = self.tree_height(self.root)
        for i in range(1, h + 1):
            self._print_given_level(self.root, i)
        print()

    def _print_given_level(self, node: Node, level: int) -> None:
        """Given a level of tree, print the nodes"""
        if node is None:
            return
        if level == 1:
            print(node.value, end=' ')
        elif level > 1:
            self._print_given_level(node.left, level - 1)
            self._print_given_level(node.right, level - 1)

    def level_order_traversal(self) -> List:
        res = []
        h = self.tree_height(self.root)
        for i in range(1, h + 1):
            self._given_level(self.root, i, res)
        return res

    def _given_level(self, node: Node, level: int, res: List) -> None:
        """Given a level of tree, gets the nodes"""
        if node is None:
            return
        if level == 1:
            res.append(node.value)
        elif level > 1:
            self._given_level(node.left, level - 1, res)
            self._given_level(node.right, level - 1, res)

    def tree_height(self, node: Node) -> int:
        """Finds the height of the tree"""
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            left_height = self.tree_height(node.left)
            right_height = self.tree_height(node.right)

            # Use the larger one
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def _insert_node(self, value: int) -> None:
        if self.root:
            root = self.root
            node = Node(value)
            while root:
                if not root.left:
                    root.left = node
                    break
                elif not root.right:
                    root.right = node
                    break
                if root.left and root.left.value:
                    root = root.left
                elif root.right and root.right.value:
                    root = root.right
        else:
            self.root = Node(value)

    def _insert_list(self, array: List) -> None:
        for num in array:
            self._insert_node(num)
