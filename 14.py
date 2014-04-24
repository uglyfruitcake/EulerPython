import my_module

largest_sequence = 0
largest_sequence_number = 0
for i in xrange(2, 1000000):
    if my_module.collatz_sequence_length(i) > largest_sequence:
        largest_sequence = my_module.collatz_sequence_length(i)
        largest_sequence_number = i
print largest_sequence_number
