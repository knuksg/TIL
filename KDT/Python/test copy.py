# from collections import deque
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
member = {}
for _ in range(n):
    nn = input()
    member[nn] = member.get(nn, 0) + 1
for _ in range(n-1):
    nn = input()
    member[nn] -= 1
print(sorted(member.items(), key=lambda x:x[1])[-1][0])