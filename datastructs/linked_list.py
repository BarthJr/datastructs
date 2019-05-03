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

    def add(self, val: Union[int, List]) -> None:
        if type(val) == int:
            if self.head is None:
                self.head = self.tail = ListNode(val)
            else:
                self.tail.next = ListNode(val)
        elif type(val) == list:
            if self.head is None:
                self.head = self.tail = ListNode(val.pop(0))
            while val:
                self.tail.next = ListNode(val.pop(0))
                self.tail = self.tail.next

    def _traversal(self, list_node: ListNode = None) -> List:
        res = []
        if list_node is None:
            return res
        while list_node:
            if list_node:
                res.append(list_node.val)
            list_node = list_node.next
        return res

    def print(self, list_node: ListNode = None) -> None:
        if list_node is None:
            list_node = self.head
        list_nodes = self._traversal(list_node)
        for i in list_nodes[:-1]:
            print(i, end='->')
        print(list_nodes[-1])
