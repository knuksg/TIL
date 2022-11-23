dic_ = {}
a, b, c = map(int, input().split())
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        dic_[i] = dic_.get(i, 0) + 1
rst = 0
for i in dic_:
    if dic_[i] == 1:
        rst += a
    elif dic_[i] == 2:
        rst += 2*b
    elif dic_[i] == 3:
        rst += 3*c
print(rst)