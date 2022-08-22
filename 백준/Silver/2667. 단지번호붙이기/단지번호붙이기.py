n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = []

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(start:tuple):
    stack = [start]
    visited.append(start)
    cnt = 1
    while stack:
        current = stack.pop()
        for d in range(4):
            nr = current[0] + dr[d]
            nc = current[1] + dc[d]

            if not(-1<nr<n and -1<nc<n):
                continue
            if graph[nr][nc] == '0':
                continue
            if (nr, nc) in visited:
                continue

            visited.append((nr, nc))
            stack.append((nr, nc))
            cnt += 1
    return cnt

rst_list = []

for r in range(n):
    for c in range(n):
        if graph[r][c] == '0':
            continue
        if (r, c) in visited:
            continue
        rst_list.append(dfs((r, c)))
rst_list = sorted(rst_list, reverse=True)
print(len(rst_list))
while rst_list:
    print(rst_list.pop())