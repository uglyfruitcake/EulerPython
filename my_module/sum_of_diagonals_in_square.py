def sum_of_diagonals_in_square(size):
    diagonal_sum = 1
    for i in xrange(3, size + 1, 2):
        diagonal_sum += (4 * (i ** 2)) - (6 * (i - 1))
    return(diagonal_sum)
