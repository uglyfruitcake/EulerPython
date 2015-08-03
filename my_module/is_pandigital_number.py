import my_module


def is_pandigital_number(n):
    digits = my_module.array_of_digits(n)
    if len(digits) == 9:
        if 0 not in digits:
            if len(list(set(digits))) == 9:
                return(True)
    return(False)
