from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack.extend(reversed(sorted(graph[current])))
    return visited

def bfs(start):
    queue = deque([start])
    visited = []

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            queue.extend(sorted(graph[current]))
    return visited

print(*dfs(v))
print(*bfs(v))