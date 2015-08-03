import my_module


def is_pandigital_number(n):
    digits = my_module.array_of_digits(n)
    if len(digits) == 9:
        if 0 not in digits:
            if len(list(set(digits))) == 9:
                return(True)
    return(False)

pandigitals = []
for i in xrange(9000, 10000):
    if is_pandigital_number(str(i) + str(i * 2)):
        pandigitals.append(str(i) + str(i * 2))

print(pandigitals)
