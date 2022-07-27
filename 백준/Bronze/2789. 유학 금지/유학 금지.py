word = input()
new_word = ''
for i in range(len(word)):
    if word[i] not in 'CAMBRIDGE':
        new_word += word[i]
print(new_word)