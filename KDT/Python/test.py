# import sys
# input = sys.stdin.readline
import heapq
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")


n = input()
start = int(n)
for i in range(40, 41):
    number = [start]
    len_number = len(number)
    while start:
        start -= i
        number.append(start)
        i = number[-1]
    print(number)
    start = int(n)