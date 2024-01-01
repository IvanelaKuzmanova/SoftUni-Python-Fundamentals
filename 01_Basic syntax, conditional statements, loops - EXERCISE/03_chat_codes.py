messages_sent = int(input())

for i in range(messages_sent):
    number = int(input())

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88 and number != 86:      #Може да не проверявам дали е равно на 86, защото горната проверка вече е дала false
        print("GREAT!")
    elif number > 88:           #по същата логика може да се ползва директно else, защото горните проверки обхващат всички останали случаи
        print("Bye.")

