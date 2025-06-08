import unittest
import io
import sys
from python_assignment.src.assignment14.util import print_formatted

class TestPrintFormatted(unittest.TestCase):
    def test_print_formatted_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        print_formatted(2)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().split('\n')

        self.assertEqual(output[0], "1 1 1 1")
        self.assertEqual(output[1], "2 2 2 10")

if __name__ == '__main__':
    unittest.main()
