import unittest
from unittest.mock import patch
from io import StringIO
from python_assignment.src.assignment7.util import determinant

class TestDeterminant(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '1.0 2.0',
        '3.0 4.0'
    ])
    @patch('builtins.print')
    def test_determinant_2x2(self, mock_print, mock_input):
        determinant(2)
        mock_print.assert_called_with(-2.0)


if __name__ == '__main__':
    unittest.main()
