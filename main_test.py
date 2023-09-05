import unittest

from main import remove_duplicates, is_balanced


class TestFunctions(unittest.TestCase):

    def test_remove_duplicates(self):
        input_sequence1 = [2, 3, 2, 4, 5, 3, 6, 7, 5]
        result1 = remove_duplicates(input_sequence1)

        input_sequence2 = [3, 3, 5, 6, 7, 2, 3, 5, 6, 6, 7, 7]
        result2 = remove_duplicates(input_sequence2)

        self.assertEqual(result1, [2, 3, 4, 5, 6, 7])
        self.assertEqual(result2, [3, 5, 6, 7, 2])

    def test_is_balanced(self):
        expression1 = "([]{})"
        expression2 = "([)]"
        expression3 = "{[()]}"
        expression4 = "({[]})"

        self.assertTrue(is_balanced(expression1))
        self.assertFalse(is_balanced(expression2))
        self.assertTrue(is_balanced(expression3))
        self.assertTrue(is_balanced(expression4))


if __name__ == '__main__':
    unittest.main()
