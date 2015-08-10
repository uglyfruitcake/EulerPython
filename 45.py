import my_module


for i in xrange(286, 1000000):
    if my_module.is_pentagonal_number(my_module.nth_triangular_number(i)):
        if my_module.is_hexagonal_number(my_module.nth_triangular_number(i)):
            print(my_module.nth_triangular_number(i))
