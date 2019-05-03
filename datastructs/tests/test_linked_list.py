from datastructs import LinkedList
from datastructs.linked_list import ListNode


def test_create_list_node():
    list_node = ListNode()
    assert isinstance(list_node, ListNode)


def test_create_list_node_passing_int():
    list_node = ListNode(1)
    assert isinstance(list_node, ListNode)


def test_create_linked_list():
    linked_list = LinkedList()
    assert isinstance(linked_list, LinkedList)


def test_create_linked_list_passing_int():
    linked_list = LinkedList(4)
    assert isinstance(linked_list, LinkedList)


def test_create_linked_list_with_int():
    linked_list = LinkedList(4)
    assert linked_list._traversal(linked_list.head) == [4]


def test_create_linked_list_and_insert_int():
    linked_list = LinkedList()
    linked_list.add(5)
    assert linked_list._traversal(linked_list.head) == [5]


def test_create_linked_list_with_int_and_insert_int():
    linked_list = LinkedList(4)
    linked_list.add(5)
    assert linked_list._traversal(linked_list.head) == [4, 5]


def test_create_linked_list_and_insert_list():
    linked_list = LinkedList()
    linked_list.add([4, 5])
    assert linked_list._traversal(linked_list.head) == [4, 5]


def test_create_linked_list_with_int_and_insert_list():
    linked_list = LinkedList(3)
    linked_list.add([4, 5])
    assert linked_list._traversal(linked_list.head) == [3, 4, 5]


def test_create_linked_list_with_list_and_insert_int():
    linked_list = LinkedList([2, 3])
    linked_list.add(4)
    assert linked_list._traversal(linked_list.head) == [2, 3, 4]


def test_create_linked_list_with_list_and_insert_list():
    linked_list = LinkedList([2, 3])
    linked_list.add([4, 5])
    assert linked_list._traversal(linked_list.head) == [2, 3, 4, 5]


def test_if_list_remains_the_same_after_passed_as_parameter_in_constructor():
    lst = [1, 2, 3, 4]
    LinkedList(lst)
    assert lst == [1, 2, 3, 4]


def test_if_list_remains_the_same_after_passed_as_parameter_in_method():
    lst = [1, 2, 3, 4]
    LinkedList(lst).add(lst)
    assert lst == [1, 2, 3, 4]
