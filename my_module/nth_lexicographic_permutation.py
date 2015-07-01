import itertools

def nth_lexicographic_permutation(n):
    x = itertools.permutations('0123456789', 10)
    counter = 0
    for i in x:
        counter += 1
        if counter == n:
            return(i)
