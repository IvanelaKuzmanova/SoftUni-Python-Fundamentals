name = input()
forbidden_name = False

while name != "Welcome!":

    if name != "Voldemort":

        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        elif len(name) > 6:
            print(f"{name} goes to Hufflepuff.")

    else:
        print(f"You must not speak of that name!")
        forbidden_name = True
        break

    name = input()

if not forbidden_name:
    print(f"Welcome to Hogwarts.")