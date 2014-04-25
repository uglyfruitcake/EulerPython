import my_module

number = 1
answer = 0

while answer == 0:
    if my_module.is_multiple_of_a_to_b(number, 1, 20):
        answer = number
    else:
        number += 1

print answer
