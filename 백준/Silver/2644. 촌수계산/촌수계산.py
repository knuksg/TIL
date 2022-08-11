# 초기 입력
n = int(input())
start, end = map(int, input().split())
m = int(input())

# 초기 설정
people = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 관계 입력
for _ in range(m):
    u, v = map(int, input().split())
    people[u].append(v)
    people[v].append(u)

def dfs(start):
    stack = [(start, 0)]
    visited[start] = True
    while stack:
        name, number = stack.pop()
        if name == end:
            break
        for adj in people[name]:
            if not visited[adj]:
                visited[adj] = True
                stack.append((adj, number+1))
    else:
        number = -1
    return number

print(dfs(start))