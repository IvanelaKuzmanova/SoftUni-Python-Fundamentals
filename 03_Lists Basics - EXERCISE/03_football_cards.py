# team_a_players = 11
# team_b_players = 11
#
# card_sequence = input()
# list_cards = card_sequence.split(" ")
#
# cards_a = []
# cards_b = []
#
# game_stopped = False
#
# for card in list_cards:
#     if "A" in card:
#         cards_a.append(card)
#     elif "B" in card:
#         cards_b.append(card)
#
# unique_cards_a_count = len(set(cards_a))        #we transform lists to sets to eliminate duplicated numbers, since it is explained we need to ignore them
# unique_cards_b_count = len(set(cards_b))
#
# if unique_cards_a_count > 5:
#     unique_cards_a_count = 5
# if unique_cards_b_count > 5:
#     unique_cards_b_count = 5
#
# if unique_cards_a_count == 5 or unique_cards_b_count == 5:
#     game_stopped = True
#
# print(f"Team A - {team_a_players - unique_cards_a_count}; Team B - {team_b_players - unique_cards_b_count}")
#
# if game_stopped:
#     print("Game was terminated")

team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]        # създаваме директно списък на отборите с точни имена както в картите
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

cards_list = input().split()

game_stopped = False

for player in cards_list:           #търсим директно в листа съответствие за целия стринг от карта и го вадим с remove
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)       # с тази проверка обхващаме и случая играчът да не е в отбора, като просто го игнорираме и цикълът продължава

    if len(team_a) < 7 or len(team_b) < 7:          # aко в листа има по-малко от 7 елемента, т.е. по-малко от 7 играчи, прекъсваме цикъла
        game_stopped = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")        #директно принтираме дължината на листа, тъй като това са останалите играчи

if game_stopped:
    print("Game was terminated")