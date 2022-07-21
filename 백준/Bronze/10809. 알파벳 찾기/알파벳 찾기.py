S = list(input())
alphabet = {}
for i in range(97, 123):
    alphabet[i] = -1
for i in S:
    if alphabet[ord(i)] == -1:
        alphabet[ord(i)] = S.index(i)
for i in range(97, 123):
    print(alphabet[i], end=' ')