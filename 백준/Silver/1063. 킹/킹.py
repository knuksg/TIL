# 킹과 돌의 초기 위치 설정
king, dol, n = input().split()
k_a = ord(king[0])-65
k_1 = 8 - int(king[1])
d_a = ord(dol[0])-65
d_1 = 8 - int(dol[1])

# 초기 체스판 설정
board = [[0]*8 for _ in range(8)]
board[d_1][d_a] = dol
board[k_1][k_a] = king

# 명령어 설정
command_list = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [1, 0],
    'T': [-1, 0],
    'RT': [-1, 1],
    'LT': [-1, -1],
    'RB': [1, 1],
    'LB': [1, -1]
}

# 킹 이동
for _ in range(int(n)):
    # 명령 입력
    command = input()
    command = command_list[command]

    # 킹의 새 위치
    knr = k_1 + command[0]
    knc = k_a + command[1]
    
    # 조건 1. 범위를 벗어나면 안 된다.
    if not(-1<knr<8 and -1<knc<8):
        continue
    # 조건 2. 돌이 있으면 돌의 위치부터 옮긴다.
    if board[knr][knc] == dol:
        # 돌의 새 위치
        dnr = d_1 + command[0]
        dnc = d_a + command[1]

        # 조건 2-1. 돌의 새 위치가 범위를 벗어나면 안 된다.
        if not(-1<dnr<8 and -1<dnc<8):
            continue
        
        # 기존 위치 없애고, 새 위치에 돌 표시를 한다.
        board[d_1][d_a] = 0
        d_1 = dnr
        d_a = dnc
        board[d_1][d_a] = dol

        # 기존 위치 없애고, 새 위치에 킹 표시를 한다.
        board[k_1][k_a] = 0
        k_1 = knr
        k_a = knc
        board[k_1][k_a] = king

    # 기존 위치 없애고, 새 위치에 킹 표시를 한다.
    board[k_1][k_a] = 0
    k_1 = knr
    k_a = knc
    board[k_1][k_a] = king

# 마지막 위치 찾기
print(chr(k_a+65), 8 - k_1, sep='')
print(chr(d_a+65), 8 - d_1, sep='')