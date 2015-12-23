import my_module
import sys


def getbins(length):
    bins = []
    for i in range(1, (2 ** length) - 1):
        a = ("".join(([str(x) for x in bin(i)[2:]])))
        bins.append(a.zfill(length))
    return(bins)

def getfamilies(n):
    n = list(n)
    bins = getbins(len(n))
    families = []
    for b in bins:
        family = []
        for i in range(len(n)):
            if b[i] == "1":
                family.append("*")
            else:
                family.append(n[i])
        families.append(family)
    return(families)

def getfamilymembers(n):
    families = getfamilies(n)
    familymembers = []
    for i in families:
        family = []
        for x in range(1, 10):
            member = []
            for digit in i:
                if digit == "*":
                    member.append(str(x))
                else:
                    member.append(digit)
            family.append("".join(member))
        familymembers.append(family)
    return(familymembers)

primes = (my_module.generate_prime(10, 130000))

for i in primes:
    for family in getfamilymembers(str(i)):
        count = 0
        for n in family:
            if my_module.is_prime(int(n)):
                count += 1
        if count == 8:
            print(min(family))
            sys.exit()
