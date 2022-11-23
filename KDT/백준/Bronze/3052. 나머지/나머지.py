import sys
input = sys.stdin.readline

ten = []
while len(ten) <= 9:
    ten.append(int(input())%42)
print(len(set(ten)))