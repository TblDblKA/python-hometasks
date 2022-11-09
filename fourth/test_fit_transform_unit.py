import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_numbers(self):
        actual = fit_transform('[1, 2, 3, 2, 0]')
        expected = [(1, [0, 0, 0, 1]), (2, [0, 0, 1, 0]), (3, [0, 1, 0, 0]), (2, [0, 0, 1, 0]), (0, [1, 0, 0, 0])]
        self.assertNotEqual(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_str(self):
        actual = fit_transform('abc')
        expected = [('abc', [1])]
        self.assertEqual(actual, expected)

    def test_fruits(self):
        fruits = ['Apple', 'Orange', 'Apple', 'Pineapple', 'Melon', 'Tangerine']
        transformed_fruits = fit_transform(fruits)
        value = ('Pineapple', [0, 0, 1, 0, 0])
        self.assertIn(value, transformed_fruits)
