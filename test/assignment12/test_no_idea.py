import unittest
from python_assignment.src.assignment12.util import happiness_score

class TestHappinessScore(unittest.TestCase):
    def test_happiness_score(self):
        n = 3
        m = 2
        arr = [1, 5, 3]
        a = {3, 1}
        b = {5, 7}
        result = happiness_score(n, m, arr, a, b)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
