import random
# Trenger sys for å bruke sys.exit()
import sys

full_deck = {"Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
             "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
             "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
             "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
             "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
             "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
             "Ace of diamonds": 11,
             "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
             "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
             "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
             "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
             "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
             "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
             }


def get_new_shuffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


def get_card_value(card):
    return full_deck[card]


def calculate_hand_value(hand):
    hand_value = 0

    for card in hand:
        hand_value += get_card_value(card)
    
    if hand_value > 21:
        if "Ace of spades" in hand:
            hand_value -= 10
        elif "Ace of diamonds" in hand:
            hand_value -= 10
        elif "Ace of hearts" in hand:
            hand_value -= 10
        elif "Ace of clubs" in hand:
            hand_value -= 10
    #TODO: kanskje få dette til å fungere med mer enn 1 kort

    return hand_value


# Lager en funksjon som lar deg dele ut X antall kort
def deal_cards(input_list, output_list, num_of_cards):
    for x in range(0, num_of_cards):
        output_list.append(input_list.pop())

# Lager funksjon print_result()
def print_result(player_list, dealer_list, money_pile, temp_money):
    player_points = calculate_hand_value(player_list)
    dealer_points = calculate_hand_value(dealer_list)
    if dealer_points > 21:
        # Dealer busts
        print(f"\nYour hand: {', '.join(player_list)} - Value: {player_points} points.")
        print(f"Dealer's hand: {', '.join(dealer_list)} - Value: {dealer_points} points.\n")
        print(f"Dealer has {dealer_points} points. You have {player_points} points. Dealer Busts! You win!\n")
        print(f"You WON your bet of {temp_money} and gained {temp_money * 2} chips!")
        money_pile += (temp_money * 2)
        print(f"You now have {money_pile} chips.")
        return money_pile


    elif player_points > 21:
        # Player busts
        print(f"\nYour hand: {', '.join(player_list)} - Value: {player_points} points.")
        print(f"Dealer's hand: {', '.join(dealer_list)} - Value: {dealer_points} points.\n")
        print(f"Dealer has {dealer_points} points. You have {player_points} points. You are bust! House wins!\n")
        print(f"You LOST your bet of {temp_money} chips. ")
        print(f"You now have {money_pile} chips.")
        return money_pile
        
    elif calculate_hand_value(player_list) == 21:
        # BLACKJACK
        print(f"\nYour hand: {', '.join(player_list)} - Value: {player_points} points.")
        print(f"Dealer's hand: {', '.join(dealer_list)} - Value: {dealer_points} points.\n")
        print(f"Dealer has {dealer_points} points. You have {player_points} points. Player blackjack!\n")
        print(f"You WON your bet of {temp_money} and gained {temp_money * 4} chips!")
        money_pile += (temp_money * 4)
        print(f"You now have {money_pile} chips.")
        return money_pile


    elif dealer_points > player_points:
        # Dealer has more points
        print(f"\nYour hand: {', '.join(player_list)} - Value: {player_points} points.")
        print(f"Dealer's hand: {', '.join(dealer_list)} - Value: {dealer_points} points.\n")
        print(f"Dealer has {dealer_points} points. You have {player_points} points. House wins!\n")
        print("------")
        print(f"You LOST your bet of {temp_money} chips. ")
        print(f"You now have {money_pile} chips.")
        return money_pile


    elif player_points > dealer_points:
        # Player has more points
        print(f"\nYour hand: {', '.join(player_list)} - Value: {player_points} points.")
        print(f"Dealer's hand: {', '.join(dealer_list)} - Value: {dealer_points} points.\n")
        print(f"Dealer has {dealer_points} points. You have {player_points} points. You win!\n")
        print(f"You WON your bet of {temp_money} and gained {temp_money * 2} chips!")
        money_pile += (temp_money * 2)
        print(f"You now have {money_pile} chips.")
        return money_pile


    elif player_points == dealer_points:
        # Dealer & Player are tied
        print(f"\nYour hand: {', '.join(player_list)} - Value: {player_points} points.")
        print(f"Dealer's hand: {', '.join(dealer_list)} - Value: {dealer_points} points.\n")
        print(f"Dealer has {dealer_points} points. You have {player_points} points. It's a tie!\n")
        print(f"The {temp_money} chips were returned to your hand.")
        money_pile += temp_money
        print(f"You now have {money_pile} chips.")
        return money_pile


def restart_prompt(money_pile):
    
    yes_or_no = ""
    
    # Checks if you already lost 'the game'
    # Om du taper så skal det komme en utskrift og programmet termineres
    # Lærte om sys.exit fra stackoverflow på denne lenken
    # https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running
    if money_pile == 0:
        print("Since you have no chips left, you have lost.")
        print("Thanks for playing, we hope to see you again.")
        sys.exit()
    
    while True:
        if yes_or_no == "y":
            return "first loop"
            False
        elif yes_or_no == "n":
            print("Thank you for playing. Until next time.")
            return "q"
            False
        else:
            print("Do you want to play another round?")
            yes_or_no = input("Type 'y' for yes | type 'n' for no: ")
            print()