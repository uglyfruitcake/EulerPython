import my_module


def is_list_prime(primelist):
    for i in primelist:
        if not my_module.is_prime(i):
            return(False)
    return(True)
