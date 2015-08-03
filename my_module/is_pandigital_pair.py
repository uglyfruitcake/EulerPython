import my_module


def is_pandigital_pair(a, b):
    digits = my_module.array_of_digits(a*b)
    digits.extend(int(i) for i in str(a))
    digits.extend(int(i) for i in str(b))
    if len(digits) == 9:
        if 0 not in digits:
            if len(list(set(digits))) == 9:
                return(True)
    return(False)
