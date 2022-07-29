import sys
from turtle import pu
sys.stdin = open("input.txt", "r")

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    puzzle = [input().split() for i in range(a)]
    print(puzzle)
    p1 = []
    p2 = []