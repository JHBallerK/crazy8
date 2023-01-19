def user_inp():
    play=input("please input: ").lower()
    return play

def skip(play,players,i):
    if play[0] =="7":
        print("player",players[i]," played a ",play," ,so player",players[i]," turn is skipped")
        return True


def change_suit(play):
    if play[0] == "8":
        print("change suit")
        suit=pick_suit().lower()
        if suit[0] == "s" or suit[0] == "h" or suit[0] == "d" or suit[0]=="c":
            print(suit)
            print("the suit has been changed to ",suit.capitalize())
        #return True


def turn_play(play,players):
    if play[0] =="j":
        print("player[] played a [play] the order of the ply has been reversed it's player[]turn to play")
        players.reverse()
        print(players)
        

def pick_suit():
        pick_a_suit=input("please pick a suit- Spades, Hearts, Diamonds , Clubs : ")
        return pick_a_suit

def reverse_play(players,i):
    x=players[:i]
    y=players[i:]
    x.reverse()
    y.reverse()
    z=x+y
    return z


players=[["T"],["Q"],["W"],["K"],["L"]]#reverse the list from a certain index
print(players)
for i in range(len(players)):
    t=reverse_play(players,i)
    print(t)
play=user_inp()
skip_player=skip(play)
change_suit(play)
turn_play(play,players) 
reverse_play(players,i)