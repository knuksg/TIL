happy = 0
sad = 0
word = list(input())
for w in range(len(word)):
    if word[w] != ':':
        continue
    if not (w+1 < len(word) and w+2 < len(word)):
        continue
    if word[w+1] == '-' and word[w+2] == ')':
        happy += 1
    elif word[w+1] == '-' and word[w+2] == '(':
        sad += 1
if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
else:
    print('unsure')