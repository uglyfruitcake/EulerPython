import my_module


abundantnumbers = my_module.generate_abundant_number(28123)
abundantsums = []
total = 0
for i in abundantnumbers:
    for j in abundantnumbers:
        abundantsums.append(i + j)
for i in xrange(1, 28123):
    if i not in abundantsums:
        total += i
print(total)
