############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##########################################


from art import logo
import random

game_in_progress = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
  return cards[random.randint(0, len(cards)-1)]

def deal_starting_hand():
  for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def score_total(hand):
  return sum(hand)

#function to check if hand is greater than 21
def is_over_21(hand):
  if score_total(user_cards) == 21:
    print("Blackjack. You win!")
    return
  elif score_total(computer_cards) == 21:
    print("Dealer Blackjack. Computer Wins!")
    return
  elif score_total(hand) > 21:
    if 11 in hand:
      ace_index = hand.index(11)
      hand[ace_index] = 1
      if score_total(hand) > 21:
        print("You busted.")
        return True
    else:
      print("You busted.")
      return True
      

def more_cards_or_not():
  push_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  if push_decision == 'y':
    user_cards.append(deal_card())
  elif push_decision == 'n':
    return

def start_game():
  game_status = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if game_status == 'y':
    print(logo)
    deal_starting_hand()
    
    print(f"Your Cards: {user_cards}, Current Score: {score_total(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    if score_total(user_cards) == 21:
      print("Blackjack. You win!")
    elif score_total(computer_cards) == 21:
      print("Dealer Blackjack. Computer Wins!")
    
    user_busted = False
    computer_busted = False
    
    while user_busted == False:
      more_cards_or_not() #user input
      print(score_total(user_cards)) 
      
      if is_over_21(user_cards) == True:
        user_busted = True
  else: 
    return

start_game()

