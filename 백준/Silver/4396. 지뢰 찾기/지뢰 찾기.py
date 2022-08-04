# 지뢰의 위치와 열림 여부가 각각 n x n 형태로 주어진다.
# 테두리를 '.'으로 감싼다.
n = int(input())
game1 = [['.']*(n+2)]
for _ in range(n):
    game1.append(list('.'+input()+'.'))
game1.append(['.']*(n+2))
game2 = [['.']*(n+2)]
for _ in range(n):
    game2.append(list('.'+input()+'.'))
game2.append(['.']*(n+2))


# 주위 여덟 칸을 판단할 count_ 리스트,
# 지뢰 위치, 열림 여부 둘 다 기록할 result_list 리스트 생성.

count_ = []
result_list = []
for r in range(1,n+1):
    result = []
    for c in range(1, n+1):
        # 열린 칸에 지뢰가 있으면 지뢰 표시.
        if game2[r][c] == 'x' and game1[r][c] == '*':
            result.append('*')
        # 열린 칸에 온점이 있으면 주변 여덟 칸 카운트 리스트에 넣고,
        # 카운트 리스트에 있는 지뢰 수를 result 리스트에 넣는다.
        elif game2[r][c] == 'x' and game1[r][c] == '.':
            for r1 in range(r-1, r+2):
                for c1 in range(c-1, c+2):
                    count_.append(game1[r1][c1])
            result.append(count_.count('*'))
            count_ = []
        # 닫힌 칸에 지뢰가 있으면 구분하기 쉽게 다른 기호를 리스트에 넣는다.
        elif game2[r][c] == '.' and game1[r][c] == '*':
            result.append('@')
        # 아무것도 아니면 그냥 온점 추가.
        else:
            result.append('.')
    result_list.append(result)

# [[0, 0, 1, '@', '@', '.', '.', '.'],
#  [0, 0, 1, 3, '.', '.', '@', '.'],
#  [0, 0, 0, 1, '@', '.', '.', '.'],
#  [0, 0, 0, 1, 1, '.', '.', '.'],
#  [0, 0, 0, 0, 1, '.', '.', '.'],
#  [0, 0, 1, 2, 3, '@', '.', '.'],
#  [0, 0, 1, '@', '@', '.', '@', '.'],
#  [0, 0, 1, 2, 3, '@', '.', '.']]

# 지뢰 밟았는지 판단하는 변수 생성.
gameover = False

# 리스트에 *가 있으면 게임오버.
for i in range(n):
    if '*' in result_list[i]:
        gameover = True

# 지뢰를 안 밟았으면 닫힌 칸에 있던 지뢰를 '.'으로 바꾸고 출력.
if gameover == False:
    for r in range(n):
        for c in range(n):
            if result_list[r][c] == '@':
                result_list[r][c] = '.'
            print(result_list[r][c], end='')
        print()
# 지뢰를 밟았으면 닫힌 칸에 있던 지뢰를 '*'로 바꾸고 출력.
else:
    for r in range(n):
        for c in range(n):
            if result_list[r][c] == '@':
                result_list[r][c] = '*'
            print(result_list[r][c], end='')
        print()