import my_module


def is_truncatable_prime(n):
    if not my_module.is_prime(n):
        return(False)
    for i in xrange(1, len(str(n))):
        if not my_module.is_prime(int(str(n)[:i])):
            return(False)
        if not my_module.is_prime(int(str(n)[i:])):
            return(False)
    return(True)
