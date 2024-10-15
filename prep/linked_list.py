"""
Practice manually implementing a linked list.

References
----------
https://builtin.com/data-science/python-linked-list
https://realpython.com/linked-lists-python/
"""

from collections import deque
from functools import cached_property


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{__class__.__name__}(value={self.value}, next={self.next})'


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        nodes = deque(nodes) if nodes else deque()

        if nodes:
            node = Node(nodes.popleft())
            self.head = node
            for element in nodes:
                node.next = Node(element)
                node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return f'{self.head}'

    def __str__(self):
        return ' -> '.join([str(n.value) for n in self])

    @cached_property
    def size(self):
        cnt = 0
        node = self.head
        while node:
            cnt += 1
            node = node.next
        return cnt


if __name__ == '__main__':
    linked = LinkedList(range(5))
    print(linked)
    print(linked.head)
    print(f'{linked.size=}')
