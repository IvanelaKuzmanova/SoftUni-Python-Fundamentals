string_word = input()
counter = int(input())

repeated = lambda a, b: a * b

combined = repeated(string_word, counter)

print(combined)
