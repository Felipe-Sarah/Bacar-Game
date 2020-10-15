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

# Setting Decks
n = int(input('Number of decks (1/6/8) '))
while n != 1 and n != 6 and n != 8:
    print('Invalid number of decks')
    n = int(input('Number of decks (1/6/8) '))
deck = deck * n


# Seting Values

points = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '1':0, 'J':0, 'Q':0, 'K':0}

# Game Starts

i = 0
while i < len(players):
    print(players[i] + ' recieves 100 chips')
    i+=1

chips = [100]*len(players)


while True:

    random.shuffle(deck)

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

    table_cards = [deck[0], deck[1]]
    house_cards = [deck[2], deck[3]]

    print('Table has {}'.format(table_cards))
    print('House has {}'.format(house_cards))



    a = deck[0]
    b = deck[1]
    c = deck[2]
    d = deck[3]
    e = deck[4]
    f = deck[5]



    table_points = points[a[0]] + points[b[0]]
    if table_points >= 10:
        table_points = table_points - (table_points - (table_points % 10))
    print('Table has {} points'.format(table_points))

    house_points = points[c[0]] + points[d[0]]
    if house_points >= 10:
        house_points = house_points - (house_points - (house_points % 10))
    print('House has {} points'.format(house_points))


    while True:

        if table_points > 7 or house_points > 7:
            if house_points == table_points:
                print('Tie')
                resultado = 'Tie'
                break
            elif table_points > house_points:
                print('Table wins')
                resultado = 'Table'
                break
            else:
                print('House wins')
                resultado = 'House'
                break

        if table_points < 6:
            table_cards.append(e)
            print('Table has {}'.format(table_cards))
            table_points = table_points + points[e[0]]
            if table_points >= 10:
                table_points = table_points - (table_points - (table_points % 10))
            print('Table has {} points'.format(table_points))

        

        if house_points < 6 and len(table_cards) == 2:
            house_cards.append(e)
            print('House has {}'.format(house_cards))
            house_points = house_points + points[e[0]]
            if house_points >= 10:
                house_points = house_points - (house_points - (house_points % 10))
            print('House has {} points'.format(house_points))

        while house_points < 6 and len(table_cards) == 3:

            if house_points == 5 and points[e[0]] < 4 and points[e[0]] > 7:
                break
            elif house_points == 4 and points[e[0]] < 2 and points[e[0]] > 7:
                break    
            elif house_points == 4 and points[e[0]] == 8:
                break
            else:
                house_cards.append(f)
                print('House has {}'.format(house_cards))
                house_points = house_points + points[f[0]]
                if house_points >= 10:
                    house_points = house_points - (house_points - (house_points % 10))
                print('House has {} points'.format(house_points))
                break

        if house_points == table_points:
            print('Tie')
            resultado = 'Tie'
            break
        elif table_points > house_points:
            print('Table wins')
            resultado = 'Table'
            break
        else:
            print('House wins')
            resultado = 'House'
            break

    # Pagamento de apostas
    i = 0
    while i < len(players):
        if n == 1:
            if resultado == 'Tie':
                if bets_winners[i] == resultado:
                    print('{} wins {} chips'.format(players[i], 8*bets_chips[i]*0.8425))
                    chips[i] = chips[i] + 
                


    









