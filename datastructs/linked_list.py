from typing import Union, List


class ListNode:
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val: Union[int, List] = None) -> None:
        self.head = self.tail = None
        if val:
            self.add(val)

    def add(self, val):
        if self.head is None:
            self.head = self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val)

    def _traversal(self, list_node: ListNode = None) -> List:
        res = []
        if list_node is None:
            return res
        while list_node:
            if list_node:
                res.append(list_node.val)
            list_node = list_node.next
        return res
