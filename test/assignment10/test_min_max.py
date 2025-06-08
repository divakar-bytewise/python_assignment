import unittest
import io
import sys
from python_assignment.src.assignment10.util import determinant

class TestDeterminant(unittest.TestCase):
    def test_determinant(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.stdin = io.StringIO("2\n1 2\n3 4\n")
        
        determinant(2)
        
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        output = captured_output.getvalue().strip()
        self.assertEqual(output, "-2.0")

if __name__ == '__main__':
    unittest.main()
