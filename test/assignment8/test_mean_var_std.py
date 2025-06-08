import unittest
from python_assignment.src.assignment8.util import calculate_statistics

class TestCalculateStatistics(unittest.TestCase):
    def test_calculate_statistics(self):
        mean_rows, var_columns, std_dev = calculate_statistics()

        expected_mean_rows = [2.0, 5.0]
        expected_var_columns = [2.0, 2.0, 2.0]
        expected_std_dev = 1.70782512766

        self.assertEqual(mean_rows.tolist(), expected_mean_rows)
        self.assertEqual(var_columns.tolist(), expected_var_columns)
        self.assertAlmostEqual(std_dev, expected_std_dev, places=11)

    def test_calculate_statistics_single_element(self):
        with unittest.mock.patch('builtins.input', side_effect=["1 1", "42"]):
            mean_rows, var_columns, std_dev = calculate_statistics()

        expected_mean_rows = [42.0]
        expected_var_columns = [0.0]
        expected_std_dev = 0.0

        self.assertEqual(mean_rows.tolist(), expected_mean_rows)
        self.assertEqual(var_columns.tolist(), expected_var_columns)
        self.assertAlmostEqual(std_dev, expected_std_dev, places=11)

if __name__ == '__main__':
    unittest.main()
