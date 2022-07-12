numbers = [4, 10, 20]
result = 0
a = 0
for i in numbers:
    result += i
    a += 1
result /= a
result = round(result)
print(f'{result:.1f}')