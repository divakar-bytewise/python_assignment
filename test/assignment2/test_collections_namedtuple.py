import unittest
from unittest.mock import patch
from python_assignment.src.assignment2.util import finding_avg

class TestFindingAvg(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '1 90 A 9',
        '2 80 B 10',
        '3 70 C 9'
    ])
    def test_average(self, mock_input):
        n = 3
        attributes=['ID', 'MARKS', 'NAME', 'CLASS']
        result = finding_avg(n, attributes)
        self.assertEqual(round(result, 2), 80.00)

if __name__ == '__main__':
    unittest.main()
