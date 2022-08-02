from collections import deque
n, k = map(int, input().split())
list_n = deque(range(1, n+1))
print('<', end='')
while len(list_n)>1:
    for i in range(1, k+1):
        list_n.append(list_n.popleft())
    print(list_n.pop(), end=', ')
print(list_n.pop(), end='')
print('>')