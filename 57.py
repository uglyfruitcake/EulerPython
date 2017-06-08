from decimal import Decimal

previous = 0
denominator = 1
count = 0

for i in range(1, 1001):
    denominator = Decimal(2*denominator + previous)
    previous = Decimal((denominator - previous)/2)
    numerator = Decimal(previous + denominator)
    if len(str(int(numerator))) - len(str(int(denominator))) == 1:
        count += 1

print(count)
