import my_module


def is_circular_prime(n):
    if my_module.is_prime(n):
        rotations = my_module.get_rotations(n)
        if my_module.is_list_prime(rotations):
            return(True)
    return(False)
