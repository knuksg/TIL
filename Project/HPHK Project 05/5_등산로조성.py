from collections import deque
import sys

sys.stdin = open("_등산로조성.txt")

'''
한 지점에서 뻗어나가는 등산로를 찾아야 함. (bfs, 촌수 계산 문제)
델타 탐색을 하는데, 숫자가 낮아야 한다는 조건으로 탐색해야 함.
모든 지점에 돌아가면서 최대 K번을 빼주고, 탐색을 함.
'''

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(r, c):
    queue = deque([(r, c, 0)])
    visited[r][c] = True
    while queue:
        r, c, number = queue.popleft()

        # 델타 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 조건 1. 범위를 벗어나면 안 된다.
            if not(-1<nr<n and -1<nc<n):
                continue
            # 조건 2. 현재 봉우리보다 낮아야 한다.
            if not(maps[r][c] > maps[nr][nc]):
                continue

            # 델타 탐색한 지점을 방문처리하고, 큐에 넣는다.
            visited[nr][nc] = True
            queue.append((nr, nc, number + 1))

    return number+1

for i in range(int(input())):
    # 초기 입력
    n, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    number_list = []

    # 모든 숫자에 돌아가면서 1~k번 빼주기
    for k in range(K+1):
        for ar in range(n):
            for ac in range(n):

                # 조건. 지형이 0보다 낮아지면 안 된다.
                if maps[ar][ac] - k < 0:
                    continue

                # 가장 높은 봉우리의 높이
                max_ = -1
                for x in maps:
                    if max(x) >= max_:
                        max_ = max(x)

                # k만큼 깎는다.
                maps[ar][ac] -= k

                # 탐색
                for sr in range(n):
                    for sc in range(n):

                        # 조건 1. 가장 높은 봉우리가 아니면 안 된다.
                        if maps[sr][sc] != max_:
                            continue
                        # 조건 2. 이미 방문한 곳이면 안 된다.
                        if visited[sr][sc]:
                            continue     
                        number_list.append(bfs(sr, sc))

                # 탐색 후 초기화
                visited = [[False] * n for _ in range(n)]

                # k만큼 다시 복구한다.
                maps[ar][ac] += k

    print(f'#{i+1} {max(number_list)}')