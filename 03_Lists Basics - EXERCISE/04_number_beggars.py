numbers_as_string = input()
beggars = int(input())

numbers_list = numbers_as_string.split(", ")

money = []
final_sums = []
start_index_for_beggar = 0

for n in numbers_list:         # използваме този цикъл само за да обърнем парите от стрингове в числа и да ги добавим в листа, с който ще работим
    money.append(int(n))

while start_index_for_beggar < beggars:       #първият започва да взима от индекс нула, последният от индекс броя на просяците-1
    current_beggar_sum = 0
    for current_index in range(start_index_for_beggar, len(money), beggars):        #на всяка итерация се добавя +1 към стартовия индекс за всеки
        current_beggar_sum += money[current_index]          #ще се извърти цикъл, който ще сметне общата сума за първия

    final_sums.append(current_beggar_sum)       #добавяме сметнатата сума и while цикълът започва отначало за следвашия човек докато има
    start_index_for_beggar += 1         #следващият започва да взима от следващ индекс през броя на просяците

print(final_sums)