Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0
for _ in range(int(input())):
    r, c = map(int, input().split())
    if 0 < r and 0 < c:
        Q1 += 1
    elif 0 > r and 0 < c:
        Q2 += 1
    elif 0 > r and 0 > c:
        Q3 += 1
    elif 0 < r and 0 > c:
        Q4 += 1
    else:
        AXIS += 1
print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')