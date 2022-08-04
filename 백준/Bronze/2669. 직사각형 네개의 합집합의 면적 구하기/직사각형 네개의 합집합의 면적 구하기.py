dic_ = dict()
square = []
for _ in range(4):
    square.append(list(map(int, input().split())))
for i in range(4):
    x = square[i]
    for r in range(x[0], x[2]):
        for c in range(x[1], x[3]):
            dic_[r, c] = 0
# 위치 좌표를 전부 딕셔너리에 넣고 딕셔너리의 길이를 구하면 총 넓이와 같다!
print(len(dic_))