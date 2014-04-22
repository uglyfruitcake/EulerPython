import my_module

triangular_numbers = my_module.generate_triangular_numbers(100000000)
for i in triangular_numbers:
    if my_module.num_factors(i) > 500:
        print i
