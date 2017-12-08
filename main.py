class Deck(object):
    def __init__(self,num):
        self.cards = num * [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'king','king','king','king','queen','queen','queen','queen','knight','knight','knight','knight']
    def throwCard(self):
        if len(self.cards) == 0:
            return
        import random
        return (self.cards).pop(random.randint(0,len(self.cards)-1))
    def getCards(self):
        return self.cards

class Hand(object):
    def __init__(self,type):
        self.cards = []
        self.sum = 0
        self.type = type
    def addCard(self,card):
        (self.cards).append(card)
    def getSum(self):
        self.sum = 0
        ###Throws The One's at the End of the hand list
        for i in xrange(0,len(self.cards)):
            if self.cards[i] == 1:
                (self.cards).pop(i)
                (self.cards).append(1)
        ###Sums The hand list
        for i in self.cards:
            if i == 1:
                if self.sum + 11 > 21:
                    self.sum += 1
                else :
                    if self.type == "player":
                        print "do you want to count the ace as 1 or 11 ?? Enter your choice as a number!"
                        while 1:
                            while 1 :
                                try :
                                    result = int(raw_input("Your choice -> "))
                                except :
                                    continue
                                else:
                                    break
                            if int(result) == 1:
                                self.sum += 1
                                break
                            elif int(result) == 11:
                                self.sum += 11
                                break
                            else :
                                continue
                    if self.type == 'pc':
                        rand = random.randint(1,10)
                        if rand % 2 == 0:
                            self.sum += 11
                        else:
                            self.sum += 1
            elif i == 'knight' or i == 'king' or i == 'queen':
                self.sum += 10
            else:
                self.sum += i
        return self.sum
    def showCards(self):
        return self.cards
    def __str__(self):
        print self.type
def getBet(cash):
    print "Enter the Amount of bet from your cash : ",cash
    while 1:
        while 1 :
            try :
                value = int(raw_input("Cash -> "))
            except:
                continuel
            else:
                break
        if value > cash:
            continue
        if value < 1:
            continue
        else :
            bet = value
            cash -= value
            break
    return bet
def getNumOfDecks():
    print "Enter the an integer num of decks  : 'Max is 100,Min is 1'"
    while 1:
        while 1 :
            try :
                num = int(raw_input("Num -> "))
            except:
                continue
            else:
                break
        if num > 100:
            continue
        if num < 1:
            continue
        else :
            return num
            break
def checkPlayer(player,pc):
    if player.getSum() > 21:
        print pc.type," Win"
        return False
    elif player.getSum() == 21:
        print player.type," BlackJack"
    else :
        return True
def checkDealer(player,pc):
    if pc.getSum() > 21:
        print player.type, " Win"
        return False
    elif pc.getSum() ==21:
        print pc.type, " Win"
        return False
    elif pc.getSum() == player.getSum() and player.getSum() < 21:
        print "PUSH"
        return False
    else :
        return True
def playAgain():
    print "Play Again ? yes or no!"
    choice = ((str(raw_input("Choice -> "))).upper())[0]
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False
from IPython.display import clear_output
while 1 :
    cash = 2500
    bet = getBet(cash)
    playerHand = Hand("person")
    autoHand = Hand("pc")
    num = getNumOfDecks()
    deck = Deck(num)
    clear_output()
    playerHand.addCard(deck.throwCard())
    if len((playerHand.showCards())) == 1:
        playerHand.addCard(deck.throwCard())
    print "Your Cards : ",playerHand.showCards()
    print "Player : ",playerHand.getSum()
    autoHand.addCard(deck.throwCard())
    temp = autoHand.getSum()
    print "Dealer : ",temp
    autoHand.addCard(deck.throwCard())
    game_on = checkPlayer(playerHand,autoHand)
    while game_on:
        game_on = checkPlayer(playerHand,autoHand)
        if game_on == False:
            break
        print "Hit or stand !?"
        choice = (str(raw_input("Choice -> ")).upper())[0]
        if choice == 'H':
            playerHand.addCard(deck.throwCard())
            print "Your Cards : ",playerHand.showCards()
            print "Player : ",playerHand.getSum()
            print "Dealer : ",temp
            continue
        elif choice == 'S':
            stand_on = True
            while stand_on:
                print "Dealer Cards : ",autoHand.showCards()
                print "Dealer : ",autoHand.getSum()
                autoHand.addCard(deck.throwCard())
                print "Your Cards : ",playerHand.showCards()
                print "Player : ",playerHand.getSum()
                print "Dealer Cards : ",autoHand.showCards()
                print "Dealer : ",autoHand.getSum()
                stand_on = checkDealer(playerHand,autoHand)
            break
        else:
            continue
        
    if playAgain() == False:
        break
    
