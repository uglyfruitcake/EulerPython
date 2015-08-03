import my_module


def is_pandigital_number(n):
    digits = my_module.array_of_digits(n)
    if 0 not in digits:
        if len(list(set(digits))) == len(digits):
            return(True)
    return(False)
