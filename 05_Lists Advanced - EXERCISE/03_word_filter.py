even_length_words = [x for x in input().split() if len(x) % 2 == 0]

# for element in even_length_words:
#     print(element)

print("\n".join(even_length_words))
