import urllib2,string

totalscore = 0
alphabet = string.ascii_uppercase
file = urllib2.urlopen("https://projecteuler.net/project/resources/p022_names.txt")
names = file.readline().replace("\"","").split(",")
names.sort()
for name in names:
    score = 0
    for letter in name:
        score += alphabet.index(letter)+1
    score *= names.index(name)+1
    totalscore += score
print (totalscore)
