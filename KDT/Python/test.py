# import sys
# input = sys.stdin.readline
from collections import deque
import heapq
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

def odd(n):
  	return n % 2
numbers = [1, 2, 3]
result = list(filter(odd, numbers))
print(result)