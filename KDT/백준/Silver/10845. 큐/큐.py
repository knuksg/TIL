import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
        continue
    if command[0] == 'pop':
        if queue:
            print(queue.popleft())
            continue
        else:
            print(-1)
            continue
    if command[0] == 'size':
        print(len(queue))
        continue
    if command[0] == 'empty':
        if queue:
            print(0)
            continue
        else:
            print(1)
            continue
    if command[0] == 'front':
        if queue:
            print(queue[0])
            continue
        else:
            print(-1)
            continue
    if command[0] == 'back':
        if queue:
            print(queue[-1])
            continue
        else:
            print(-1)
            continue