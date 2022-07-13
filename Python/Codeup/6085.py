w, h, b = map(int, input().split())
whb = w * h * b / 8 / 1024 / 1024
print(f'{whb:.2f} MB')