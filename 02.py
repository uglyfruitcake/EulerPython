import my_module
sum = 0
even_fibonacci = my_module.generate_even_fibonacci(1, 2, 4000000)
for i in even_fibonacci:
    sum += i
print sum
