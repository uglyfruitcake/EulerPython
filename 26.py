import my_module


lengths = []
for d in range(2, 1001):
    lengths.append(my_module.cycle_length(d))
print(lengths.index(max(lengths)) + 2)
