from typing import List, Union

NOTHING = object()


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        left = None if self.left is None else self.left.value
        right = None if self.right is None else self.right.value
        return '(D:{}, L:{}, R:{})'.format(self.val, left, right)


class BinaryTree:
    def __init__(self, value: Union[int, List] = None):
        self.root = None
        if value:
            self.add(value)

    def print(self, order: str = None, node: TreeNode = None) -> None:
        """Prints binary tree according to the type of the chosen order"""
        if node is None:
            node = self.root
        if order is None:
            order = 'lvl'

        if order == 'lvl':
            self._print_lvl_order(node)
        elif order == 'pre':
            self._print_pre_order(node)
        elif order == 'in':
            self._print_in_order(node)
        elif order == 'pos':
            self._print_pos_order(node)

        else:
            raise AttributeError('This order type is not supported.')

    def add(self, value: Union[int, List]) -> None:
        """Add a element or list of elements in tree by level order"""
        if type(value) == int:
            self._insert_node(value)
        elif type(value) == list:
            self._insert_list(value)

    def _print_pre_order(self, node: TreeNode = NOTHING) -> None:
        if node is NOTHING:
            node = self.root
        if node:
            print(node.val, end=' ')
            self._print_pre_order(node.left)
            self._print_pre_order(node.right)

    def _print_in_order(self, node: TreeNode = NOTHING) -> None:
        if node is NOTHING:
            node = self.root
        if node:
            self._print_in_order(node.left)
            print(node.val, end=' ')
            self._print_in_order(node.right)

    def _print_pos_order(self, node: TreeNode = NOTHING) -> None:
        if node is NOTHING:
            node = self.root
        if node:
            self._print_pos_order(node.left)
            self._print_pos_order(node.right)
            print(node.val, end=' ')

    def _print_lvl_order(self, node: TreeNode = NOTHING) -> None:
        if node is NOTHING:
            node = self.root
        h = self.tree_height(node)
        for i in range(1, h + 1):
            self._print_given_level(node, i)
        print()

    def _print_given_level(self, node: TreeNode, level: int) -> None:
        """Given a level of tree, print the nodes"""
        if node is None:
            return
        if level == 1:
            print(node.val, end=' ')
        elif level > 1:
            self._print_given_level(node.left, level - 1)
            self._print_given_level(node.right, level - 1)

    def level_order_traversal(self) -> List:
        """Traverse a binary tree in level order"""
        res = []
        h = self.tree_height(self.root)
        for i in range(1, h + 1):
            self._given_level(self.root, i, res)
        return res

    def _given_level(self, node: TreeNode, level: int, res: List) -> None:
        """Given a level of tree, gets the nodes"""
        if node is None:
            return
        if level == 1:
            res.append(node.val)
        elif level > 1:
            self._given_level(node.left, level - 1, res)
            self._given_level(node.right, level - 1, res)

    def tree_height(self, node: TreeNode) -> int:
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

    def _insert_node(self, val: int, node: TreeNode = None) -> None:
        """Insert node in level order traversal"""
        if self.root is None:
            self.root = TreeNode(val)
            return
        if node is None:
            node = self.root
        q = list()
        q.append(node)
        while len(q):
            node = q[0]
            q.pop(0)
            if not node.left:
                node.left = TreeNode(val)
                break
            else:
                q.append(node.left)
            if not node.right:
                node.right = TreeNode(val)
                break
            else:
                q.append(node.right)

    def _insert_list(self, array: List) -> None:
        for num in array:
            self._insert_node(num)
