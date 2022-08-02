import sys
input = sys.stdin.readline
for _ in range(int(input())):
    r, e, c = map(int, input().split())
    if r - (e - c) < 0:
        print('advertise')
    elif r - (e - c) == 0:
        print('does not matter')
    else:
        print('do not advertise')