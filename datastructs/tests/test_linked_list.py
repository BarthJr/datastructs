from datastructs import LinkedList
from datastructs.linked_list import ListNode


def test_create_list_node():
    list_node = ListNode()
    assert isinstance(list_node, ListNode)


def test_create_linked_list():
    linked_list = LinkedList()
    assert isinstance(linked_list, LinkedList)
