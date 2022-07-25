a, b, c = map(int, input().split())
d = [a, b, c]
if a == b and b == c:
    print(10000+a*1000)
elif a == b or b == c:
    print(1000+b*100)
elif a == c:
    print(1000+a*100)
else:
    d.sort()
    print(d[2]*100)