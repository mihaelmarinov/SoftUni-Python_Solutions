n = int(input())
word = input()

list_of_words = []
filtered_words = []

for i in range(n):
    words = input()
    list_of_words.append(words)

for k in list_of_words:
    if word in k:
        filtered_words.append(k)

print(list_of_words)
print(filtered_words)
