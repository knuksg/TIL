from collections import deque
n = int(input())
stack = deque(range(n, 0, -1))
while len(stack) != 1:
    stack.pop()
    stack.appendleft(stack.pop())
print(stack[0])