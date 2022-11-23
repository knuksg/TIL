import sys
input = sys.stdin.readline
import heapq
heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if not len(heap):
            print(0)
        else:
            a, b = heapq.heappop(heap)
            print(a*b)
    else:
        if x > 0:
            heapq.heappush(heap, [abs(x), 1])
        else:
            heapq.heappush(heap, [abs(x), -1])