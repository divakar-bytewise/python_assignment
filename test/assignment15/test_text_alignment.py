import unittest
import io
import sys
from python_assignment.src.assignment15.util import print_h_logo

class TestPrintHLogo(unittest.TestCase):
    def test_h_logo_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        print_h_logo(2)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().split('\n')

        
        self.assertGreater(len(output), 0)
        self.assertIn(" H ", output[0])
        self.assertIn("HH", output[2])

if __name__ == '__main__':
    unittest.main()
