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
        self.assertEqual(my_module.generate_prime(2, 11), [2, 3, 5, 7])

class test_generate_triangular_numbers(unittest.TestCase):
    def test_generate_triangular_numbers(self):
        self.assertEqual(my_module.generate_triangular_numbers(0), [])
        self.assertEqual(my_module.generate_triangular_numbers(2), [1, 3])
        self.assertEqual(my_module.generate_triangular_numbers(11), [1, 3, 6, 10, 15])


class test_get_proper_devisors(unittest.TestCase):
    def test_get_proper_devisors(self):
        self.assertEqual(my_module.get_proper_divisors(220), [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
        self.assertEqual(my_module.get_proper_divisors(2), [1])


class test_is_amicable_number(unittest.TestCase):
    def test_is_amicable_number(self):
        self.assertTrue(my_module.is_amicable_number(220))
        self.assertFalse(my_module.is_amicable_number(1))


class test_is_factor(unittest.TestCase):
    def test_is_factor(self):
        self.assertTrue(my_module.is_factor(2, 4))
        self.assertFalse(my_module.is_factor(5, 7))
        self.assertTrue(my_module.is_factor(193, 193))


class test_is_in_array(unittest.TestCase):
    def test_is_in_array(self):
        self.assertTrue(my_module.is_in_array(2, ["n", 2]))
        self.assertFalse(my_module.is_in_array(6, ["n", "6"]))


class test_is_multiple_of_a_to_b(unittest.TestCase):
    def test_is_multiple_of_a_to_b(self):
        self.assertTrue(my_module.is_multiple_of_a_to_b(2520, 1, 10))
        self.assertFalse(my_module.is_multiple_of_a_to_b(10, 1, 4))


class test_is_palindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(my_module.is_palindrome(5))
        self.assertTrue(my_module.is_palindrome(57975))
        self.assertTrue(my_module.is_palindrome(5445))
        self.assertFalse(my_module.is_palindrome(57585))


class test_is_prime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(my_module.is_prime(1))
        self.assertTrue(my_module.is_prime(2))
        self.assertTrue(my_module.is_prime(193))
        self.assertFalse(my_module.is_prime(49))


class test_is_pythagorean_triple(unittest.TestCase):
    def test_is_pythagorean_triple(self):
        self.assertTrue(my_module.is_pythagorean_triple(3, 4, 5))
        self.assertFalse(my_module.is_pythagorean_triple(1, 1, 2))


class test_largest_product_of_consecutive_integers_in_array(unittest.TestCase):
    def test_largest_product_of_consecutive_integers_in_array(self):
        self.assertEqual(my_module.largest_product_of_consecutive_integers_in_array([1, 2, 3, 4, 5, 6], 3), 120)


class test_largest_sum_route_in_triangle(unittest.TestCase):
    def test_largest_sum_route_in_triangle(self):
        self.assertEqual(my_module.largest_sum_route_in_triangle([[6], [5, 4], [2, 3, 5]]), 15)


class test_nth_prime(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(my_module.nth_prime(7), 17)


class test_num_factors(unittest.TestCase):
    def test_num_factors(self):
        self.assertEqual(my_module.num_factors(1), 1)
        self.assertEqual(my_module.num_factors(64), 7)


class test_number_of_ways_across_square(unittest.TestCase):
    def test_number_of_ways_across_square(self):
        self.assertEqual(my_module.number_of_ways_across_square(3), 6)


class test_square_of_sum(unittest.TestCase):
    def test_square_of_sum(self):
        self.assertEqual(my_module.square_of_sum(1, 3), 36)


class test_sum_of_factorial_digits(unittest.TestCase):
    def test_sum_of_factorial_digits(self):
        self.assertEqual(my_module.sum_of_factorial_digits(6), 9)


class test_sum_of_squares(unittest.TestCase):
    def test_sum_of_squares(self):
        self.assertEqual(my_module.sum_of_squares(1, 3), 14)


class test_generate_abundant_number(unittest.TestCase):
    def test_generate_abundant_number(self):
        self.assertEqual(my_module.generate_abundant_number(30), [12, 18, 20, 24, 30])


class test_nth_lexicographic_permutation(unittest.TestCase):
    def test_nth_lexicographic_permutation(self):
        self.assertEqual(my_module.nth_lexicographic_permutation(1), ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
        self.assertEqual(my_module.nth_lexicographic_permutation(100), ("0", "1", "2", "3", "4", "9", "5", "7", "8", "6"))


class test_cycle_length(unittest.TestCase):
    def test_cycle_length(self):
        self.assertEqual(my_module.cycle_length(7), 6)
        self.assertEqual(my_module.cycle_length(17), 16)
        self.assertEqual(my_module.cycle_length(8), 0)


class test_consecutive_primes_from_quadratic(unittest.TestCase):
    def test_consecutive_primes_from_quadratic(self):
        self.assertEqual(my_module.consecutive_primes_from_quadratic(1, 41), 40)


class test_sum_of_diagonals_in_square(unittest.TestCase):
    def test_sum_of_diagonals_in_square(self):
        self.assertEqual(my_module.sum_of_diagonals_in_square(5), 101)


class test_is_pandigital_pair(unittest.TestCase):
    def test_is_pandigital_pair(self):
        self.assertTrue(my_module.is_pandigital_pair(39, 186))
        self.assertFalse(my_module.is_pandigital_pair(1, 9671))


class test_is_circular_prime(unittest.TestCase):
    def test_is_circular_prime(self):
        self.assertTrue(my_module.is_circular_prime(197))
        self.assertFalse(my_module.is_circular_prime(53))


class test_is_list_prime(unittest.TestCase):
    def test_is_list_prime(self):
        self.assertTrue(my_module.is_list_prime([2, 5, 197]))
        self.assertFalse(my_module.is_list_prime([2, 5, 9]))


class test_get_rotations(unittest.TestCase):
    def test_get_rotations(self):
        self.assertEqual(my_module.get_rotations(197), [197, 971, 719])


class test_is_truncatable_prime(unittest.TestCase):
    def test_is_truncatable_prime(self):
        self.assertTrue(my_module.is_truncatable_prime(3797))
        self.assertFalse(my_module.is_truncatable_prime(29))


class test_is_pandigital_number(unittest.TestCase):
    def test_is_pandigital_number(self):
        self.assertTrue(my_module.is_pandigital_number(123456789))


class test_is_pentagonal_number(unittest.TestCase):
    def test_is_pentagonal_number(self):
        self.assertTrue(my_module.is_pentagonal_number(145))
        self.assertFalse(my_module.is_pentagonal_number(467))


class test_nth_pentagonal_number(unittest.TestCase):
    def test_nth_pentagonal_number(self):
        self.assertEqual(my_module.nth_pentagonal_number(3), 12)


class test_nth_triangular_number(unittest.TestCase):
    def test_nth_triangular_number(self):
        self.assertEqual(my_module.nth_triangular_number(285), 40755)


class test_is_hexagonal_number(unittest.TestCase):
    def test_is_hexagonal_number(self):
        self.assertTrue(my_module.is_hexagonal_number(40755))


class test_is_goldback_composite(unittest.TestCase):
    def test_is_goldback_composite(self):
        self.assertTrue(my_module.is_goldback_composite(493))


class test_get_distinct_prime_factors(unittest.TestCase):
    def test_get_distinct_prime_factors(self):
        self.assertEqual(my_module.get_distinct_prime_factors(12), [2, 3])


class test_factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(my_module.factorial(5), 120)


class test_combinatorics(unittest.TestCase):
    def test_combinatorics(self):
        self.assertEqual(my_module.combinatorics(5, 3), 10)
