n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

def dfs(start):
    stack = [start] # 돌아갈 곳을 기록 
    visited[start] = True # 시작 정점 방문 처리
    while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복 
        cur = stack.pop() # 현재 방문 정점(후입선출)
        
        for adj in graph[cur]: # 인접한 모든 정점에 대해 
            if not visited[adj]: # 아직 방문하지 않았다면
                visited[adj] = True # 방문 처리 
                stack.append(adj) # 스택에 넣기
list_ = []
cnt = 0
for i in range(1, n+1):
    if i not in list_:
        dfs(i)
        cnt += 1
        for j in range(1, n+1):
            if visited[j] == True:
                list_.append(j)
print(cnt)