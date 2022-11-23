from collections import deque
m, n = map(int, input().split())

# 정사각형 설정
board = [[0]*(m+1) for _ in range(m+1)]

# 로봇 움직임 설정
command_list = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])

# 초기 위치, 방향 설정
robot = [0, 0]

# 명령어 입력
for i in range(n):
    command, number = input().split()
    direction = command_list[0]
    if command == 'MOVE':
        nr =  robot[0] + direction[0] * int(number)
        nc =  robot[1] + direction[1] * int(number)
        # 조건 1. 범위를 벗어나면 안 된다.
        if not(-1<nr<m+1 and -1<nc<m+1):
            print(-1)
            break
        robot[0] = nr
        robot[1] = nc
    elif command == 'TURN' and number =='0':
        command_list.append(command_list.popleft())
    elif command == 'TURN' and number =='1':
        command_list.appendleft(command_list.pop())
else:
    print(robot[1], robot[0])