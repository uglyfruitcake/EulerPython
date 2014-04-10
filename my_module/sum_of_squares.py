def sum_of_squares(lower_bound, upper_bound):
    sum = 0
    for i in xrange(lower_bound, upper_bound+1):
        sum += i**2
    return sum
