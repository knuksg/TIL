t = int(input())
for i in range(t):
    n = int(input())
    print(f'#{i+1}')
    money_dic = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    while n >= 10:
        if n >= 50000:
            money_dic[50000] += n//50000
            n %= 50000
        elif n >= 10000:
            money_dic[10000] += n//10000
            n %= 10000
        elif n >= 5000:
            money_dic[5000] += n//5000
            n %= 5000
        elif n >= 1000:
            money_dic[1000] += n//1000
            n %= 1000
        elif n >= 500:
            money_dic[500] += n//500
            n %= 500
        elif n >= 100:
            money_dic[100] += n//100
            n %= 100
        elif n >= 50:
            money_dic[50] += n//50
            n %= 50
        elif n >= 10:
            money_dic[10] += n//10
            n %= 10
    for i in money_dic:
        if i != 10:
            print(money_dic[i], end=' ')
        else:
            print(money_dic[i])