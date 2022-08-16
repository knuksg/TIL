n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

rst_list = []

for sr in range(n):
    for sc in range(m):
        if not(sr+7<n and sc+7<m):
            continue
        cnt = 0
        for r in range(8):
            for c in range(8):
                nr = sr + r
                nc = sc + c

                if (r+c) % 2 == 0 and board[nr][nc] == 'W':
                    cnt += 1
                elif (r+c) % 2 != 0 and board[nr][nc] == 'B':
                    cnt += 1
        rst1 = cnt
        rst2 = 64-cnt
        rst_list.append(min(rst1, rst2))
print(min(rst_list))