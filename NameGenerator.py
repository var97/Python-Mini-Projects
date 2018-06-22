import string, random
def generator():
    l1 = random.choice(string.ascii_lowercase)
    l2 = random.choice(string.ascii_lowercase)
    l3 = random.choice(string.ascii_lowercase)
    l4 = random.choice(string.ascii_lowercase)
    l5 = random.choice(string.ascii_lowercase)
    name = l1+l2+l3+l4+l5
    return(name)

print(generator())

#now asks user for some input
le1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letters ')
le2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letters ')
le3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letters ')
le4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letters ')
le5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letters ')

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase
le = [le1, le2, le3, le4, le5]
nme = str()
for i in range(0,5):
    if le[0] == "v":
        let = random.choice(vowels)
    elif le[0] == "c":
        let = random.choice(consonants)
    elif le[0] == "l":
        let = random.choice(letter)
    else:
        let = le[0]
    nme = nme+let

for babynames in range(20):
    print(generator())    
