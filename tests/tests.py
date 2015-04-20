import my_module
import unittest


class test_array_of_digits(unittest.TestCase):
    def test_array_of_digits(self):
        self.assertEqual(my_module.array_of_digits(3024), [3, 0, 2, 4])


class test_collatz_sequence_length(unittest.TestCase):
    def test_collatz_sequence_length(self):
        self.assertEqual(my_module.collatz_sequence_length(1), 1)
        self.assertEqual(my_module.collatz_sequence_length(3), 8)
        self.assertEqual(my_module.collatz_sequence_length(7), 17)


class test_generate_even_fibonacci(unittest.TestCase):
    def test_array_of_digits(self):
        self.assertEqual(my_module.generate_even_fibonacci(1, 1, 7), [2])
        self.assertEqual(my_module.generate_even_fibonacci(1, 3, 4), [])
        self.assertEqual(my_module.generate_even_fibonacci(1, 1, 35), [2, 8, 34])


class test_generate_fibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        self.assertEqual(my_module.generate_fibonacci(1, 1, 13), [1, 1, 2, 3, 5, 8])
        self.assertEqual(my_module.generate_fibonacci(3, 2, 31), [3, 2, 5, 7, 12, 19])


class test_generate_prime(unittest.TestCase):
    def test_generate_prime(self):
        self.assertEqual(my_module.generate_prime(11), [2, 3, 5, 7])

class test_generate_triangular_numbers(unittest.TestCase):
    def test_generate_triangular_numbers(self):
        self.assertEqual(my_module.generate_triangular_numbers(0), [])
        self.assertEqual(my_module.generate_triangular_numbers(2), [1, 3])
        self.assertEqual(my_module.generate_triangular_numbers(11), [1, 3, 6, 10, 15])


class test_get_proper_devisors(unittest.TestCase):
    def test_get_proper_devisors(self):
        self.assertEqual(my_module.get_proper_divisors(220), [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
