import urllib2
import string
import my_module


count = 0
alphabet = string.ascii_uppercase
file = urllib2.urlopen(
    "https://projecteuler.net/project/resources/p042_words.txt")
words = file.readline().replace("\"", "").split(",")
triangular_numbers = my_module.generate_triangular_numbers(500)
for word in words:
    total = 0
    for letter in word:
        total += alphabet.index(letter)+1
    if total in triangular_numbers:
        count += 1
print(count)
