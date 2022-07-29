h, b, c, s = map(int, input().split())
rst = h * b * c * s / 8 / 1024 / 1024
print(f'{rst:.1f}', 'MB', sep=' ')