import my_module


differences = []
for a in xrange(1, 3000):
    for b in xrange(1, 3000):
        if a > b:
            if my_module.is_pentagonal_number(my_module.nth_pentagonal_number(a) + my_module.nth_pentagonal_number(b)):
                if my_module.is_pentagonal_number(my_module.nth_pentagonal_number(a) - my_module.nth_pentagonal_number(b)):
                    differences.append(my_module.nth_pentagonal_number(a) - my_module.nth_pentagonal_number(b))
print(max(differences))
