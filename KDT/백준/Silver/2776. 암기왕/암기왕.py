import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    n_list = set(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))
    for i in range(m):
        if m_list[i] in n_list:
            print(1)
        else:
            print(0)