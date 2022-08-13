dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    maps = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1
    
    cnt = 0

    for sr in range(n):
        for sc in range(m):

            if visited[sr][sc]:
                continue
            if not maps[sr][sc]:
                continue
            
            cnt += 1

            stack = [(sr, sc)]
            visited[sr][sc] = True

            while stack:
                current = stack.pop()

                for d in range(4):
                    nr = current[0] + dr[d]
                    nc = current[1] + dc[d]

                    if not(-1<nr<n and -1<nc<m):
                        continue
                    if visited[nr][nc]:
                        continue
                    if not maps[nr][nc]:
                        continue

                    visited[nr][nc] = True
                    stack.append((nr, nc))
    print(cnt)
    cnt = 0