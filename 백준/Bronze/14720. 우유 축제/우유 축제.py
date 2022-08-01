from collections import deque
n = int(input())
store = list(map(int, input().split()))
status = deque([0, 1, 2])
cnt = 0
for i in range(n):
    if store[i] == status[0]:
        cnt += 1
        status.append(status.popleft())
print(cnt)