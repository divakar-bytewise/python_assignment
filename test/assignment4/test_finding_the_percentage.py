import unittest
from python_assignment.src.assignment4.util import finding_average

class TestFindingAverage(unittest.TestCase):

    def test_average_1(self):
        data = {'Alice': [100, 90, 80], 'Bob': [70, 60, 50]}
        self.assertAlmostEqual(finding_average(data, 'Alice'), 90.0)

    def test_average_2(self):
        data = {'Divakar': [75.5, 80.0, 85.0], 'Akhil': [60.0, 70.0, 80.0]}
        self.assertAlmostEqual(finding_average(data, 'Divakar'), 80.17, places=2)

    def test_average_3(self):
        data = {'Ravi': [88.0, 92.0, 96.0]}
        self.assertEqual(finding_average(data, 'Ravi'), 92.0)

if __name__ == '__main__':
    unittest.main()
