member = []
for _ in range(9):
    member.append(int(input()))
for i in range(8):
    for j in range(i+1, 9):
        if sum(member) - (member[i]+member[j]) == 100:
            a, b = member[i], member[j]
member.remove(a)
member.remove(b)
member.sort()
for i in range(7):
    print(member[i])