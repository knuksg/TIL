# Python_Fuction

## Sort(key= , reverse=True/False)

```python
x = [{'a' : 10, 'b' : 20, 'c' : 30}, {'a' : 20, 'b' : 2, 'c' : 1}, {'a' : 20, 'b' : 30, 'c' : 10}]
# x는 딕셔너리를 요소로 가진 리스트!
print(x[0]['a'])
# x의 0번째 딕셔너리 의 'a' 값인 10이 출력된다.

#sort(key=lamda)를 사용할 때는 '요소'값만 있으면 된다.
x.sort(key=lambda x : x['a'])
# [{'a': 10, 'b': 20, 'c': 30}, {'a': 20, 'b': 2, 'c': 1}, {'a': 20, 'b': 30, 'c': 10}]
# 'a' 값을 기준으로 정렬된 모습.

x = [{'a' : 10, 'b' : 20, 'c' : 30}, {'a' : 20, 'b' : 2, 'c' : 1}, {'a' : 20, 'b' : 30, 'c' : 10}]
x.sort(key=lambda x : (x['a'], x['c']))
# [{'a': 10, 'b': 20, 'c': 30}, {'a': 20, 'b': 2, 'c': 1}, {'a': 20, 'b': 30, 'c': 10}]
# 'a' 값을 기준으로 정렬하고, 'a' 값이 같으면 그 다음 'c' 값으로 정렬.
```

## Find(찾을 문자, 시작 Index, 끝 Index)

```python
str= "BlockDMask Blog.";

# find 예제1
result1 = str.find('a')   # 문자가 있는 경우 : 7
result2 = str.find('Z')   # 문자가 없는 경우 : -1

result3 = str.find('ask') # 문자열이 있는 경우 : 7 (겹치는 문자열 중 a의 인덱스.)
result4 = str.find('kkk') # 문자열이 없는 경우 : -1

# find 예제2
result5 = str.find('o') # 2 (2, 13 o 중 먼저 나온 것의 인덱스만 표시.)
result6 = str.find('o', 5) # 13 (5번째 문자부터 시작해서 처음 마주친 o의 인덱스.)

# find 예제3
result7 = str.find('o') # 2
result8 = str.find('o', 5, 11)  # -1 "DMask B" (5~11 사이 o 가 없음.) 

출처: https://blockdmask.tistory.com/569 [개발자 지망생:티스토리]
```
