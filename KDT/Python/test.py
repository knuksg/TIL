# import sys
# input = sys.stdin.readline
import heapq
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")


for _ in range(int(input())):
    k = int(input())
    n = int(input())
    def home(k, n):
        if k == 0:
            return n
        else:
            sum_ = 0
            for i in range(1, n+1):
                sum_ += home(k-1, i)
            return sum_
    print(home(k, n))