import unittest
from python_assignment.src.assignment6.util import probability_of_a

class TestProbabilityOfA(unittest.TestCase):
    def test_case_1(self):
        n = 4
        letters = ['a', 'a', 'c', 'd']
        k = 2
        result = probability_of_a(n, letters, k)
        self.assertAlmostEqual(result, 0.8333, places=4)

    def test_case_2(self):
        n = 5
        letters = ['a', 'b', 'c', 'd', 'e']
        k = 3
        result = probability_of_a(n, letters, k)
        self.assertAlmostEqual(result, 0.6825, places=4)

if __name__ == '__main__':
    unittest.main()
