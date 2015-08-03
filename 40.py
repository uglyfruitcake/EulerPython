import my_module


digitlist = []
for i in xrange(1, 1000000):
    digits = my_module.array_of_digits(i)
    for n in digits:
        digitlist.append(n)
product = 1
for i in range(1, 7):
    product *= digitlist[(10 ** i) - 1]
print(product)
