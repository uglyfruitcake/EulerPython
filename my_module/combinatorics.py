import my_module


def combinatorics(n, r):
    return(my_module.factorial(n)/(my_module.factorial(r)*my_module.factorial(n - r)))
