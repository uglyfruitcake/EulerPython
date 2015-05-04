import my_module
import collections


def nth_lexicographic_permutation(n):
    permutations = []
    i = 123456789
    while len(permutations) != n:
        ilist = my_module.array_of_digits(i)
        if 0 not in ilist:
            if [x for x, y in collections.Counter(ilist).items() if y > 1] == []:
                permutations.append(i)
        i += 1
    i = 1023456789
    while len(permutations) != n:
        ilist = my_module.array_of_digits(i)
        if [x for x, y in collections.Counter(ilist).items() if y > 1] == []:
                permutations.append(i)
        i += 1
    return(permutations[n-1])
