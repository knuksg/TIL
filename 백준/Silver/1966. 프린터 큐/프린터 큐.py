from collections import deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
    new_number = deque([])
    for i in range(len(number)):
        new_number.append((number[i], i))
    number = sorted(number)
    cnt = 1
    while new_number:
        if new_number[0][0] == max(number):
            if new_number[0][1] == m:
                print(cnt)
            new_number.popleft()
            number.pop()
            cnt += 1
        else:
            new_number.append(new_number.popleft())