import my_module


answer = 0
for i in xrange(10, 1000000):
    total = 0
    for digit in my_module.array_of_digits(i):
        total += digit ** 5
    if total == i:
        answer += i

print(answer)
