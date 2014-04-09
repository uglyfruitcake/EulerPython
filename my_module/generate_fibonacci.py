def generate_fibonacci(first_seed, second_seed, max_value):
    array = [first_seed, second_seed]
    while first_seed + second_seed < max_value:
        array.append(first_seed + second_seed)
        second_seed = first_seed + second_seed
        first_seed = second_seed - first_seed
    return array
