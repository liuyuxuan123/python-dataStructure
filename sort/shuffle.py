import random

poke = []
i = 0
# Generate a new set of card

while i < 13:
    n = random.randint(0,13)
    if n not in poke:
        poke.append(n)
        i += 1
        
print(poke)

#Here is shuffle function
def shuffle(poke):
    lenth = len(poke)
    for i in range(lenth):
        newIndex = random.randint(i,lenth - 1)
        print(newIndex)
        poke[i],poke[newIndex] = poke[newIndex],poke[i]

shuffle(poke)
print(poke)
