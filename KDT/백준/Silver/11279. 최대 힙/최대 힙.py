import sys
input = sys.stdin.readline
import heapq
n = int(input())
number = []
for i in range(n):
    nn = int(input())
    if nn != 0:
        heapq.heappush(number, (-nn, nn))
    elif not len(number):
        print(0)
    else:
        print(heapq.heappop(number)[1])