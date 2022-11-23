from collections import deque
# 초기 입력
n, m = map(int, input().split())
drawing = [list(map(int, input().split())) for _ in range(n)]

stack = deque([])
visited = [[False] * m for _ in range(n)]
drawing_list = []

# 델타 탐색 준비
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    cnt = 1
    if drawing[r][c]:
        stack = [[r, c]]
        visited[r][c] = True
        while stack:
            r, c = stack.pop()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (-1<nr<n and -1<nc<m):
                    continue
                if not drawing[nr][nc]:
                    continue
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append([nr, nc])
                    cnt += 1
    return cnt

for r in range(n):
    for c in range(m):
        if visited[r][c]:
            continue
        if not drawing[r][c]:
            continue
        drawing_list.append(dfs(r, c))

if drawing_list:        
    print(len(drawing_list))
    print(max(drawing_list))
else:
    print(0)
    print(0)