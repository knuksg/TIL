import sys
sys.stdin = open("input.txt", "r")

N = int(input())
sang_card = input().split()
M = int(input())
M_card = input().split()
rst = [0]*M
print(rst)
for i in M_card:
    for j in sang_card:
        if i == j:
            rst[i] += 1
print(rst)