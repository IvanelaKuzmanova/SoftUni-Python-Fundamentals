team_a_players = 11
team_b_players = 11

card_sequence = input()
list_cards = card_sequence.split(" ")

cards_a = []
cards_b = []

game_stopped = False

for card in list_cards:
    if "A" in card:
        cards_a.append(card)
    elif "B" in card:
        cards_b.append(card)

unique_cards_a_count = len(set(cards_a))        #we transform lists to sets to eliminate duplicated numbers, since it is explained we need to ignore them
unique_cards_b_count = len(set(cards_b))

if unique_cards_a_count > 5:
    unique_cards_a_count = 5
if unique_cards_b_count > 5:
    unique_cards_b_count = 5

if unique_cards_a_count == 5 or unique_cards_b_count == 5:
    game_stopped = True

print(f"Team A - {team_a_players - unique_cards_a_count}; Team B - {team_b_players - unique_cards_b_count}")

if game_stopped:
    print("Game was terminated")
