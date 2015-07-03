import my_module


products = []
for a in xrange(10, 100):
    for b in xrange(100, 1000):
        if my_module.is_pandigital_pair(a, b):
            products.append(a*b)

for a in xrange(1, 10):
    for b in xrange(1000, 10000):
        if my_module.is_pandigital_pair(a, b):
            products.append(a*b)

print(sum(list(set(products))))
