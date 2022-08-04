n = int(input())
game1 = [['.']*(n+2)]
for _ in range(n):
    game1.append(list('.'+input()+'.'))
game1.append(['.']*(n+2))
game2 = [['.']*(n+2)]
for _ in range(n):
    game2.append(list('.'+input()+'.'))
game2.append(['.']*(n+2))

count_ = []
result_list = []
for r in range(1,n+1):
    result = []
    for c in range(1, n+1):
        if game2[r][c] == 'x' and game1[r][c] == '*':
            result.append('*')
        elif game2[r][c] == 'x' and game1[r][c] == '.':
            for r1 in range(r-1, r+2):
                for c1 in range(c-1, c+2):
                    count_.append(game1[r1][c1])
            result.append(count_.count('*'))
            count_ = []
        elif game2[r][c] == '.' and game1[r][c] == '*':
            result.append('@')
        else:
            result.append('.')
    result_list.append(result)

gameover = False
for i in range(n):
    if '*' in result_list[i]:
        gameover = True
if gameover == False:
    for r in range(n):
        for c in range(n):
            if result_list[r][c] == '@':
                result_list[r][c] = '.'
            print(result_list[r][c], end='')
        print()
else:
    for r in range(n):
        for c in range(n):
            if result_list[r][c] == '@':
                result_list[r][c] = '*'
            elif result_list[r][c] == '*':
                result_list[r][c] = '*'
            print(result_list[r][c], end='')
        print()