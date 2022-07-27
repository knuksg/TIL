t = int(input())
month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for i in range(t):
    result = 0
    fst_m, fst_d, snd_m, snd_d = map(int, input().split())
    if fst_m == snd_m:
        result += (snd_d - fst_d + 1)
        print(f'#{i+1} {result}')
    else:
        months = []
        days = snd_d - fst_d +1
        for j in range(fst_m, snd_m):
            months.append(j)
        for j in months:
            days += month.get(j)
        print(f'#{i+1} {days}')