import my_module


answer = 0
while answer == 0:
    for a in xrange(1, 1000):
        for b in xrange(1, 1000):
            for c in xrange(1, 1000):
                if my_module.is_pythagorean_triple(a, b, c):
                    if a + b + c == 1000:
                        answer = a * b * c

print answer
