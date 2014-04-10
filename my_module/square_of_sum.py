def square_of_sum(lower_bound, upper_bound):
    total = 0
    for i in xrange(lower_bound, upper_bound+1):
        total += i
    return total**2