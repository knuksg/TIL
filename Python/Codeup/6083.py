r, g, b = map(int, input().split())
rgb = 0
for x in range(r):
    for y in range(g):
        for z in range(b):
            print(x, y, z, sep=' ')
            rgb += 1
print(rgb)