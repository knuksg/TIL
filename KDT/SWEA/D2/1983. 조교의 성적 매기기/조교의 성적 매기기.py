t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    scores = {}
    for j in range(n):
        scores[j+1] = list(map(int, input().split()))
        scores[j+1] = scores[j+1][0]*(35/100) + scores[j+1][1]*(45/100) + scores[j+1][2]*(20/100)
    new_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    cnt = 0
    rst = 0
    for x, y in new_scores:
        cnt += 1
        if x == k:
            rst = cnt / n * 100
            break
    print(f'#{i+1}', end=' ')
    if rst > 90:
        print('D0')
    elif rst > 80:
        print('C-')
    elif rst > 70:
        print('C0')
    elif rst > 60:
        print('C+')
    elif rst > 50:
        print('B-')
    elif rst > 40:
        print('B0')
    elif rst > 30:
        print('B+')
    elif rst > 20:
        print('A-')
    elif rst > 10:
        print('A0')
    else:
        print('A+')