def largest_product_of_consecutive_integers_in_array(array, number_of_ints):
    lower_bound = 0
    upper_bound = number_of_ints
    n = 1
    largest_sum = 0

    while lower_bound < len(array) - number_of_ints + 1:
        for i in array[lower_bound:upper_bound]:
            n *= i
        if n > largest_sum:
            largest_sum = n
        lower_bound += 1
        upper_bound += 1
        n = 1
    return largest_sum
