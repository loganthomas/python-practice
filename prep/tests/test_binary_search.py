import unittest

from prep import binary_search


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.cases = [
            ([1, 2, 3], 0, 2, 3, 3),
            (list(range(9)), 0, 8, 8, 8),
            (list(range(9)), 0, 8, 10, -1),
            (list(range(9)), 0, 8, -10, -1),
        ]

    def test_binary_search_recursive(self):
        for x, low, high, find, expected in self.cases:
            with self.subTest(x=x, low=low, high=high, find=find, expected=expected):
                result = binary_search.binary_search_recursive(x, low, high, find)
                self.assertEqual(result, expected)

    def test_binary_search_indexed(self):
        for x, low, high, find, expected in self.cases:
            with self.subTest(x=x, low=low, high=high, find=find, expected=expected):
                x_enum = list(enumerate(x))
                if expected >= 0:
                    idx = x.index(expected)
                    expected = x_enum[idx]
                result = binary_search.binary_search_indexed(x_enum, low, high, find)
                self.assertEqual(result, expected)

    def test_binary_search_iterative(self):
        for x, low, high, find, expected in self.cases:
            with self.subTest(x=x, low=low, high=high, find=find, expected=expected):
                result = binary_search.binary_search_iterative(x, low, high, find)
                self.assertEqual(result, expected)

    def test_binary_search_iterative_indexed(self):
        for x, low, high, find, expected in self.cases:
            with self.subTest(x=x, low=low, high=high, find=find, expected=expected):
                if expected >= 0:
                    idx = x.index(expected)
                    x_enum = list(enumerate(x))
                    expected = x_enum[idx]
                result = binary_search.binary_search_iterative(x, low, high, find, show_index=True)
                self.assertEqual(result, expected)
