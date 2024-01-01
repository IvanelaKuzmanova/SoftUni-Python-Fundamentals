command = input()

while command != "End":

    # if command == "SoftUni":
    #     command = input()
    #     continue

    if command != "SoftUni":
        doubled_text = ""

        for char in command:            #фор цикъл обхождащ символ по символ дадена прменлива
            doubled_text += char * 2    # директно принтира символът 2 пъти

        print(doubled_text)

    command = input()