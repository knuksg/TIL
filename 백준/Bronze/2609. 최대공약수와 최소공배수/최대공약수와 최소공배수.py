a, b = map(int, input().split())
def max_(a, b):
    if a > b:   
        while a % b != 0:
            r = a % b
            a = b
            b = r
        return b
    elif a == b:
        return b
    else:
        while b % a != 0:
            r = b % a
            b = a
            a = r
        return a
def min_(a, b):
    return a*b/max_(a,b)
print(max_(a, b))
print(f'{min_(a, b):.0f}')