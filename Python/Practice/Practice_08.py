numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30
max1 = numbers[0] # 첫 번째로 큰 수
max2 = numbers[0] # 두 번째로 큰 수

for i in numbers:
    if max1 < i:
        max1 = i
    if max1 > i:
        max2 = i   
print(max2)