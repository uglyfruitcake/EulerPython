import my_module

units = ["", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
         "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
total_length = 0

for i in xrange(1, 1001):
    if i < 20:
        total_length += len(units[i])
    elif i < 100:
        digits = my_module.array_of_digits(i)
        total_length += len(tens[digits[0]-2])
        total_length += len(units[digits[1]])
    else:
        digits = my_module.array_of_digits(i)
        if i == 1000:
            total_length += 11
        elif i % 100 == 0:
            total_length += (len(units[digits[0]])+7)
        elif i - digits[0]*100 < 20:
            total_length += len(units[i - digits[0]*100])
            total_length += len(units[digits[0]]) + 10
        else:
            total_length += len(tens[digits[1]-2])
            total_length += len(units[digits[2]])
            total_length += len(units[digits[0]]) + 10

print(total_length)
