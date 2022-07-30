n = int(input())
number = {*map(int, input().split())}
m = int(input())
m_number = list(map(int, input().split()))
for i in range(m):
    if m_number[i] in number:
        print(1, end=' ')
    else:
        print(0, end=' ')