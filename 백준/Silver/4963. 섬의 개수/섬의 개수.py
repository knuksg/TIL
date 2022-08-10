while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    dr = [0, 0, 1, -1, 1, -1, 1, -1]
    dc = [1, -1, 0, 0, 1, -1, -1, 1]

    '''
    [[1, 0, 1, 0, 0], 
    [1, 0, 0, 0, 0], 
    [1, 0, 1, 0, 1], 
    [1, 0, 0, 1, 0]]
    [[False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False]]
    '''

    stack = []
    dic_ = {}

    for r in range(h):
        for c in range(w):
            # 땅일 경우에만 시행.
            if not land[r][c]:
                continue
            # 이미 온 땅이 아닐 경우에만 시행.
            if visited[r][c] == True:
                continue

            visited[r][c] = True
            dic_[(r, c)] = []

            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
            
                if not (-1<nr<h and -1<nc<w):
                    continue
                if not land[nr][nc]:
                    continue
                dic_[(r, c)] = dic_.get((r, c), []) + [(nr, nc)]

    '''
    {(0, 0): [(1, 0)],
    (1, 0): [(2, 0), (0, 0)],
    (2, 0): [(3, 0), (1, 0)],
    (2, 2): [(3, 3)],
    (2, 4): [(3, 3)],
    (3, 0): [(2, 0)],
    (3, 3): [(2, 2), (2, 4)]}
    '''

    stack = []
    visited = []

    def dfs(start:tuple):
        stack = [start] # 돌아갈 곳을 기록 
        visited.append(start) # 시작 정점 방문 처리
        while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복 
            cur = stack.pop() # 현재 방문 정점(후입선출)

            for adj in dic_[cur]: # 인접한 모든 정점에 대해 
                if adj not in visited: # 아직 방문하지 않았다면
                    visited.append(adj) # 방문 처리 
                    stack.append(adj) # 스택에 넣기
    list_ = []
    cnt = 0
    for i in dic_:
        if i not in list_:
            dfs(i)
            cnt += 1
            for j in dic_:
                if j in visited:
                    list_.append(j)
    print(cnt)