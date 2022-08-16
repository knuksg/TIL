from collections import deque
import sys

sys.stdin = open("_암호생성기.txt")

for i in range(1, 11):
    n = int(input())
    number = deque(map(int, input().split()))
    cnt = 1
    while True:
        # 끝 숫자가 0 이하면 0으로 바꾸고 브레이크.
        if number[-1] <= 0:
            number[-1] = 0
            break
        # 한 차례 돌았으면 다시 초기화.
        if cnt > 5:
            cnt = 1
        # 제일 앞자리 숫자에 cnt를 빼주고 제일 뒤에 추가.
        number[0] -= cnt
        number.append(number.popleft())
        cnt += 1
    result = list(number)
    print(f'#{i}', end=' ')
    for i in result:
        print(i, end=' ')
    print()