from collections import deque

distance = [0]*2000001

n, k = map(int, input().split())

def bfs(start):
    queue = deque([start])

    while queue:

        current = queue.popleft()

        if current == k:
            break

        for d in [+1, current, -1]:
            if current > k and not (d == -1):
                continue
            adj = current+d
            if adj < 0:
                continue
            if not distance[adj]:
                distance[adj] = distance[current] + 1
                queue.append(adj)
    return distance

print(bfs(n)[k])