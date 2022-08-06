from collections import deque
for i in range(1, 11):
    n = int(input())
    number = deque(map(int, input().split()))
    cnt = 1
    while True:
        if number[-1] <= 0:
            number[-1] = 0
            break
        if cnt > 5:
            cnt = 1
        number[0] -= cnt
        number.append(number.popleft())
        cnt += 1
    result = list(number)
    print(f'#{i}', end=' ')
    for i in result:
        print(i, end=' ')
    print()