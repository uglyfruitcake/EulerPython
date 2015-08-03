import my_module


pandigitals = []
for i in xrange(9000, 10000):
    if my_module.is_pandigital_number(str(i) + str(i * 2)):
        pandigitals.append(str(i) + str(i * 2))
print(max(pandigitals))
