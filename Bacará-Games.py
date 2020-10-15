# Bacará Game
# Creating the deck
import random

print('Welcome to Bacará Game')

cardfaces = []
suits = ['Hearts', 'Diomonds', 'Spades' , 'Clubs']
royals = ['J', 'Q', 'K', 'A']
deck = []

i = 2
while i < 11:
    cardfaces.append(str(i))
    i+=1

j = 0
while j < 4:
    cardfaces.append(str(royals[j]))
    j+=1

k = 0
l = 0
m = 0
while m < 52:
    card = cardfaces[k] + " of " + suits[l]
    if k != 12:
        k += 1
    else:
        k = 0
        l += 1
    m += 1
    deck.append(card)


# Seting Players
players = []
j = 1
i = int(input('Number of Players '))
while j <= i:
    players.append(input('Name of player ' + str(j) + ' '))
    j += 1

print(players)

# Seting Decks
i = int(input('Number of decks '))
deck = deck * i


# Seting Values



# Game Starts
random.shuffle(deck)
i = 0
while i < len(players):
    print(players[i] + ' recieves 100 chips')
    i+=1

chips = [100]*len(players)

# Placing bets

bets_chips = []
bets_winners = []
i = 0
j = 1
while i < len(players):
    bets_chips.append(int(input('{} place your bet value '.format(players[i]))))
    bets_winners.append(input('on whom? (Table, House or Tie) '))
    i += 1
    j += 1

#Card Value
points = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':0, 'J':0, 'Q':0, 'K':0}

a = deck[0]
b = deck[1]
c = deck[2]
d = deck[3]


table_points = points[a[0]] + points[b[0]]
print(table_points)
if table_points >= 10:
    table_points = table_points - (table_points - (table_points % 10))
print('Table has {} points'.format(table_points))

house_points = points[c[0]] + points[d[0]]
print(house_points)
if house_points >= 10:
    house_points = house_points - (house_points - (house_points % 10))
print('House has {} points'.format(house_points))
