import unittest
from io import StringIO
from unittest.mock import patch

from prime_number import check_for_prime_number


class TestCheckForPrimeNumber(unittest.TestCase):

    def test_prime_numbers_only(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_for_prime_number([2, 3, 5, 7, 11])
            output = fake_out.getvalue().strip()
        self.assertEqual(output, "prime: [2, 3, 5, 7, 11] not prime: []")

    def test_mix_of_primes_and_non_primes(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_for_prime_number([4, 5, 6, 7, 8, 9])
            output = fake_out.getvalue().strip()
        self.assertEqual(output, "prime: [5, 7] not prime: [4, 6, 8, 9]")

    def test_non_prime_numbers_only(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_for_prime_number([4, 6, 8, 9, 10])
            output = fake_out.getvalue().strip()
        self.assertEqual(output, "prime: [] not prime: [4, 6, 8, 9, 10]")


if __name__ == "__main__":
    unittest.main()