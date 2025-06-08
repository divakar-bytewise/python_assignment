import unittest
import io
import sys
from python_assignment.src.assignment9.util import merge_the_tools

class TestMergeTheTools(unittest.TestCase):
    def test_merge_the_tools(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        merge_the_tools("AABCAAADA", 3)
        sys.stdout = sys.__stdout__
        result = captured_output.getvalue().strip().split('\n')
        expected = ['AB', 'CA', 'AD']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
