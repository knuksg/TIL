game = []
n = int(input())
m = 3
for _ in range(n):
    game.append(list(map(int, input().split())))
score_list = [0] * n
for i in range(m):
    score_dic = dict()
    for j in range(n):
        score = game[j][i]
        if score_dic.get(score) == None:
            score_dic[score] = score
        else:
            score_dic[score] = 0
    for j in range(n):
        score_list[j] += score_dic[game[j][i]] 
for i in range(len(score_list)):
    print(score_list[i])