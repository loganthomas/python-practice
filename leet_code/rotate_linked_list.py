"""
https://leetcode.com/problems/rotate-list/description/

61. Rotate List
Medium
Topics
Companies
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

from collections import deque


def simple_non_linked_solution_1(head, k):
    pt = len(head) - k
    return head[pt:] + head[:pt]


def simple_non_linked_solution_2(head, k):
    head = deque(head)
    for _ in range(k % len(head)):
        head.appendleft(head.pop())
    return list(head)


def built_in_non_linked_solution(head, k):
    head = deque(head)
    head.rotate(k)
    return list(head)


#######################################
# Trying to match format on leet code #
#######################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{__class__.__name__}(val={self.val}, next={self.next})'


class LinkedList:
    def __init__(self, nodes=None):
        # if nothing provided head and nodes are None, deque()
        self.head = None
        nodes = deque(nodes) if nodes else deque()

        # if nodes exist, set up the linked list
        if nodes:
            # make the first element of the nodes the head
            # this is why nodes should be a double ended queue (deque)
            node = ListNode(nodes.popleft())
            self.head = node

            # iterate over all nodes to set linkages
            # since the first node has been popped, this works;
            # this is really for element in remaining nodes after pop
            for element in nodes:
                node.next = ListNode(element)
                node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return f'{list(self)}'

    def __str__(self):
        return ' -> '.join([str(x.val) for x in self])


class SolutionLinkedList:
    def rotate_right(self, head, k):
        linked = LinkedList(head)

        k_ = k % len(head)
        if k_ == 0:
            return head

        n = len(head) - k_

        node = linked.head
        end = deque()
        while len(end) < n:
            end.append(node.val)
            node = node.next

        start = deque()
        while node is not None:
            start.append(node.val)
            node = node.next

        return list(start + end)


# special format
class LeetSolution:
    def rotateRight(self, head, k):
        # Instead of the LinkedList class, they want to use the head and iterate through
        if not head:
            return None

        last_seen = head
        length = 1

        while last_seen.next is not None:
            last_seen = last_seen.next
            length += 1

        k = k % length

        # circular
        # 1 -> 2 -> 3 -> 4 -> 5 ->
        # 1 -> 2 -> 3 -> 4 -> 5 ->
        # trick is to use the length calc to get to end and then set next of end to head
        # thus making it circular
        last_seen.next = head

        # need tmp variable to keep before out to set to None and end circular
        tmp = head
        for _ in range(length - k - 1):
            tmp = tmp.next

        out = tmp.next

        # cut off circular
        tmp.next = None

        return out
