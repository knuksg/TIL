import sys

sys.stdin = open("_창용마을무리의개수.txt")


def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        current = stack.pop()
        for adj in graph[current]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

for i in range(int(input())):
    cnt = 0
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for j in range(1, n+1):
        if not visited[j]:
            dfs(j)
            cnt += 1
    print(f'#{i+1} {cnt}')