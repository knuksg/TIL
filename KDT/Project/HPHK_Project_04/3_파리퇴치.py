import sys

sys.stdin = open("_파리퇴치.txt")

for t in range(int(input())):
    n, m = map(int, input().split())
    n_list = []
    for i in range(n):
        n_list.append(list(map(int, input().split())))
    sum_ = []
    sum_list = []
    # (0, 0)을 기준으로 (m, m)까지 판단할 것이기 때문에,
    # 레인지에서 n-m의 차이만큼 빼준다.
    for r in range(n-m+1):
        for c in range(n-m+1):
            #(0, 0)에서 (m, m)까지 속한 모든 값을 더해서 리스트에 추가.
            for r1 in range(m):
                for c1 in range(m):
                    sum_.append(n_list[r+r1][c+c1])
            sum_list.append(sum(sum_))
            sum_ = []
    # 리스트 중 가장 높은 값 출력.
    print(f'#{t+1} {max(sum_list)}')