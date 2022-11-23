import sys
input = sys.stdin.readline
from collections import deque

deq = deque()
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deq.appendleft(int(command[1]))
        continue
    if command[0] == 'push_back':
        deq.append(int(command[1]))
        continue
    if command[0] == 'pop_front':
        if deq:
            print(deq.popleft())
            continue
        else:
            print(-1)
            continue
    if command[0] == 'pop_back':
        if deq:
            print(deq.pop())
            continue
        else:
            print(-1)
            continue
    if command[0] == 'size':
        print(len(deq))
        continue
    if command[0] == 'empty':
        if deq:
            print(0)
            continue
        else:
            print(1)
            continue
    if command[0] == 'front':
        if deq:
            print(deq[0])
            continue
        else:
            print(-1)
            continue
    if command[0] == 'back':
        if deq:
            print(deq[-1])
            continue
        else:
            print(-1)
            continue