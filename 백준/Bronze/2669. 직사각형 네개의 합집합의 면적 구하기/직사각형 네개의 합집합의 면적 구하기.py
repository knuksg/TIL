dic_ = dict()
square = []
for _ in range(4):
    square.append(list(map(int, input().split())))
for i in range(4):
    x = square[i]
    for r in range(x[0], x[2]):
        for c in range(x[1], x[3]):
            dic_[r, c] = 0
print(len(dic_))