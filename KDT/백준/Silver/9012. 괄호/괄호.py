for _ in range(int(input())):
    VPS = []
    word = list(input())
    for i in range(len(word)):
        if word[i] == '(':
            VPS.append('(')
        elif len(VPS) != 0 and word[i] == ')':
            VPS.pop()
        else:
            VPS.append('NO')
            break
    if len(VPS) == 0:
        print('YES')
    else:
        print('NO')