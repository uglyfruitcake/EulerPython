import my_module


def generate_even_fibonacci(first_seed, second_seed, max_value):
    even_fibonacci = []
    for i in my_module.generate_fibonacci(first_seed, second_seed, max_value):
        if my_module.is_even(i):
            even_fibonacci.append(i)
    return even_fibonacci
