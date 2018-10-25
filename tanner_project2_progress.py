#Created by: Tanner Suard
#Purpose: Project 2 for OMIS30, create a blackjack simulator
#Date: October 24, 2018

import random
import itertools
from sys import platform as _platform
import os


# ****************************************************************************
# BEGIN FUNCTIONS FOR GENERAL USE (below)
# ****************************************************************************

#define a function for a deck of cards with 6 decks within it
def deck_of_cards():
    suits= ("Hearts","Diamonds","Clubs","Spades")
    cardvalues= ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    deck=[]
    for cardvalue in cardvalues:
        for suit in suits:
            deck.append(cardvalue + " of " + suit) 
    deck_1= []      
    for i in deck:  
        b=6*[i] #make loop for 6 decks to combine into one large deck
        #create correct number of cards with each card type in it's own list
        deck_1.extend([b]) 
    #flatten all lists of cards to make one big list with all cards
    deck_of_six=list(itertools.chain.from_iterable(deck_1)) 
    random.shuffle(deck_of_six) #shuffle deck
    return deck_of_six

#create a deck that can be popped and used repeatedly until runs out of cards.
deck_of_six=deck_of_cards()   
cardvalues= ("A","2","3","4","5","6","7","8","9","10","J","Q","K")


#Function for providing integer value for cards dealt
def value_of_card(card):
    #turn strings of values into integers for cards that equal 10 for the game.
    if card[0] in cardvalues[10:13+1]:
        return 10
    #turn strings into integers for numbers 2 thru 9 for the game.
    elif card[0] in cardvalues[1:8+1]:
        return int(card[0])
    #turn strings into ints for Aces. Allows player to use Ace as an 11 or 1.
    elif card[0] in cardvalues[0]:
        #create list with total value of cards. If over 10, ace has to be a 1
        if value_hand>10: 
            return 1
        else:
            ace_value= input("Would you like to treat the " + str(card) + \
            " as a 1 or 11? \n")
            while ace_value !="1" or ace_value !="11":    #input validation
                if ace_value== "1" or ace_value== "11":
                    return int(ace_value)
                elif ace_value== "one":
                    return 1
                elif ace_value== "eleven":
                    return 11
                else:
                    ace_value== input("Please enter a 1 or 11 as the value for\
                     your" + str(card)+ "? \n")
                 

#give a new card and remove card from original list                 
def new_card(deck_of_six):   
    return deck_of_six.pop(0)      


# allow us to change text style
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# ****************************************************************************
# BEGIN USER-FACING CODE (below)
# ****************************************************************************


# Detect OS to clear terminal window
if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    os.system('clear') # clear terminal
elif _platform == "win32" or _platform == "win64":
    os.system('cls') # clear cmd or ps
else:
    pass # or do nothing


# INTRO: Welcome to Blackjack!  
print(color.BOLD + color.BLUE + "Welcome to Blackjack!\n" + color.GREEN + "  \
  .... Created by Tanner, Chris, & Javi.\n" + color.END + color.BOLD + "\nNow,\
 let's get started.\n" + color.END)


# COLLECT # OF USERS & VALIDATE
while True: #validate input
    number_of_players = input("How many people are playing? ")
    if number_of_players.isdigit() and int(number_of_players) > 0:
        break
    else:
        continue

# CREATE LIST OF BETS & CURRENT PLAYER TRACKER-var
print(color.BOLD,"\nGot it,", number_of_players, "people will be playing.",\
color.END, "Now, we'll collect bets.\n")
ListOfBets = [] # Create list in which bets will appear
ListOfBets.insert(0,0) # Assign dealer in position 0, $0 to start off with
current_player = 1   # Establish starting position


# COLLECT BETS
# Start with dealer (0) and go until number of entered players
for i in range (0,int(number_of_players)): 
        bet = int(input("Player " + (str(current_player)) + ", what is your\
 bet? ")) # Take in bet input
        ListOfBets.insert(current_player,bet) # Add bet to list of bets
        current_player+=1 # move on to next player        


# START THE GAME
print(color.BOLD + "\nThanks for that information. Each player has been dealt\
 a hand. " + color.END + "We'll start with Player 1.\n")

#Deal cards if users want to play again
play_again = ""
while play_again!= "exit" or play_again!= "Exit":
    #Create a player's hand  (maybe loop to create mulitple players??)
    card_1= new_card(deck_of_six)
    card_2= new_card(deck_of_six)
    print("You have received a " + card_1 + " and a " + card_2 + ".")
    #turn String of card1 into int. Check for ace and 10
    value_1= value_of_card(card_1) 
    value_2= value_of_card(card_2)
    value_hand= value_1 + value_2
    print("Your total hand value is " + str(value_hand) + ".")


    #Create Dealer's hand
    dealer_card_1= new_card(deck_of_six)
    dealer_card_2= new_card(deck_of_six)
    dealer_value_1= value_of_card(dealer_card_1)
    dealer_value_2= value_of_card(dealer_card_2)
    dealer_value_hand= dealer_value_1 + dealer_value_2
    print("The Dealer deals himself two cards. One face up and one face down.")
    print("The face up card is a " + dealer_card_1 + ".")


    #Blackjack results if player has blackjack
    if value_hand == 21:
        print("Congratulations! You got a Blackjack!")
        print("The Dealer now reveals his second card which is a "\
         + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
        if dealer_value_hand== 21 and value_hand== 21:
            print("You and the Dealer both have Blackjack so you push and tie!")
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")
        else:
            print("You win!")
            play_again = input("Would you like to play another hand? Or you can\
             type exit to leave\n")

    else:
        if value_hand < 21:
            user_input= input("Would you like to hit or stand? \n")
            if user_input== "hit" or user_input=="Hit":
                card_3= new_card(deck_of_six)
                value_3= value_of_card(card_3)
                value_hand += value_3
                print("You are dealt a " + card_3 + " for a total of "\
                 + str(value_hand) + ".")

                if value_hand > 21:
                    print("You busted; therefore, you lose this hand.")
                    play_again = input("Would you like to play another hand?\
                     Or you can type exit to leave\n")
                else:
                    continue
            
            elif user_input== "stand" or user_input== "Stand":
                continue
            print("The Dealer reveals his face down card to be a "\
             + dealer_card_2 + " for a total of " + str(dealer_value_hand) + ".")
            if dealer_value_hand < 17:
                print("The Dealer must hit.")
                dealer_card_3= new_card(deck_of_six)
                dealer_value_3= value_of_card(dealer_card_3)
                print("The Dealer drew a " + dealer_card_3 + " for a total of "\
                 + str(dealer_value_hand)+ ".")
                if dealer_value_hand > 21 and value_hand <= 21:
                    print("The Dealer busted... You win!")
                    play_again = input("Would you like to play another hand?\
                     Or you can type exit to leave\n")
                elif dealer_value_hand < 21 and dealer_value_hand > value_hand:
                    print("The Dealer has a higher hand than you. You lose!")
                    play_again = input("Would you like to play another hand?\
                    Or you can type exit to leave\n")
                else:
                    continue
            elif dealer_value_hand == value_hand:
                print("There is a push. Player and Dealer tie.")
                play_again = input("Would you like to play another hand?\
                 Or you can type exit to leave\n")
            elif dealer_value_hand < value_hand:
                print("You have a higher hand than the Dealer. You win!")
                play_again = input("Would you like to play another hand?\
                 Or you can type exit to leave\n")
            else:
                print("The Dealer has a higher hand than you. You lose!")
                play_again = input("Would you like to play another hand?\
                 Or you can type exit to leave\n")
            break
