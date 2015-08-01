import my_module
import itertools

def is_list_prime(primelist):
    for i in primelist:
        if not my_module.is_prime(i):
            return(False)
    return(True)


def get_rotations(n):
    rotations = []
    for i in xrange(len(str(n))):
        rotations.append(int(str(n)[i:] + str(n)[0:i]))
    return(rotations)


def is_circular_prime(n):
    if my_module.is_prime(n):
        rotations = get_rotations(n)
        if is_list_prime(rotations):
            return(True)
    return(False)


count = 0
for i in xrange(1, 1000001):
    if is_circular_prime(i):
        count += 1
print(count)
