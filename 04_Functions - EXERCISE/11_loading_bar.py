def loading_bar(num = int):

    symbols_list = []
    digit_to_start = 10 - num/10

    for symbol in range(int(num/10)):
        symbols_list.append("%")
    for symbol in range(int(digit_to_start)):
        symbols_list.append(".")

    list_as_string = "".join(symbols_list)

    if symbols_list[9] != "%":
        print(f"{num}% [{list_as_string}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{list_as_string}]")

number = int(input())

result = loading_bar(number)

