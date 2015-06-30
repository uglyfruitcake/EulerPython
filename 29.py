values = []
for a in xrange(2, 101):
    for b in xrange(2, 101):
        values.append(a ** b)

print(len(list(set(values))))
