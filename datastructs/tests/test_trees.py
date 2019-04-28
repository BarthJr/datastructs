from datastructs import BinaryTree


def test_create_binary_tree():
    binary_tree = BinaryTree()
    assert isinstance(binary_tree, BinaryTree)


def test_create_binary_tree_passing_int():
    binary_tree = BinaryTree(4)
    assert isinstance(binary_tree, BinaryTree)


def test_create_binary_tree_passing_list():
    binary_tree = BinaryTree([4, 5, 6, 7])
    assert isinstance(binary_tree, BinaryTree)


def test_level_order_traversal_from_inserted_int():
    binary_tree = BinaryTree(4)
    assert binary_tree.level_order_traversal() == [4]


def test_level_order_traversal_from_inserted_list():
    binary_tree = BinaryTree([4, 5, 6, 7])
    assert binary_tree.level_order_traversal() == [4, 5, 6, 7]


def test_create_binary_tree_with_int_and_insert_int():
    binary_tree = BinaryTree(3)
    assert isinstance(binary_tree, BinaryTree)
    binary_tree.add(4)
    assert binary_tree.level_order_traversal() == [3, 4]


def test_create_binary_tree_with_int_and_insert_list():
    binary_tree = BinaryTree(3)
    assert isinstance(binary_tree, BinaryTree)
    binary_tree.add([4, 5])
    assert binary_tree.level_order_traversal() == [3, 4, 5]


def test_create_binary_tree_with_list_and_insert_int():
    binary_tree = BinaryTree([4, 5])
    assert isinstance(binary_tree, BinaryTree)
    binary_tree.add(3)
    assert binary_tree.level_order_traversal() == [4, 5, 3]


def test_create_binary_tree_with_list_and_insert_list():
    binary_tree = BinaryTree([4, 7])
    assert isinstance(binary_tree, BinaryTree)
    binary_tree.add([5, 6, 8])
    assert binary_tree.level_order_traversal() == [4, 7, 5, 6, 8]
