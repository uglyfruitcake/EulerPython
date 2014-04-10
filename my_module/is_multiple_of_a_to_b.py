def is_multiple_of_a_to_b(n, lower_bound, upper_bound):
    multiple = True
    for i in xrange(lower_bound, upper_bound + 1):
        if n % i != 0:
            multiple = False

    return multiple
