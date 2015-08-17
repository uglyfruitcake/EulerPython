import my_module


total = 0
for n in xrange(1, 101):
    for r in xrange(1, 100):
        if n > r:
            if my_module.combinatorics(n, r) > 1000000:
                total += 1
print(total)
