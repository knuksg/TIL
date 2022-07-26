N = int(input())

def saengsung(n:int):
    list_ = list(map(int, (str(n)))) 
    # int로 들어온 값을 리스트로 변환하기 위해 str로 형변환 후 다시 map 적용.
    return sum(list_) + n # 'sum(list_) + n'의 생성자가 'n'

number = 0
while saengsung(number) != N: 
    # 함수의 결과값이 N일 때, 즉 N의 생성자 number를 찾을 때까지
    if number < N:
        number += 1
    else:
        break
if number >= N: # 
    print('0')
else:
    print(number)