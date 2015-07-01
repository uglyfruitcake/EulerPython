import my_module


products = []
for a in xrange(10, 100):
    for b in xrange(100, 1000):
        digits = my_module.array_of_digits(a*b)
        if len(digits) == 4:
            digits.extend(int(i) for i in str(a))
            digits.extend(int(i) for i in str(b))
            if 0 not in digits:
                if len(list(set(digits))) == 9:
                    products.append(a*b)
                    print(products)

for a in xrange(1, 10):
    for b in xrange(1000, 10000):
        digits = my_module.array_of_digits(a*b)
        if len(digits) == 4:
            digits.extend(int(i) for i in str(a))
            digits.extend(int(i) for i in str(b))
            if 0 not in digits:
                if len(list(set(digits))) == 9:
                    products.append(a*b)
                    print(products)

print(sum(list(set(products))))
