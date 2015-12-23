import my_module

count = 0
for n in range(1, 10000):
    for i in range(50):
        n += int(str(n)[::-1])
        if my_module.is_palindrome(n):
            count += 1
            break

print(9999 - count)
