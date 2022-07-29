# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

n = 2
m = 1

while n != 10:
    print(f'{n}단')
    while m != 10:
        print(f'{n} X {m} = {n * m}')
        m += 1
    m = 1
    n += 1