for _ in range(int(input())):
    m, n = map(int, input().split())
    mn = []
    for _ in range(m):
        mn.append(list(map(int, input().split())))
    # [[1, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0]]
    box = []
    for c in range(n):
        col = []
        for r in range(m):
            col.append(mn[r][c])
        box.append(col[::-1])
    # [[1, 0, 1, 0, 1], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 0]]
    cnt = 0
    for r in range(n):
        for c in range(m):
            if box[r][c] == 1:
                cnt += [box[r][c] for c in range(c+1)].count(0)
    print(cnt)