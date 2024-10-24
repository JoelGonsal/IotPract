#importing modules 
import itertools , random 
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club'])) 
random.shuffle(deck) 
print("Joel Gonsalves 111") 
print("You Got: ") 
for i in range(5):
    print(deck[i][0],"of",deck[i][1])


#practice improved 
# Define card ranks including face cards
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
suits = ['Spade', 'Heart', 'Diamond', 'Club']

# Create a deck of cards
deck = list(itertools.product(ranks, suits))

# Shuffle the deck
random.shuffle(deck)

print("Joel Gonsalves 111")
print("You Got:")

# Draw and print 5 cards
for i in range(5):
    print(deck[i][0], "of", deck[i][1])

#practice

deck = list(itertools.product(range(1,14),['a','b','c','d']))

for i in range(5):
    print(deck[i][0]," of " ,deck[i][1])
