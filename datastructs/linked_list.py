from typing import Union, List


class ListNode:
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val: Union[int, List] = None) -> None:
        self.head = self.tail = None
