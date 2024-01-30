def palindromes_check(my_list:list):

    palindromes_list = []

    for word in words_list:

        reversed_word = word[::-1]

        if word == reversed_word:
            palindromes_list.append(word)

    palindrome_count = palindromes_list.count(command)

    return f"{palindromes_list}\nFound palindrome {palindrome_count} times"

words_list = input().split()
command = input()

result = palindromes_check(words_list)
print(result)

