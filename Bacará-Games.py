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
    print(players[i] + ' recieves 10000 chips')
    i+=1

chips = [10000]*len(players)


while True:

    k = 0
    while k < len(players):
        print('{} has {} chips'.format(players[k], chips[k]))
        if chips[k] == 0:
            print('{} has been removed due to insuficient funds'.format(players[k]))
            del players[k]
            del chips[k]
            continue
        m = input('{}, would you like to continue? (y/n) '.format(players[k]))
        while m != 'y' and m != 'n':
            print('Invalid answer')
            m = input('{}, would you like to continue? (y/n) '.format(players[k]))
        if m == 'n':
            print('{} is out'.format(players[k]))
            del players[k]
            del chips[k]
            continue    
        k += 1

    if len(players) == 0:
        break



    random.shuffle(deck)

    # Placing bets

    bets_chips = []
    bets_winners = []
    i = 0
    while i < len(players):
        bets_chips.append(int(input('{} place your bet value (number of chips) '.format(players[i]))))
        while bets_chips[i] > chips[i] or bets_chips[i] < 0:
            print('Not enough chips or negative number!')
            bets_chips[i] =int(input('{} place your bet value '.format(players[i])))

        bets_winners.append(input('on whom? (Players, Bank or Tie) '))
        while bets_winners[i] != 'Players' and bets_winners[i] != 'Bank' and bets_winners[i] != 'Tie':
            print ('Invalid bet, please try again')
            bets_winners[i] = input('on whom? (Players, Bank or Tie) ')
        i += 1


    players_cards = [deck[0], deck[1]]
    bank_cards = [deck[2], deck[3]]

    print('Players have {}'.format(players_cards))
    print('Bank has {}'.format(bank_cards))



    a = deck[0]
    b = deck[1]
    c = deck[2]
    d = deck[3]
    e = deck[4]
    f = deck[5]



    players_points = points[a[0]] + points[b[0]]
    if players_points >= 10:
        players_points = players_points - (players_points - (players_points % 10))
    print('Players have {} points'.format(players_points))

    bank_points = points[c[0]] + points[d[0]]
    if bank_points >= 10:
        bank_points = bank_points - (bank_points - (bank_points % 10))
    print('Bank has {} points'.format(bank_points))


    while True:

        if players_points > 7 or bank_points > 7:
            if bank_points == players_points:
                print('Tie')
                resultado = 'Tie'
                break
            elif players_points > bank_points:
                print('Players win')
                resultado = 'Players'
                break
            else:
                print('Bank wins')
                resultado = 'Bank'
                break

        if players_points < 6:
            players_cards.append(e)
            print('Players have {}'.format(players_cards))
            players_points = players_points + points[e[0]]
            if players_points >= 10:
                players_points = players_points - (players_points - (players_points % 10))
            print('Players have {} points'.format(players_points))

        

        if bank_points < 6 and len(players_cards) == 2:
            bank_cards.append(e)
            print('Bank has {}'.format(bank_cards))
            bank_points = bank_points + points[e[0]]
            if bank_points >= 10:
                bank_points = bank_points - (bank_points - (bank_points % 10))
            print('Bank has {} points'.format(bank_points))

        while bank_points < 6 and len(players_cards) == 3:

            if bank_points == 5 and points[e[0]] < 4 and points[e[0]] > 7:
                break
            elif bank_points == 4 and points[e[0]] < 2 and points[e[0]] > 7:
                break    
            elif bank_points == 4 and points[e[0]] == 8:
                break
            else:
                bank_cards.append(f)
                print('Bank has {}'.format(bank_cards))
                bank_points = bank_points + points[f[0]]
                if bank_points >= 10:
                    bank_points = bank_points - (bank_points - (bank_points % 10))
                print('Bank has {} points'.format(bank_points))
                break

        if bank_points == players_points:
            print('Tie')
            resultado = 'Tie'
            break
        elif players_points > bank_points:
            print('Players win')
            resultado = 'Players'
            break
        else:
            print('Bank wins')
            resultado = 'Bank'
            break

    # Pagamento de apostas
    i = 0
    while i < len(players):
        if n == 1:
            if resultado == 'Tie':
                if bets_winners[i] == resultado:
                    p = 8*bets_chips[i]
                    q = int(p*0.8425)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]

            if resultado == 'Players':
                if bets_winners[i] == resultado:
                    p = bets_chips[i]
                    q = int(p*0.9871)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]

            if resultado == 'Bank':
                if bets_winners[i] == resultado:
                    p = int(bets_chips[i]*0.95)
                    q = int(p*0.9899)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]    
            
        if n == 6:
            if resultado == 'Tie':
                if bets_winners[i] == resultado:
                    p = 8*bets_chips[i]
                    q = int(p*0.8556)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]

            if resultado == 'Players':
                if bets_winners[i] == resultado:
                    p = bets_chips[i]
                    q = int(p*0.9876)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]

            if resultado == 'Bank':
                if bets_winners[i] == resultado:
                    p = int(bets_chips[i]*0.95)
                    q = int(p*0.9894)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]           

        if n == 8:
            if resultado == 'Tie':
                if bets_winners[i] == resultado:
                    p = 8*bets_chips[i]
                    q = int(p*0.8564)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]

            if resultado == 'Players':
                if bets_winners[i] == resultado:
                    p = bets_chips[i]
                    q = int(p*0.9876)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]

            if resultado == 'Bank':
                if bets_winners[i] == resultado:
                    p = int(bets_chips[i]*0.95)
                    q = int(p*0.9894)
                    print('{} wins {} chips'.format(players[i], p))
                    print('Commission of {} chips'.format(p - q))
                    print('{} gets {} chips'.format(players[i], q))
                    chips[i] = chips[i] + q
                else:
                    print('{} loses {} chips'.format(players[i], bets_chips[i]))
                    chips[i] = chips[i] - bets_chips[i]
        i += 1

print('Game over, thanks for playing! =D')









