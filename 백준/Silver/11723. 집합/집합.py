import sys
input = sys.stdin.readline
n = int(input())
s = set()
for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        s.add(command[1])
    elif command[0] == 'remove':
        if command[1] in s:
            s.remove(command[1])
    elif command[0] == 'check':
        if command[1] in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if command[1] in s:
            s.remove(command[1])
        else:
            s.add(command[1])
    elif command[0] == 'all':
        s = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
    elif command[0] == 'empty':
        s = set()