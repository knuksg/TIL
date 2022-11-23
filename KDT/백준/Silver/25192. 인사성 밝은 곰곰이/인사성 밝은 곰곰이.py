cnt = 0
member = set()
for _ in range(int(input())):
    w = input()
    if w == 'ENTER':
        cnt += len(member)
        member.clear()
    else:
        member.add(w)
cnt += len(member)
print(cnt)