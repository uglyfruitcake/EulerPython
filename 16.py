import my_module

power = 2**1000
array = my_module.array_of_digits(power)
sum = 0

for i in array:
    sum += i

print sum
