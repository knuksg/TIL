numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # -60
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -100

result = numbers[0]

for i in numbers:
    if i < result:
        result = i
print(result)