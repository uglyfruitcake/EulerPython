def is_multiple_of_a_to_b(n, lower_bound, upper_bound):
    for i in xrange(lower_bound, upper_bound + 1):
        if n % i != 0:
            return(False)
    return(True)
