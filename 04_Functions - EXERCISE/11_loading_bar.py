def loading_bar(num:int) -> str:

    symbols_list = []
    number_of_dots = 10 - num//10

    for symbol in range(int(num//10)):
        symbols_list.append("%")
    for symbol in range(int(number_of_dots)):
        symbols_list.append(".")

    list_as_string = "".join(symbols_list)

    if symbols_list[9] != "%":
        return f"{num}% [{list_as_string}]\nStill loading..."
    else:
        return f"100% Complete!\n[{list_as_string}]"

number = int(input())
result = loading_bar(number)

print(result)

