words = input()
words_list = list(words)

converted_words = []

for i in range(len(words_list)):
    converted_words.append(words_list.pop())

print("".join(converted_words))
