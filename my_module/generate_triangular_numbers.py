def generate_triangular_numbers(ceiling):
    number = 1
    triangular_number = 0
    triangular_numbers = []
    while triangular_number < ceiling:
        triangular_number += number
        triangular_numbers.append(triangular_number)
        number += 1
    return triangular_numbers
