from __future__ import division
from fractions import Fraction
import my_module


fractions = []
for a in xrange(10, 100):
    for b in xrange(10, 100):
        if a < b:
            list_a = my_module.array_of_digits(a)
            list_b = my_module.array_of_digits(b)
            if 0 not in list_a:
                if 0 not in list_b:
                    for i in xrange(0, 2):
                        if list_a[i] == list_b[1 - i]:
                            if a / b == list_a[1 - i] / list_b[i]:
                                fractions.append(a)
                                fractions.append(b)

productnumerator = 1
productdenominator = 1
for j in xrange(0, 7, 2):
    productnumerator *= fractions[j]
    productdenominator *= fractions[j + 1]

print(Fraction(productnumerator, productdenominator).denominator)
