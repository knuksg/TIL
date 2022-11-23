number = []
for i in range(1, 9):
    number.append((int(input()), i))
score = 0
new_number = sorted(number)
list_ = []
for i in range(3, 8):
    score += new_number[i][0]
    list_.append(new_number[i][1])
print(score)
print(*sorted(list_))