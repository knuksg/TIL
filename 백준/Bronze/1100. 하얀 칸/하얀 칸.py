board = []
cnt = 0
for _ in range(8):
    board.append(list(input()))
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if board[i][j] == 'F':
                cnt += 1
print(cnt)