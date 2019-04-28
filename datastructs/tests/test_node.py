from datastructs.trees import Node


def test_create_node():
    node = Node(4)
    assert isinstance(node, Node)
