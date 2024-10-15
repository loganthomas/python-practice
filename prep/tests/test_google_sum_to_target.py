import unittest

from prep import google_sum_to_target


class TestGoogleSumToTarget(unittest.TestCase):
    def setUp(self):
        self.cases = [
            ([1, 2, 3, 4, 9], 10, (1, 9)),
            ([1, 2, 3, 4, 9], 8, -1),
            ([1, 4, 4], 8, (4, 4)),
            ([1, 4], 8, -1),
            ([1, 2, 3, 9, 22], 10, (1, 9)),
            ([1, 2, 3, 9, 22], 8, -1),
            ([1, 2, 3, 9, 22], 23, (1, 22)),
        ]

    def test_sum_to_target(self):
        for a, target, expected in self.cases:
            with self.subTest(a=a, target=target, expected=expected):
                result = google_sum_to_target.find_sum_to_target(a, target)
                if expected == -1:
                    self.assertFalse(result)
                else:
                    self.assertTrue(result)

    def test_sum_to_target2(self):
        for a, target, expected in self.cases:
            with self.subTest(a=a, target=target, expected=expected):
                result = google_sum_to_target.find_sum_to_target2(a, target)
                if isinstance(expected, int):
                    self.assertEqual(result, expected)
                else:
                    # (1,9) and (9,1) are equivalent
                    self.assertEqual(sorted(result), sorted(expected))

    def test_sum_to_target_w_binary_serach(self):
        for a, target, expected in self.cases:
            with self.subTest(a=a, target=target, expected=expected):
                result = google_sum_to_target.find_sum_to_target_w_binary_search(a, target)
                if isinstance(expected, int):
                    self.assertEqual(result, expected)
                else:
                    # (1,9) and (9,1) are equivalent
                    self.assertEqual(sorted(result), sorted(expected))

    def test_sum_to_target_w_indexing(self):
        for a, target, expected in self.cases:
            with self.subTest(a=a, target=target, expected=expected):
                result = google_sum_to_target.find_sum_to_target_w_indexing(a, target)
                if isinstance(expected, int):
                    self.assertEqual(result, expected)
                else:
                    # (1,9) and (9,1) are equivalent
                    self.assertEqual(sorted(result), sorted(expected))

    def test_sum_to_target_w_set(self):
        for a, target, expected in self.cases:
            with self.subTest(a=a, target=target, expected=expected):
                result = google_sum_to_target.find_sum_to_target_w_set(a, target)
                if isinstance(expected, int):
                    self.assertEqual(result, expected)
                else:
                    # (1,9) and (9,1) are equivalent
                    self.assertEqual(sorted(result), sorted(expected))
