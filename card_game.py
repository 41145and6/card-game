def card_picking_game(bet):
  money = 1000
  discard_pile = []
  deck_of_cards = []
  for i in range(0, 4):
    for n in range (2, 15):
      deck_of_cards.append(n)
  while len(discard_pile) < 52 and money > 0:
    #player card pick
    plyr1 = random.randrange(0 , len(deck_of_cards))
    plyr1_card = deck_of_cards.pop(plyr1)
    discard_pile.append(plyr1_card)
    #house card pick
    house = random.randrange(0 , len(deck_of_cards))
    house_card = deck_of_cards.pop(house)
    discard_pile.append(house_card)
    #compare cards
    if plyr1_card > house_card:
      money += bet
      if plyr1_card == 14:
        print('Player beats House with an Ace')
        print('You have $' + str(money))
      elif plyr1_card == 13:
        print('Player beats House with a King')
        print('You have $' + str(money))
      elif plyr1_card == 12:
        print('Player beats House with a Queen')
        print('You have $' + str(money))
      elif plyr1_card == 11:
        print('Player beats House with a Jack')
        print('You have $' + str(money))
      else:
        print('Player beats House with a ' + str(plyr1_card))
        print('You have $' + str(money))
    elif house_card > plyr1_card:
      money -= bet
      if house_card == 14:
        print('House beats Player with an Ace')
        print('You have $' + str(money))
      elif house_card == 13:
        print('House beats Player with a King')
        print('You have $' + str(money))
      elif house_card == 12:
        print('House beats Player with a Queen')
        print('You have $' + str(money))
      elif house_card == 11:
        print('House beats Player with a Jack')
        print('You have $' + str(money))
      else:
        print('Player beats House with a ' + str(house_card))
        print('You have $' + str(money))
    elif plyr1_card == house_card:
      print('Tied! All bets returned')
  if money > 0:
    print('After ' + str(len(discard_pile) / 2) + 'rounds, you have won $' + str(money))
  elif money <= 0:
    print('After ' + str(len(discard_pile) / 2) + ' rounds, you have lost all your money to the house!')