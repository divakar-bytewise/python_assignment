import unittest
from python_assignment.src.assignment13.util import can_stack_cubes

class TestCanStackCubes(unittest.TestCase):
    def test_can_stack_cubes(self):
        self.assertEqual(can_stack_cubes([4, 3, 2, 1, 3, 4]), "No")
        self.assertEqual(can_stack_cubes([1, 3, 2]), "Yes")
        self.assertEqual(can_stack_cubes([3, 2, 1]), "Yes")

if __name__ == '__main__':
    unittest.main()
