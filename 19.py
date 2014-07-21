months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0
suns = 0
asds = []
for y in xrange(1901, 2001):
    if y % 4 == 0:
        months[1] = 29
    if y % 100 == 0:
        months[1] = 28
    if y % 400 == 0:
        months[1] = 29
    for i in months:
        for m in xrange(1, i + 1):
            days += 1
            if m == 1:
                if days % 7 == 5:
                    suns += 1
print suns
