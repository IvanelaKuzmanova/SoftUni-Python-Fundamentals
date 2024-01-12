cards_list = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):    #cycle defining number of shuffles

    middle_of_cards = len(cards_list) // 2
    left_deck = cards_list[0:middle_of_cards]       #slicing first half (exclusive the second value of the range)
    right_deck = cards_list[middle_of_cards:]       #slicing second half (end by default)

    new_shuffled_deck = []

    for card_index in range(len(left_deck)):        #could be to the length of deck 2, since 1 and 2 are with the same length

        new_shuffled_deck.append(left_deck[card_index])         #from each deck one after the other we take the card from the corresponding index and add it to the new deck
        new_shuffled_deck.append(right_deck[card_index])

    cards_list = new_shuffled_deck          #to shuffle the new deck after the first iteration (not the initial one)

print(new_shuffled_deck)