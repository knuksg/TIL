'''
테스트 케이스
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
'''
while True:
    # 지도의 너비와 높이를 입력받는다.
    w, h = map(int, input().split())
    # 마지막 줄에 0, 0이 들어오면 브레이크.
    if w == 0 and h == 0:
        break
    # land에는 지도를 입력하고, visited에는 각 지점에 방문했는지를 확인하기 위해 초기화한다.
    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

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

    dr = [0, 0, 1, -1, 1, -1, 1, -1]
    dc = [1, -1, 0, 0, 1, -1, -1, 1]

    stack = []
    dic_ = {}
    # 각 지점을 순회한다. 이어진 지점의 정보를 딕셔너리에 넣는다.
    for r in range(h):
        for c in range(w):
            # 땅일 경우에만 시행.
            if not land[r][c]:
                continue
            # 이미 온 땅이 아닐 경우에만 시행.
            if visited[r][c] == True:
                continue
            # 방문했다는 표시를 해주고, 딕셔너리에 추가한다.
            visited[r][c] = True
            dic_[(r, c)] = []
            # 여덟 방위를 돌면서 현재 지점과 이어져있는지 확인한다.
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                # 조건 1. 지점이 범위를 벗어나면 안 된다.
                if not (-1<nr<h and -1<nc<w):
                    continue
                # 조건 2. 지점이 바다(0)이면 안 된다.
                if not land[nr][nc]:
                    continue
                # 기준 좌표를 키로 넣고, 이동한 좌표를 값으로 넣는다.
                dic_[(r, c)] += [(nr, nc)]

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
    cnt = 0
    # 딕셔너리를 순회한다.
    for i in dic_:
        # 키가 리스트에 없으면 dfs 함수를 사용한다.
        if i not in visited:
            dfs(i)
            cnt += 1
    print(cnt)