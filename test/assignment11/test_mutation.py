import unittest
from python_assignment.src.assignment11.util import mutate_string

class TestMutateString(unittest.TestCase):
    def test_mutate_string(self):
        result = mutate_string("hello", 1, "a")
        self.assertEqual(result, "hallo")

if __name__ == '__main__':
    unittest.main()
