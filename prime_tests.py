import unittest
from prime import generate_prime_numbers


class PrimeNumberTestCases(unittest.TestCase):
    def test_for_correct_answer_including_number(self):
        result = generate_prime_numbers(11)
        self.assertEqual(result, [1, 2, 3, 5, 7, 11], msg='Incorrect answers')

    def test_only_list_returned(self):
        result = generate_prime_numbers(9)
        self.assertEqual(type(result), list, msg='Invalid output')

    def test_for_not_allowing_non_integer(self):
        with self.assertRaises(ValueError) as context:
            generate_prime_numbers('string')
            self.assertEqual(
                "The provided input is not an integer.",
                context.exception.message, "Invalid input not allowed"
            )

    def test_for_negative_values(self):
        result = generate_prime_numbers(-3)
        self.assertEqual(result, [], msg='It should return an empty list for negative times.')

    def test_for_when_no_variable_is_passed(self):
        with self.assertRaises(ValueError) as context:
            generate_prime_numbers()
            self.assertEqual(
                "Provide an integer.",
                context.exception.message, "Invalid input not allowed"
            )


if __name__ == '__main__': unittest.main()
