from collections import deque

n = int(input())
m = int(input())
if m != 0:
    broken = set(input().split())
    deq = deque()

    if n >= 100:
        for i in range(100, 1000001):
            if len(set(list(str(i))) & broken) == 0:
                deq.append((abs(i-n), i))
    else:
        for i in range(100):
            if len(set(list(str(i))) & broken) == 0:
                deq.append((abs(i-n), i))
    if deq:
        min_ = min(deq)
        if abs(n-min_[1])+len(str(min_[1])) < abs(n-100):
            print(abs(n-min_[1]) + len(str(min_[1])))
        else:
            print(abs(n-100))
    else:
        print(abs(n-100))
else:
    if abs(n-100) > len(str(n)):
        print(len(str(n)))
    else:
        print(abs(n-100))