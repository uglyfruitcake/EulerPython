total = 0
for i in xrange(1, 1001):
    total += (i ** i)
print("".join([i for i in str(total)][-10:]))
