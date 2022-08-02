import sys
input = sys.stdin.readline
import heapq
list_ = []
for _ in range(int(input())):
    heapq.heappush(list_, int(input()))
for _ in range(len(list_)):
    print(heapq.heappop(list_))