import unittest

from main import remove_duplicates, is_balanced, word_frequency


class TestFunctions(unittest.TestCase):

    def test_remove_duplicates(self):
        input_sequence1 = [2, 3, 2, 4, 5, 3, 6, 7, 5]
        result1 = [2, 3, 4, 5, 6, 7]

        input_sequence2 = [3, 3, 5, 6, 7, 2, 3, 5, 6, 6, 7, 7]
        result2 = [3, 5, 6, 7, 2]

        self.assertEqual(remove_duplicates(input_sequence1), result1)
        self.assertEqual(remove_duplicates(input_sequence2), result2)

    def test_is_balanced(self):
        expression1 = "([]{})"
        expression2 = "([)]"
        expression3 = "{[()]}"
        expression4 = "({[]})"

        self.assertTrue(is_balanced(expression1))
        self.assertFalse(is_balanced(expression2))
        self.assertTrue(is_balanced(expression3))
        self.assertTrue(is_balanced(expression4))

    def test_word_frequency(self):
        sentence1 = "This is a test sentence. This sentence is a test."
        result1 = {'this': 2, 'is': 2,
                   'a': 2, 'test': 2, 'sentence': 2}

        sentence2 = "The quick brown fox jumps over the lazy dog."
        result2 = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1,
                   'jumps': 1, 'over': 1,   'lazy': 1, 'dog': 1}

        self.assertEqual(word_frequency(sentence1), result1)
        self.assertEqual(word_frequency(sentence2), result2)


if __name__ == '__main__':
    unittest.main()
