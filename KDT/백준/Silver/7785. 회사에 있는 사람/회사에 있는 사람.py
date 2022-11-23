n = int(input())
member = {}
for i in range(n):
    name, now = input().split()
    member[name] = now
new_member = sorted(member.items(), reverse=True)
for i in range(len(new_member)):
    if new_member[i][1] == 'enter':
        print(new_member[i][0])