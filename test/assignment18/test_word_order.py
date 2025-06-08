import unittest
from python_assignment.src.assignment18.util import word_occurrence_counter

class TestWordOccurrenceCounter(unittest.TestCase):
    def test_word_occurrence(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
        expected = {'apple': 3, 'banana': 2, 'orange': 1}
        result = word_occurrence_counter(words)
        self.assertEqual(list(result.keys()), list(expected.keys()))
        self.assertEqual(list(result.values()), list(expected.values()))

    def test_all_unique_words(self):
        words = ['a', 'b', 'c']
        expected = {'a': 1, 'b': 1, 'c': 1}
        result = word_occurrence_counter(words)
        self.assertEqual(list(result.keys()), list(expected.keys()))
        self.assertEqual(list(result.values()), list(expected.values()))

if __name__ == '__main__':
    unittest.main()
