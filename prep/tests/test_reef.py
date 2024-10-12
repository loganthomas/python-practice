import io
import sys
import unittest
from contextlib import redirect_stdout

from prep import reef

# pytest way of capturing stdout
# def test_swap_cols(capsys):
#     sys.stdin = io.StringIO('1,2,3\ba,b,c')
#     reef.main()

#     captured = capsys.readouterr()
#     assert captured.out == 'test'


# unittest way of capturing stdout
class TestReef(unittest.TestCase):
    def setUp(self):
        self.cases = [
            ('1,2,3\r\na,b,c', '2,1,3\r\nb,a,c\r\n'),
            ('1,"2,3",4', '"2,3",1,4\r\n'),
            ('1,"2",3\r\n4,"5,6","7",8,"9"', '2,1,3\r\n"5,6",4,7,8,9\r\n'),
        ]

    def test_swap_cols(self):
        for csv, expected in self.cases:
            with self.subTest(csv=csv, expected=expected):
                with io.StringIO() as buf, redirect_stdout(buf):
                    sys.stdin = io.StringIO(csv)
                    reef.swap_cols()
                    result = buf.getvalue()

                    self.assertEqual(result, expected)
