happiness_list = [int(num) for num in input().split()]
improvement_factor = int(input())

total_happiness = [num * improvement_factor for num in happiness_list]

print(total_happiness)
print(happiness_list)