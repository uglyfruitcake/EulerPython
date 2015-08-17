import my_module


def rearrange(i):
    return(sorted(list(set(my_module.array_of_digits(i)))))

for i in xrange(1, 1000000):
    if rearrange(i) == rearrange(2 * i):
        if rearrange(i) == rearrange(3 * i):
            if rearrange(i) == rearrange(4 * i):
                if rearrange(i) == rearrange(5 * i):
                    if rearrange(i) == rearrange(6 * i):
                        print(i)
                        break
