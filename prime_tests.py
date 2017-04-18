import unittest
from prime import generate_prime_numbers


class PrimeNumberTestCases(unittest.TestCase):
    def test_for_correct_answer_including_number(self):
        result = generate_prime_numbers(11)
        self.assertEqual(result, [1, 2, 3, 5, 7, 11], msg='Incorrect answers')

    def test_only_list_returned(self):
        result = generate_prime_numbers(9)
        self.assertEqual(type(result), list, msg='Invalid output')


if __name__ == '__main__': unittest.main()
