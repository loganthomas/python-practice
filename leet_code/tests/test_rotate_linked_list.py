import unittest
from collections import deque

from leet_code import rotate_linked_list


class TestMaximumWidthRamp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = [([0, 1, 2], 4, [2, 0, 1]), ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])]

    def test_simple_non_linked_solution_1(self):
        for head, k, expected in self.cases:
            with self.subTest(head=head, k=k, expected=expected):
                result = rotate_linked_list.simple_non_linked_solution_1(head, k)
                self.assertEqual(result, expected)

    def test_simple_non_linked_solution_2(self):
        for head, k, expected in self.cases:
            with self.subTest(head=head, k=k, expected=expected):
                result = rotate_linked_list.simple_non_linked_solution_2(head, k)
                self.assertEqual(result, expected)

    def test_built_in_non_linked_solution(self):
        for head, k, expected in self.cases:
            with self.subTest(head=head, k=k, expected=expected):
                result = rotate_linked_list.built_in_non_linked_solution(head, k)
                self.assertEqual(result, expected)

    def test_linked_solution(self):
        for head, k, expected in self.cases:
            with self.subTest(head=head, k=k, expected=expected):
                result = rotate_linked_list.SolutionLinkedList().rotate_right(head, k)
                self.assertEqual(result, expected)

    def test_leet_solution(self):
        """
        Special expectation baked in: given node of a linked list
        (not a list from which to build a linked list).
        """
        for head, k, expected in self.cases:
            with self.subTest(head=head, k=k, expected=expected):
                nodes = deque(head)
                node = rotate_linked_list.ListNode(nodes.popleft())

                # leet code expects single head node of linked list
                head = node

                for element in nodes:
                    node.next = rotate_linked_list.ListNode(element)
                    node = node.next

                result = rotate_linked_list.LeetSolution().rotateRight(head, k)

                # leet code would have accepted the above as correct
                # since it returns a linked list as expected
                # here, need to convert expected  to linked list
                expected_nodes = deque(expected)
                node = rotate_linked_list.ListNode(expected_nodes.popleft())
                expected_head = node
                for element in expected_nodes:
                    node.next = rotate_linked_list.ListNode(element)
                    node = node.next

                self.assertEqual(str(result), str(expected_head))
