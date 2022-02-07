import unittest
from even_numbers import EvenNumber


class TestEvenNumbers(unittest.TestCase):

    def test_is_empty(self):
        my_list = EvenNumber.create_list_of_numbers(self, list_size=0)
        self.assertEqual(len(my_list), 0)

    def test_is_even(self):
        used_numbers = EvenNumber.choose_even_numbers_only(self, created_numbers=[4, 6, 8])
        self.assertEqual(len(used_numbers), 3)

    def test_is_odd(self):
        used_numbers = EvenNumber.choose_even_numbers_only(self, created_numbers=[1, 3, 5])
        self.assertEqual(len(used_numbers), 0)

    def test_is_mix_of_odd_and_even(self):
        used_numbers = EvenNumber.choose_even_numbers_only(self, created_numbers=[1, 2, 4, 11, 22, 42])
        self.assertEqual(len(used_numbers), 4)


if __name__ == '__main__':
    unittest.main()
