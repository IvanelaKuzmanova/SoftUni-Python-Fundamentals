def damage_calculator(price_ratings:list, entry_point:int, item_type:str) -> str:
    left_items_list = price_ratings[:entry_point]
    right_items_list = price_ratings[entry_point + 1:]

    entry_item_price = price_ratings[entry_point]

    if item_type == "cheap":

        left_for_sum = [x for x in left_items_list if x < entry_item_price]
        right_for_sum = [x for x in right_items_list if x < entry_item_price]

    elif item_type == "expensive":
        left_for_sum = [x for x in left_items_list if x >= entry_item_price]
        right_for_sum = [x for x in right_items_list if x >= entry_item_price]

    sum_left = sum(left_for_sum)
    sum_right = sum(right_for_sum)

    if sum_left > sum_right or sum_left == sum_right:
        print(f"Left - {sum_left}")
    elif sum_right > sum_left:
        print(f"Right - {sum_right}")


item_prices = [int(x) for x in input().split(", ")]
starting_point = int(input())
type = input()

result = damage_calculator(item_prices, starting_point, type)




