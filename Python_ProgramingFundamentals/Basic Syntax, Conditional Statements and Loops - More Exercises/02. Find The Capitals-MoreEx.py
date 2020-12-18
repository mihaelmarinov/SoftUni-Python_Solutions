word = input()
word_list = list(word)

capitol = []

for i in range(len(word_list)):
    if word_list[i].isupper():
        capitol.append(i)

print(capitol)
