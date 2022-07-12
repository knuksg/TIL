numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # 100
# numbers = [0, 1, 0] # 1
# numbers = [-10, -100, -30] # -10 

result = numbers[0]
for i in numbers:
    if result < i:
        result = i
print(result)