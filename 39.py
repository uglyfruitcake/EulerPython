import my_module


sums = []
for a in xrange(1, 1000):
    for b in xrange(1, 1000):
        for c in xrange(1, 1000):
            if a + b + c < 1000:
                if my_module.is_pythagorean_triple(a, b, c):
                    sums.append(a + b + c)
print(max(set(sums), key=sums.count))
