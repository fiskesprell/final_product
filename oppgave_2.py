# Importerer forskjellige moduler
import blackjack_module as bjm

# Deler ut deilige chips (mmm salt og pepper fra Maarud)
chips = 5
betted_chips = 0

# Oppretter variabelen 'choice' som skal velge hit eller stand senere.
choice = "first loop"

while choice != "q":
    if choice == "first loop":
        # Alt under her lå over while-løkka, velger å plassere det innenfor
        # for å få en mulighet til å restarte spillet senere
        
        # Fjerner alt i stokket_kortstokk dersom du restarter spillet
        stokket_kortstokk = []

        # Opretter kortstokken som skal brukes i spillet
        stokket_kortstokk = bjm.get_new_shuffled_deck()

        # Oppretter Hånden til 'spillerene'
        # ELLER
        # Fjerner alle kortene i hendene dersom du restarter spillet
        player_hand = []
        dealer_hand = []

        # Deler ut 2 kort til Spilleren
        bjm.deal_cards(stokket_kortstokk, player_hand, 2)
        # Deler ut 2 kort til Dealeren
        bjm.deal_cards(stokket_kortstokk, dealer_hand, 2)

        print("The game is starting, but first you must bet.")
        print(f"You have {chips} chips.")
            
        # Asks player for a bet. Also checks if userinput is valid.
        while True:
            
            # Var ikke sikker på hvordan 'try' fungerte, så jeg fant info fra python documentation
            # https://docs.python.org/3/tutorial/errors.html#handling-exceptions
            try:
                betted_chips = int(input("How many chips do you want to bet?: "))
            except ValueError:
                print("Please, Numbers only.")
            
            # Jeg sverger at dette programmet kjørte uten
            # else:
            #   if betted_chips > 0 and betted_chips < chips or betted_chips == chips:
            # men når jeg sjekket igjen før jeg skulle levere inn så gjorde det ikke det
            # måtte i all hastverk prøve å finne ut hvordan jeg fikset det og takk Gud for
            # https://w3guides.com/tutorial/while-loop-with-if-else-statement-in-python#try-if-statement-in-while-loop
            else:
                if betted_chips > 0 and betted_chips < chips or betted_chips == chips: 
                    break
                elif betted_chips > chips:
                    print("You can't bet more chips than you have!")
                    
                elif betted_chips == 0:
                    print("Well, you're going to have to bet something...")
                    
                elif betted_chips < 0:
                    print("Did you just try to bet negative chips? Idiot. Try again.")
                
                
            
        betted_chips = int(betted_chips)
        chips -= betted_chips
        print(f"{betted_chips} chips are on the table. You have {chips} chips left.")

        print("\nThe cards are dealt. Hope you are ready...\n \n"
        # Jeg fant ut hvordan jeg printer lister uten brackets via. 
        # https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
        f"Your hand: {', '.join(player_hand)} - Value: {bjm.calculate_hand_value(player_hand)} points.\n"
        f"Dealer's hand: {dealer_hand[0]} - Value: {bjm.get_card_value(dealer_hand[0])} points.\n")

        input("Press Enter to continue...")
        print()
        choice = None


    # Sjekker om du får blackjack ved første hånd
    elif bjm.calculate_hand_value(player_hand) == 21:
        chips = bjm.print_result(player_hand, dealer_hand, chips, betted_chips)
        betted_chips = 0
        choice = bjm.restart_prompt(chips)



    elif choice == "1":
        bjm.deal_cards(stokket_kortstokk, player_hand, 1)
        print(f"\nYou were dealt {player_hand[-1]}.")
        print(f"Your current hand: {', '.join(player_hand)} - Value: {bjm.calculate_hand_value(player_hand)} points.")
        print(f"Dealer's hand: {dealer_hand[0]} - Value: {bjm.get_card_value(dealer_hand[0])}")
        input("Press Enter to continue...")
        choice = None

        if bjm.calculate_hand_value(player_hand) > 21:
            chips = bjm.print_result(player_hand, dealer_hand, chips, betted_chips)
            betted_chips = 0
            choice = bjm.restart_prompt(chips)


    elif choice == "2":
        while bjm.calculate_hand_value(dealer_hand) < 17:
            print("\nThe dealer hits...")
            bjm.deal_cards(stokket_kortstokk, dealer_hand, 1)

        chips = bjm.print_result(player_hand, dealer_hand, chips, betted_chips)
        betted_chips = 0
        choice = bjm.restart_prompt(chips)
    


    else:
        if chips == None:
            choice = "q"

        choice = input(
        "Hva vil du gjøre? \n"
        "1. HIT ME (konge)\n"
        "2. STAND\n"
        "q. QUIT GAME (pyse)\n"
        "Velg et alternativ ved å skrive '1', '2', eller 'q': ")