for i in range(int(input())):
    n, k = map(int, input().split())
    member = set(map(int, input().split()))
    all_member = set(range(1, n+1))
    result = list(all_member-member)
    print(f'#{i+1}', end=' ')
    for i in result:
        print(i, end=' ')
    print()