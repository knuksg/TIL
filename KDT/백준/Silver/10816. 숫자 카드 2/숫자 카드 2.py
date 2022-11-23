N = int(input())
sang_card = input().split()
M = int(input())
M_card = input().split()
sang_card_dic = {}
for i in sang_card:
    sang_card_dic[i] = sang_card_dic.get(i, 0) + 1
for i in range(M):
    print(sang_card_dic.get(M_card[i], 0), end=' ')