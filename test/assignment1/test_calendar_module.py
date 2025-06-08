import unittest
from python_assignment.src.assignment1.util import finding_day

class TestFindingDay(unittest.TestCase):

    def test_known_date(self):
        self.assertEqual(finding_day(8, 5, 2015), "WEDNESDAY")
        self.assertEqual(finding_day(1, 1, 2000), "SATURDAY")
        self.assertEqual(finding_day(12, 25, 2023), "MONDAY")
        self.assertEqual(finding_day(6, 4, 2025), "WEDNESDAY")  

if __name__ == '__main__':
    unittest.main()
