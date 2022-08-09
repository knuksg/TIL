dr = [0, 1, -1, 1]
dc = [1, 0, 1, 1]
black = 1
white = 2
n = 19

board = []

# 오목판 상황 입력
for _ in range(n):
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

answer = 0

# 이중 반복문
for r in range(n):
    for c in range(n):
        # 검은색 돌이나 흰색 돌일 떄만 델타 탐색을 수행.
        if board[r][c] == black or board[r][c] == white:
            
            # 델타 탐색
            for d in range(4):
                # 방향이 바뀔 때마다 갱신
                stone_count = 1
                
                # 다음 좌표 탐색
                nr = r + dr[d]
                nc = c + dc[d]

                while True:
                    # 인덱스 조건
                    if not(-1 < nr < n and -1 < nc < n):
                        break
                    # 같은색 돌인지 확인하는 조건
                    if not(board[r][c] == board[nr][nc]):
                        break

                    # 같은 값이고 범위를 벗어나지 않으면
                    stone_count += 1

                    # 같은 방향 다음 좌표를 탐색
                    nr = nr + dr[d]
                    nc = nc + dc[d]
                
                # 돌의 개수가 5개라면        
                if stone_count == 5:
                    prev_r = r - dr[d]
                    prev_c = c - dc[d]

                    # 육목인지 판단
                    # 조건 1. 이전 좌표가 범위를 벗어나면 오목
                    # 조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
                    if not(-1 < prev_r < n and -1 < prev_c < n) or board[r][c] != board[prev_r][prev_c]:
                        # answer 값 갱신
                        answer = board[r][c]
                        # 현재 돌의 색 출력
                        print(board[r][c])
                        # 현재 돌의 좌표를 출력
                        print(r + 1, c + 1)

# 전체를 반복했는데 무승부.
if answer == 0:
    print(answer)