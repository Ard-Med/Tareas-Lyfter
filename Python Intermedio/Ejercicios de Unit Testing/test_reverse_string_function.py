import unittest

from reverse_string_function import return_function


class TestReturnFunction(unittest.TestCase):

    def test_simple_word(self):
        self.assertEqual(return_function("hello"), "olleh")

    def test_sentence_with_spaces_and_punctuation(self):
        self.assertEqual(return_function("Hello, World!"), "!dlroW ,olleH")

    def test_empty_string(self):
        self.assertEqual(return_function(""), "")

    def test_single_character(self):
        self.assertEqual(return_function("a"), "a")

    def test_palindrome(self):
        self.assertEqual(return_function("radar"), "radar")

    def test_original_example_string(self):
        result = return_function("you were just like me, trying to make history")
        self.assertEqual(result, "yrotsih ekam ot gniyrt ,em ekil tsuj erew uoy")

    def test_reversing_twice_gives_original(self):
        original = "Python is fun"
        self.assertEqual(return_function(return_function(original)), original)


if __name__ == "__main__":
    unittest.main()