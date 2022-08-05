import sys

sys.stdin = open("_민석이의과제체크하기.txt")

for i in range(int(input())):
    n, k = map(int, input().split())
    # 전체 출석 인원 집합과 과제 제출 인원 집합의 차집합 = 과제 미제출 인원 리스트.
    member = set(map(int, input().split()))
    all_member = set(range(1, n+1))
    result = list(all_member-member)
    print(f'#{i+1}', end=' ')
    for i in result:
        print(i, end=' ')
    print()