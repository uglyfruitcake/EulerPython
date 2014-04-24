import my_module


def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if my_module.is_even(n):
            n = n / 2
        else:
            n = n * 3 + 1
        length += 1
    return length
