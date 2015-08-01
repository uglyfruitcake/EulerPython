import my_module


palindromesum = 0
for i in xrange(1, 1000000):
    if my_module.is_palindrome(i):
        if my_module.is_palindrome(int(bin(i)[2:])):
            palindromesum += i

print(palindromesum)
