
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_total(cards_):
  total = 0
  for card_ in cards_:
      total+=card_

    #return sum(cards_)
  return total

def draw_card(cards_):
  random_card = random.choice(cards)
  if(random_card == 11 and card_total(cards_)+random_card > 22):
    random_card = 1
    cards_.append(random_card)
  else:
    cards_.append(random_card)

  return cards


def determine_winner(_computer_cards,_user_cards):

  print(f"Your final hand: {_user_cards}, final score: {card_total(_user_cards)}")
  print(f"Your Computer's final hand: {_computer_cards}, final score: {card_total(_computer_cards)}")

  if card_total(_computer_cards) > 21:
    print("You Win")
  elif card_total(_user_cards) > 21:
    print("Computer Win")
  elif card_total(_computer_cards) > card_total(_user_cards):
    print("Computer Wins")
  elif card_total(_computer_cards) == card_total(_user_cards):
    print("Draw")
  else:
    print("You Win")

def player_turn():

  if card_total(user_cards) < 21 :
    draw_card(user_cards)



def computer_turn():
  while card_total(computer_cards)  < 17 and card_total(computer_cards) !=21 :
    draw_card(computer_cards)


  


import art
import random
play =input("Do you want to play a game of Blackjack? Type 'y' or 'no' : ").lower()

if(play == "y"):


  print(art.logo)

  user_cards = [random.choice(cards),random.choice(cards)]
  current_score = user_cards[0]+user_cards[1]

  print(f"Your cards: [{user_cards[0]}][{user_cards[1]}], current score: {card_total(user_cards)} ")

  computer_cards =[random.choice(cards)]
  print(f"Computer's first card: [{computer_cards[0]}]")


if(current_score == 21):
  computer_turn()
  determine_winner(computer_cards,user_cards)
else:
  another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  while another_card =="y" and card_total(user_cards)  < 22:
    
    player_turn()
    print(f"Your cards: [{user_cards}], current score: {card_total(user_cards)} ")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

  
 
  computer_turn()
  determine_winner(computer_cards,user_cards)
