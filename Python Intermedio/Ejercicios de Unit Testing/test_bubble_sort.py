import unittest
import random

from bubble_sort_ut import bubble_sort_right_to_left


class TestBubbleSortRightToLeft(unittest.TestCase):

    def test_small_list(self):
        arr = [5, 3, 8, 1, 2]
        result = bubble_sort_right_to_left(arr)
        self.assertEqual(result, [1, 2, 3, 5, 8])

    def test_big_list(self):
        random.seed(13)
        arr = [random.randint(-1000, 1000) for _ in range(500)] 
        expected = sorted(arr)
        result = bubble_sort_right_to_left(arr)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        arr = []
        result = bubble_sort_right_to_left(arr)
        self.assertEqual(result, [])

    def test_parameter_not_in_list(self):
        invalid_parameters = [42, 3.14, None, "string", (3, 2, 1)]
        for parameter in invalid_parameters:
            with self.subTest(parameter=parameter):
                with self.assertRaises(TypeError):
                    bubble_sort_right_to_left(parameter)


if __name__ == "__main__":
    unittest.main()