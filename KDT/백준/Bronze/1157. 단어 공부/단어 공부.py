w = list(input())
w2 = []
for i in w:
    w2.append(ord(i))
word = {}
for i in w2:
    if i > 90:
        i -= 32
    word[i] = word.get(i, 0) + 1
list = sorted(word.items(), key=lambda x: x[1])
if len(list) == 1:
    print(chr(list[0][0]))
elif list[-1][1] == list[-2][1]:
    print('?')
else:
    print(chr(list[-1][0]))