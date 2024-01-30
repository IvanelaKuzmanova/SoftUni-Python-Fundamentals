train = [0] * int(input())      #all wagons should be represented with zeroes
command = input().split()       #to separate command to separate elements in list

while True:

    if command[0] == "End":
        print(train)
        break
    elif command[0] == "add":
        people_number = int(command[1])
        train[-1] += people_number         #-1 always represents the last element in list

    elif command[0] == "insert":
        wagon_to_add_to = int(command[1])
        people_number = int(command[2])
        train[wagon_to_add_to] += people_number

    elif command[0] == "leave":
        wagon_to_remove_from = int(command[1])
        people_number = int(command[2])
        train[wagon_to_remove_from] -= people_number

    command = input().split()