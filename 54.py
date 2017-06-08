hands = open("provided\hands.txt", 'r')
convert = {"T":"10", "J":"11", "Q":"12", "K":"13", "A":"14"}

def isstraight(numbers):
    straight = [9, 10, 11, 12, 13]
    for i in range(0, 9):
        straightnumbers = [i + j for j in numbers]
        if straightnumbers == straight:
            return((True, i))
    return((False, 0))

def rating(hand):
    rating = 0
    numbers = sorted([card[0] for card in hand])
    suits = [card[1] for card in hand]
    freqnumbers = sorted(numbers,key=numbers.count,reverse=True)
    f0 = freqnumbers[0]
    f1 = freqnumbers[1]
    f2 = freqnumbers[2]
    f3 = freqnumbers[3]
    f4 = freqnumbers[4]
    shape = (freqnumbers.count(f0), freqnumbers.count(f3), freqnumbers.count(f4))
    straight = isstraight(numbers)
    flush = suits.count(suits[0]) == 5

    #Straight flush
    if straight[0] and flush:
        rating += 7453
        rating += (9 - straight[1])
        return(rating)
    #4 of a kind
    if shape == (4, 4, 1):
        rating += 7297
        rating += (f0-1) * 12
        rating += f4
        if f4 > f0:
            rating -= 1
        return(rating)
    #Full house
    if shape == (3, 2, 2):
        rating += 7141
        rating += f0 * 12
        rating -= (12-f4)
        if f4 > f0:
            rating -= 1
        return(rating)
    #Flush
    if flush:
        rating += 5863
        rating += (f4 - 5) * (f4 - 4) * (f4 - 3) * (f4 - 2) * (f4 - 1) / 120
        rating += (f3 - 4) * (f3 - 3) * (f3 - 2) * (f3 - 1) / 24
        rating += (f2 - 3) * (f2 - 2) * (f2 - 1) / 6
        rating += (f1 - 2) * (f1 - 1) / 2
        rating += f0
        rating -= (f4 - 5)
        return(rating)
    #Straight
    if straight[0]:
        rating += 5854
        rating += (9 - straight[1])
        return(rating)
    #Triple
    if shape == (3, 1, 1):
        if f3 > f0:
            f3 -= 1
            f4 -= 1
        elif f4 > f0:
            f4 -= 1
        rating += 4996
        rating += (f0 - 1) * 66
        rating += (f4 - 1) * (f4 - 2) / 2
        rating += f3
        return(rating)
    #Double pair
    if shape == (2, 2, 1):
        if f4 > f3:
            f4 -= 2
        elif f4 > f0:
            f4 -= 1
        rating += 4138
        rating += (f3 - 2) * (f3 - 1) / 2
        rating += (f0 - 1) * 11
        rating += f4
        return(rating)
    #Pair
    if shape == (2, 1, 1):
        if f2 > f0:
            f2 -= 1
            f3 -= 1
            f4 -= 1
        elif f3 > f0:
            f3 -= 1
            f4 -= 1
        elif f4 > f0:
            f4 -= 1
        rating += 1278
        rating += (f0 - 1) * 220
        rating += (f4 - 3) * (f4 - 2) * (f4 - 1) / 6
        rating += (f3 - 2) * (f3 - 1) / 2
        rating += f2
        return(rating)
    #High Card
    else:
        rating += (f4 - 5) * (f4 - 4) * (f4 - 3) * (f4 - 2) * (f4 - 1) / 120
        rating += (f3 - 4) * (f3 - 3) * (f3 - 2) * (f3 - 1) / 24
        rating += (f2 - 3) * (f2 - 2) * (f2 - 1) / 6
        rating += (f1 - 2) * (f1 - 1) / 2
        rating += f0
        rating -= (f4 - 5)
        return(rating)

score = 0

for hand in hands.readlines():
    hand = [convert[x] if x in convert else x for x in hand]
    hand = [int(x) - 1 if x.isdigit() else x for x in hand]
    while " " in hand:
        hand.remove(" ")
    hand = tuple(zip(hand[0::2], hand[1::2]))
    if rating(hand[:5]) > rating(hand[5:]):
        score += 1

print(score)
