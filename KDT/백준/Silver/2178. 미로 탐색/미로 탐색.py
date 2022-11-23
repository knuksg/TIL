from collections import deque
# 초기 입력
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 델타 탐색 준비
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 방문 체크
visited = [[False]*m for _ in range(n)]

# bfs 함수
def bfs(r, c):
    stack = deque([((r, c), 0)])
    visited[r][c] = True
    # 스택이 빌 떄까지
    while stack:
        # 좌표와 순번을 입력
        move, number = stack.pop()
        # 마지막 위치에 도달하면 종료
        if move == (n-1, m-1):
            break
        # 델타 탐색
        for d in range(4):
            nr = move[0] + dr[d]
            nc = move[1] + dc[d]

            # 조건 1. 범위를 벗어나면 안 된다.
            if not(-1<nr<n and -1<nc<m):
                continue
            # 조건 2. 이동할 수 없는 칸이면 안 된다.
            if board[nr][nc] == '0':
                continue
            # 조건 3. 이미 방문한 칸이면 안 된다.
            if visited[nr][nc]:
                continue

            # 델타 탐색한 지점을 방문 처리하고, 스택에 넣는다.
            visited[nr][nc] = True
            stack.appendleft(((nr, nc), number+1))
    return number

print(bfs(0, 0)+1)