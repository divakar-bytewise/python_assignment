import unittest
import sys
import io
import numpy as np
from python_assignment.src.assignment10.util import max_min

class TestMaxMin(unittest.TestCase):
    def test_max_min(self):
        
        test_input = "3 3\n3 7 8\n2 9 4\n1 5 6\n"
        expected_output = "4\n"

    
        sys.stdin = io.StringIO(test_input)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        max_min(3, 3)

        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
