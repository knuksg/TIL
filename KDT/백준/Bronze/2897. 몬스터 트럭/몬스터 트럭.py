# 주차장 상황 입력.
r, c = map(int, input().split())
parking_lot = []
for _ in range(r):
    parking_lot.append(list(input()))

# 기준, 오른쪽, 오른쪽 아래, 아래쪽.
dr = [0,0,1,1]
dc = [0,1,1,0]

# 몇 대를 부수고 주차할 수 있는지 변수 설정.
parking = [0] * 6

for r1 in range(r):
    for c1 in range(c):
        # 빌딩이 아닐 때만 델타 탐색을 수행.
        if parking_lot[r1][c1] != '#':
            # 델타 탐색.
            cnt = 0
            for d in range(4):
                # 다음 좌표 탐색
                nr = r1 + dr[d]
                nc = c1 + dc[d]
                # 조건: 범위를 벗어나거나, 빌딩이 있을 경우 브레이크.
                if not(-1<nr<r and -1<nc<c):
                    cnt = 5
                    break
                if parking_lot[nr][nc] == '#':
                    cnt = 5
                    break
                # 부술 차 만큼 카운트 추가.
                if parking_lot[nr][nc] == 'X':
                    cnt += 1
            parking[cnt] += 1
for i in range(5):
    print(parking[i])