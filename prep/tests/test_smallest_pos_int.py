import unittest

from prep import smallest_pos_int


class TestSmallestPosInt(unittest.TestCase):
    def setUp(self):
        self.probs = [([1, 3, 6, 4, 1, 2], 5), ([1, 2, 3], 4), ([-1, -3], 1), ([0], 1)]

    def test_brute_force_solution(self):
        for data, ans in self.probs:
            with self.subTest(data=data, expected=ans):
                result = smallest_pos_int.brute_solution(data)
                self.assertEqual(result, ans)

    def test_better_solution(self):
        for data, ans in self.probs:
            with self.subTest(data=data, expected=ans):
                result = smallest_pos_int.better_solution(data)
                self.assertEqual(result, ans)

    def test_solution(self):
        for data, ans in self.probs:
            with self.subTest(data=data, expected=ans):
                result = smallest_pos_int.solution(data)
                self.assertEqual(result, ans)
