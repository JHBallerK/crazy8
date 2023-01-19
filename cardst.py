import random


def create_deck():
    ff=[str(k) for k in range(2,11)]
    royal=["A","J","Q","K"]
    ff.extend(royal)
    suits=["S","H","D","C"]
    deck=[]
    for k in range(4):
        for l in range(13):
            card = (ff[l] + suits[k])
            deck.append(card)
    return deck

def shuffle_deck(deck):
    random,random.shuffle(deck)
    return deck


def pick_number_of_hands():
    pick_hands=int(input("number of hands: "))
    
    return pick_hands


def deal_hands(hand,shuffled_deck):
    
    players=[]
    
    for player in range(hand):
        players.append([])
        for x in range(8):
            d1=shuffled_deck.pop()
            players[player].append(d1)

    return players

def play_turns(number_of_players,players,up_card,left_deck):
    for i in range(number_of_players):      
        #if skip_player == True:
            #continue
        print(up_card)
        print("it's player",i,"turn",players[i])
        can_play = check_against_card(up_card[-1],players[i])
        if can_play:
            player=validate_action_input()
        else:
            player = "draw"
        
        if player == "draw":
            d2=left_deck.pop()
            players[i].append(d2)
            print(players[i])
        elif player =="play":
           play=validate_card_input(players[i],up_card[-1])
           players[i].remove(play)
           up_card.append(play)
           print(players[i])
           print(up_card)
           

def validate_card_input(player_hand,up_card):
    while True:
        play=input("select card: ").upper()
        if play not in player_hand:
            print("that's not a card in your hand ")
        elif play[0] ==up_card[0] or play[-1] == up_card[-1]:
            return play
            
        else:
            print("not a valid play")   


def check_against_card(up_card,player_hand):
    for card in player_hand:
        if  card[0] ==up_card[0] or card[-1] == up_card[-1]:
            return True
    else:
        print("you don't have a valid card in your hand to play, Please draw a card")
        return False

def validate_action_input():
    while True:
        player=input("play or draw: ").lower()
        if player == "play" or player == "draw":
            return player
        else:
            print('not valid input') 

def check_for_winner(winners,player):
    i=0
    while i in range(len(player)):
        if len(player[i])==0:
            player.pop(i)
            winners.append(i)
        i+=1
    return winners,player

def play_crazy8():
    winners=[]
    deck=create_deck()
    shuffled_deck=shuffle_deck(deck)
    print(shuffled_deck)
    hand=pick_number_of_hands()
    players=deal_hands(hand,shuffled_deck)
    print(players)    
    for j in players:
        print(j)
    up_card=[shuffled_deck.pop()]
    left_deck=shuffled_deck
    print("the up card ",up_card)
    print(left_deck)
    while len(players) > 1:
        play_turns(hand,players,up_card,left_deck)
        winners,players=check_for_winner(winners,players)
    print("the winners are :",winners[0])

    
    
play_crazy8()