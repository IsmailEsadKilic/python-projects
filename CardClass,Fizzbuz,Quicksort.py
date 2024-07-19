class card:
    suit_names = ['Clubs', 'Diamonds',
                  'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (card.rank_names[self.rank],
                             card.suit_names[self.suit])


#print(card(1,11))

def laFizziusBuzzius():
    out = []
    for i in range(1, 200):
        t = str(i)
        if i % 3 == 0:
            t += "Fizz"
        if i % 5 == 0:
            t += "Buzz"
        if i % 7 == 0:
            t += "Bazz"
        out.append(t)
    for i in out:
        print(i)
    
#laFizziusBuzzius()

import random as rand
def smtn():
    larandomrumbers = [i for i in range(1, 101)]
    rand.shuffle(larandomrumbers)
    print(larandomrumbers)

    neu = quicksort(larandomrumbers)

    print(neu)

import math as m

def quicksort(l):
    if len(l) <= 1:
        return l
    pivot = l[m.floor(len(l)/2)]
    left = []
    right = []
    for i in l:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
    return quicksort(left) + [pivot] + quicksort(right)


