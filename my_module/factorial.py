def factorial(n):
    total = 1
    for i in xrange(1, n + 1):
        total *= i
    return(total)
