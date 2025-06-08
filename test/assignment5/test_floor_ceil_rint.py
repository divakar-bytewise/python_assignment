import unittest
from io import StringIO
import sys
import numpy as np
from python_assignment.src.assignment5.util import convertion

class TestConvertion(unittest.TestCase):
    def test_convertion_output(self):
        test_input=[1.2, 2.5, 3.7]
        expected_floor=np.floor(test_input)
        expected_ceil=np.ceil(test_input)
        expected_rint=np.rint(test_input)

        captured_output=StringIO()
        sys.stdout=captured_output
        convertion(test_input)
        sys.stdout=sys.__stdout__

        output_lines=captured_output.getvalue().strip().split('\n')
        np.set_printoptions(sign=" ")

        self.assertEqual(output_lines[0], str(expected_floor))
        self.assertEqual(output_lines[1], str(expected_ceil))
        self.assertEqual(output_lines[2], str(expected_rint))

if __name__ == '__main__':
    unittest.main()
