import unittest
from python_assignment.src.assignment3.util import finding_second_largest

class TestFindingSecondLargest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(finding_second_largest([2,3,6,6,5]),5)

    def test_case_2(self):
        self.assertEqual(finding_second_largest([1,2,3,4,5]),4)

    def test_case_3(self):
        self.assertEqual(finding_second_largest([10,10,9]),9)

    def test_case_4(self):
        self.assertEqual(finding_second_largest([5,5,5,5,4]),4)

if __name__ == '__main__':
    unittest.main()
