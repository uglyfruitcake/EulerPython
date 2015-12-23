import my_module

maxi = 0
for a in range (1, 100):
    for b in range(1, 100):
        power = a**b
        digits = my_module.array_of_digits(power)
        if sum(digits) > maxi:
            maxi = sum(digits)

print(maxi)
