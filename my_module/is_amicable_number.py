import my_module


def is_amicable_number(a):
    b = sum(my_module.get_proper_divisors(a))
    if a == sum(my_module.get_proper_divisors(b)):
        return True
    else:
        return False
