import unittest

from prep import enthought


class TestEnthought(unittest.TestCase):
    def setUp(self):
        self.cases = [
            # fmt: off
            ([[1, 0, 1, 0], [0, 0, 1, 1]], 2),
            ([[1, 0], [0, 1]], 2),
            (
                [
                    [1, 0, 1, 0],
                    [0, 0, 1, 1],
                    [1, 0, 1, 0],
                    [0, 0, 1, 1],
                    [1, 0, 1, 0],
                    [0, 0, 1, 1],
                ],
                4,
            ),
        ]
        # fmt: on

    def test_count_fist(self):
        for image, expected in self.cases:
            with self.subTest(image=image, expected=expected):
                result = enthought.count_fish(image)
                self.assertEqual(result, expected)
