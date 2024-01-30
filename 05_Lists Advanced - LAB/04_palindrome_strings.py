words_list = input().split()
command = input()

palindromes_list = []

for word in words_list:

    reversed_word = word[::-1]

    if word == reversed_word:
        palindromes_list.append(word)

palindrome_count = palindromes_list.count(command)

print(palindromes_list)
print(f"Found palindrome {palindrome_count} times")

