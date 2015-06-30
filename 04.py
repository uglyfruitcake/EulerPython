import my_module


palindromes = []

for a in range(100, 1000):
    for b in range(100, 1000):
        number = a * b
        if my_module.is_palindrome(number):
            palindromes.append(number)

print max(palindromes)
