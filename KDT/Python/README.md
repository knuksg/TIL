# Python
<details>
<summary>기초</summary>
<div markdown="1">
# 기초

## 1. 개요
- 파이썬은 1990년 귀도 반 로섬이 개발한 인터프리터 언어이다.

## 2. 특징
- 배우기 쉬운 언어
  - 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않다.
  - 문법 표현이 매우 간결하다.
- 인터프리터 언어
  - 소스 코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능하다.

- 객체 지향 프로그래밍
  - 파이썬은 모든 것이 객체로 구현되어 있다.
  - 객체(object): 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것.

## # 참고 자료
[점프 투 파이썬](https://wikidocs.net/book/1)
</div>
</details>

<details>
<summary>조건/반복문</summary>
<div markdown="1">
# 조건/반복문

## 1. 개요
- 조건/반복문은 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 파이썬의 문법이다.

## 2. 조건문
- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 쓴다.
```python
if < expression >:
    # Run this Code block
else:
		# Run this Code block
```
- 복수의 조건문을 활용할 경우 `elif`를 사용한다.
```python
if <expression>: 
  	# Code block
elif <expression>:
    # Code block
elif <expression>:
    # Code block
else:
		# Code block
```
- 중첩 조건문을 활용할 경우 들여쓰기를 유의하여 작성한다.
```python
if <expression>:
    # Code block
		if <expression>:
				# Code block
else:
		# Code block
```
- 조건 표현식은 간단한 조건문을 나타낼 때 사용한다.
```python
<true인 경우 값> if <expression> else <false인 경우 값>
```

## 3. 반복문
- 반복문은 특정 조건에 도달할 때까지 계속 반복되는 파이썬의 문법이다.
  - while: 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 한다.
  - for: 반복가능한 객체를 모두 순회하면 종료된다.
  - 반복 제어: break, continue, for-else
- while: 조건식이 참인 경우 코드를 반복한다.
```python
 while <expression>: 
    	# Code block
```
- for: 순회가능한 객체 요소를 모두 순회한다.
```python
 for <변수명> in <iterable>: 
    	# Code block
```
- break: 반복문을 종료한다.
- continue: 컨티뉴 이후 코드 블록은 실행하지 않고, 다음 반복으로 넘어간다.
- for-else: 끝까지 반복문을 실행한 후 else문을 실행한다. 단, break를 통해 중간에 종료된 경우, else문은 실행되지 않는다.
</div>
</details>

<details>
<summary>기초</summary>
<div markdown="1">
</div>
</details>

<details>
<summary>함수</summary>
<div markdown="1">
# 함수

## 1. 개요
- 함수는 특정한 기능을 하는 코드의 묶음이다.

## 2. 함수 기초
- 사용자 함수: 구현되어 있는 함수가 없을 경우 직접 함수를 작성할 수 있다.
```python
 def function_name(parameter):
    # code block
    return returning_value
```
- 함수의 선언은 def 키워드를 활용한다.
- 들여쓰기를 통해 실행될 코드 블록을 작성한다.
- 함수는 parameter를 넘겨줄 수 있다.
- 함수는 동작 후에 return을 통해 결과값을 전달한다.

## 3. 함수의 결과값
- 함수는 반드시 값을 하나만 return한다. 명시적인 return이 없는 경우에도 None을 반환한다.
- 함수는 return과 동시에 실행이 종료된다.

## 4. 함수의 입력
- parameter: 함수를 실행할 때 함수 내부에서 사용되는 식별자이다.
- argument: 함수를 호출할 때 넣어주는 값이다.
```python
def function(ham): # parameter : ham
    return ham

function('spam')   # argument: 'spam'
```
- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않을 수 있다.
```python
def add(x, y=0): 
 	  return x + y

add(2)
```
- 몇 개의 argument를 받을지 모르는 함수를 정의할 때 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용한다.
```python
def add(*args): 
		for arg in args: 
      	print(arg)
      
add(2)      
add(2, 3, 4, 5) 
```
- 몇 개의 keyword argument를 받을지 모르는 함수를 정의할 때 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용한다.
```python
def family(**kwargs):
		for key, value in kwargs:
				print(key, ":", value) 

family(father='John', mother='Jane', me='John Jr.')
```

## 5. 함수의 응용
### map(function, iterable)
- 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환한다.
```python
m, n = map(int, input().split())
```
### Sort(key= , reverse=True/False)
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
### Find(찾을 문자, 시작 Index, 끝 Index)
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
</div>
</details>

<details>
<summary>데이터 구조</summary>
# 데이터 구조

## 1. 숫자형

- 정수형

```python
n = 123
n = -123
n = 0
```

- 실수형

```python
a = 1.23
a = -1.23
```

- 8진수와 16진수 (8진수는 0o로 시작, 16진수는 0x로 시작)

```python
a = 0o177
a = 0xABC
```

- 사칙연산

```python
a = 3
b = 4
a + b #덧셈
7
a - b #뺄셈
-1
a * b #곱셈
12
a / b #나눗셈
0.75
```

- 거듭제곱

```python
a = 3
b = 4
a ** b #a의 b제곱
81
```

- 몫과 나머지

```python
7 / 4 #나눗셈
1.75
7 // 4 #몫
1
7 % 4 #나머지
3
```

## 2. 문자열 자료형

- 문자열 나타내기

```python
'문장 양 끝에 작은따옴표나 큰 따옴표를 써서 표현할 수 있다.'
"단, 문장 속에 강조할 부분이 있다면 '반대되는' 부호를 써서 표기해야 한다."
'백슬래시를 써서 "큰따옴표"나 "작은따옴표"를 사용할 수도 있다.'
```

- 개행

```python
'여러 줄의 문자열을 나타내기 위해서 ""\n" 코드를 사용할 수 있다.'
'''
혹은 연속된 작은따옴표나,
큰따옴표 세 개를 사용해도 된다.
'''
```

- 문자열 더하기 & 곱하기

```python
>>> head = "Python"
>>> tail = " is fun!"
>>> head + tail
'Python is fun!'

>>> a = "python"
>>> a * 2
'pythonpython'
```

- 문자열 길이 구하기

```python
>>> a = "Life is too short"
>>> len(a)
17
```

- 문자열 인덱싱
  - **"파이썬은 0부터 숫자를 센다."**


```python
>>> a = "Life is too short, You need Python"

# Life is too short, You need Python 
# 0         1         2         3   (십의 자리)
# 0123456789012345678901234567890123(일의 자리)

>>> a[3]
'e'
```

- 문자열 인덱싱 2
  - "''-1'은 뒤에서부터 첫 번째 자리이다."

```python
>>> a = "Life is too short, You need Python"
>>> a[0]
'L'
>>> a[12]
's'
>>> a[-1]
'n'
```

- 문자열 슬라이싱

```python
>>> a = "Life is too short, You need Python"
>>> a[0:4]
'Life'
>>> a[19:] # 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.
'You need Python'
>>> a[:17] # 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.
'Life is too short' 
```

- 문자열 나누기

```python
>>> a = "Life is too short"
>>> a.split() #공백을 기준으로 나누어준다.
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':') #괄호 안에 들어간 값을 기준으로 나누어준다.
['a', 'b', 'c', 'd']
```

## 3. 리스트 자료형

- 여러가지 리스트의 형태
  - 비어 있는 리스트는 a = list()로 생성할 수도 있다.

```python
>>> a = []
>>> b = [1, 2, 3]
>>> c = ['Life', 'is', 'too', 'short']
>>> d = [1, 2, 'Life', 'is']
>>> e = [1, 2, ['Life', 'is']]
```

- 리스트 인덱싱

```python
>>> a = [1, 2, 3, ['a', 'b', 'c']]
>>> a[0]
1
>>> a[-1]
['a', 'b', 'c']
>>> a[3]
['a', 'b', 'c']
```

- 리스트 슬라이싱 (문자열과 동일하다.)

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = a[:2]
>>> c = a[2:]
>>> b
[1, 2]
>>> c
[3, 4, 5]
```

- 리스트 길이 구하기

```python
>>> a = [1, 2, 3]
>>> len(a)
3
```

- 리스트 값 수정, 삭제하기

```python
>>> a = [1, 2, 3]
>>> a[2] = 4
>>> a
[1, 2, 4]

>>> a = [1, 2, 3]
>>> del a[1]
>>> a
[1, 3]
```

- 리스트에 요소 추가


```python
>>> a = [1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
```

- 리스트 정렬


```python
>>> a = [1, 4, 3, 2]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a = ['a', 'c', 'b']
>>> a.sort()
>>> a
['a', 'b', 'c']
```

- 리스트 뒤집기


```python
>>> a = ['a', 'c', 'b']
>>> a.reverse()
>>> a
['b', 'c', 'a']
```

- 위치 반환


```python
>>> a = [1,2,3]
>>> a.index(3)
2
>>> a.index(1)
0
```

- 리스트 요소 삽입


```python
>>> a = [1, 2, 3]
>>> a.insert(0, 4) #0번째 위치에 4를 삽입
>>> a
[4, 1, 2, 3]
```

- 리스트 요소 제거


```python
>>> a = [1, 2, 3, 1, 2, 3]
>>> a.remove(3) #리스트에서 첫 번째로 나오는 3을 제거
>>> a
[1, 2, 1, 2, 3]
```

- 리스트 요소 꺼내기


```python
>>> a = [1,2,3]
>>> a.pop() #마지막 요소를 돌려주고 삭제
3
>>> a
[1, 2]

>>> a = [1,2,3]
>>> a.pop(1) #x번째 요소를 돌려주고 삭제
2
>>> a
[1, 3]
```

- 리스트에 포함된 요소 x의 개수 세기


```python
>>> a = [1,2,3,1]
>>> a.count(1)
2
```

- 리스트 확장


```python
>>> a = [1,2,3]
>>> a.extend([4,5]) #x에는 리스트만 올 수 있다.
>>> a
[1, 2, 3, 4, 5]
>>> b = [6, 7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]
```

## 4. 튜플 자료형

- 여러가지 튜플의 형태
  - 튜플은 이하의 점을 제외하면 리스트와 거의 같다.
    - 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
    - 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.


```python
>>> t1 = ()
>>> t2 = (1,)
>>> t3 = (1, 2, 3)
>>> t4 = 1, 2, 3
>>> t5 = ('a', 'b', ('ab', 'cd'))
```

## 5. 딕셔너리 자료형

- 딕셔너리 자료형의 형태


```python
>>> dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
```

- 딕셔너리 쌍 추가하기


```python
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}
```

- 딕셔너리 요소 삭제하기


```python
>>> a = {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
```

- 딕셔너리에서 Key 사용해 Value 얻기


```python
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99
```

- Key 리스트 만들기


```python
>>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
```

- dict_keys 객체를 리스트로 변환하기


```python
>>> list(a.keys())
['name', 'phone', 'birth']
```

- Value 리스트 만들기


```python
>>> a.values()
dict_values(['pey', '0119993323', '1118'])
```

- Key, Value 쌍 얻기


```python
>>> a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
```

- Key: Value 쌍 모두 지우기


```python
>>> a.clear()
>>> a
{}
```

- Key로 Value 얻기


```python
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'0119993323'
```

## 6. 집합 자료형 (set)

- 여러가지 집합 자료형의 형태
  - 중복을 허용하지 않는다.
  - 순서가 없다.


```python
>>> s1 = set([1,2,3])
>>> s1
{1, 2, 3}

>>> s2 = set("Hello")
>>> s2
{'e', 'H', 'l', 'o'}
```

- 교집합 구하기

```python
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])
>>> s1 & s2
{4, 5, 6}
```

- 합집합 구하기


```python
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
```

- 차집합 구하기


```python
>>> s1 - s2
{1, 2, 3}
>>> s2 - s1
{8, 9, 7}
```

- 값 1개 추가하기


```python
>>> s1 = set([1, 2, 3])
>>> s1.add(4)
>>> s1
{1, 2, 3, 4}
```

- 값 여러 개 추가하기


```python
>>> s1 = set([1, 2, 3])
>>> s1.update([4, 5, 6])
>>> s1
{1, 2, 3, 4, 5, 6}
```

- 특정 값 제거하기


```python
>>> s1 = set([1, 2, 3])
>>> s1.remove(2)
>>> s1
{1, 3}
```

## 7. 불린형

<img src="Python.assets/Screen Shot 2022-07-12 at 8.32.16 PM.png" alt="Screen Shot 2022-07-12 at 8.32.16 PM" style="zoom: 50%;" />

- 불린형은 참과 거짓으로 구분된다.


```python
>>> bool([1,2,3])
True
>>> bool([])
False
>>> bool(0)
False
>>> bool(3)
True
```
<div markdown="1">
</div>
</details>

<details>
<summary>예외 처리</summary>
<div markdown="1">
# 예외 처리

## 1. 개요

- 예외 처리는 발생한 에러를 해결하는 방법이다.

## 2. try-except

- try: 오류가 발생할 가능성이 있는 코드를 실행한다. 예외가 발생하지 않으면 except 없이 종료한다.
- except: 예외가 발생하면 except 절을 실행한다.

```python
try:
		num = input('숫자입력 :') print(int(num))
except:
		print('숫자가 아닙니다')

try:
		num = input('숫자입력 :') print(int(num))
except ValueError: 
  	print('숫자가 아닙니다')
```
- 복수의 예외 처리도 가능하다.

```python
try:
		num = input('100으로 나눌 값을 입력하시오: ') 
    100/int(num)
except (ValueError, ZeroDivisionError): 
  	print('제대로 입력해줘')

try:
		num = input('값을 입력하시오: ') 
    100/int(num)
except ValueError: 
  	print('숫자를 넣어주세요.')
except ZeroDivisionError: 
  	print('0으로 나눌 수 없습니다.')
except:
		print('에러는 모르지만 에러가 발생하였습니다.')
```
## 3. 예외 발생시키기

- raise를 통해 예외를 강제로 발생시킬 수 있다.

```python
raise <표현식>(메시지)
```
</div>
</details>

<details>
<summary>OOP</summary>
<div markdown="1">
# OOP

## 1. 개요

- OOP는 객체 지향 프로그래밍(*Object-Oriented Programming*)이다.

## 2. 기본 문법

- 클래스는 틀, 인스턴스는 사례이다. 클래스 = 사람, 인스턴스 = 아이유.
- 속성은 값, 메소드는 함수이다.

```python
# 클래스 정의 
class MyClass:
		pass
# 인스턴스 생성 
my_instance = MyClass() 
# 메서드 호출 
my_instance.my_method() 
# 속성 
my_instance.my_attribute
```
## 3. 인스턴스

- 인스턴스 변수: 인스턴스가 개인적으로 가지고 있는 속성이다. `self.<name>`으로 정의한다. 생성된 이후에는 `<instance>.<name>`으로 접근한다.

```python
class Person:
  
  def __init__(self, name):
    	self.name = name
      # 인스턴스 변수 정의
 
john = Person('john')
# 인스턴스 생성

print(john.name)
# john
# 인스턴스 변수 접근

john.name = 'John Kim'
# 인스턴스 변수 할당
print(john.name)
# John Kim
```
- 인스턴스 메소드: 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드이다. 호출 시, 첫 번째 인자로 인스턴스 자기자신(self)이 전달된다.

```python
class MyClass:

  	def instance_method(self, arg1, ...):
```
- 생성자 메소드: 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드이다.

```python
class Person:

  	def __init__(self):
      print('인스턴스가 생성되었습니다.')

person1 = Person()
# 인스턴스가 생성되었습니다.

class Person:

  	def __init__(self, name):
      print(f'인스턴스가 생성되었습니다. {name}')

person1 = Person('지민')
# 인스턴스가 생성되었습니다. 지민
```
- 소멸자 메소드: 인스턴스 객체가 소멸되기 직전에 호출되는 메소드이다.

```python
class Person:

  	def __del__(self):
      print('인스턴스가 사라졌습니다.')

person1 = Person()
# 인스턴스가 사라졌습니다.
```
## 4. 클래스

- 클래스 속성: 한 클래스 안의 모든 인스턴스가 똑같은 값을 가진 속성이다. `<classname>.<name>`으로 접근 및 할당한다.

```python
class Circle:
  	pi = 3.14

c1 = Circle()
c2 = Circle()

print(Circle.pi)
# 3.14
print(C1.pi)
# 3.14
print(C2.pi)
# 3.14
```
- 클래스 메소드: 클래스가 사용하는 메소드이다. 호출 시, 첫 번째 인자로 클래스(cls)가 전달된다.

```python
 class MyClass:
    
    @classmethod
    def class_method(cls, arg1, ...):
 
MyClass.class_method(...)
```
- 스태틱 메소드: 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드이다. 속성을 다루지 않고 단지 기능만을 하는 메소드를 정의할 때 사용한다.

```python
 class MyClass:
    
    @staticmethod
    def class_method(arg1, ...):
      
MyClass.static_method(...)
```

- 클래스 메소드 정리

```python
 class MyClass:
    
    def method(self):
    	  return 'instace method', self
    
    @classmethod
    def class_method(cls):
     	  return 'class method', cls
      
    @staticmethod
    def static_method():  
     	  return 'static method'
```

## 5. 객체 지향의 핵심 개념

- 추상화
- 상속
- 다형성
- 캡슐화
</div>
</details>

<details>
<summary>심화</summary>
<div markdown="1">
# 심화

## 1. 추가 문법

- List Comprehension
```python
list_a = [<expression> for <변수> in <iterable>] 
list_b = [<expression> for <변수> in <iterable> if <조건식>]
```
- Dictionary Comprehension

```python
Dic_a = {key: value for <변수> in <iterable>}
Dic_b = {key: value for <변수> in <iterable> if <조건식>}
```
- `lambda [parameter] : 표현식`

```python
numbers = [1, 2, 3]
result = list(map(lambda x: x*2, numbers))
print(result)
# [2, 4, 6]
```
- `filter(function, iterable)`: 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환한다.

```python
def odd(n):
  	return n % 2
numbers = [1, 2, 3]
result = list(filter(odd, numbers))
print(result)
# [1, 3]
```

## 2. 가상 환경

- 터미널에서 실행한다.

```python
# 생성
python -m venv venv

# 실행(mac)
. venv/bin/activate
# 실행 후 경로 위 혹은 왼쪽에 가상환경 이름이 출력된다.

# pip3 install
pip3 install -r requirements.txt 

# 종료
deactivate
```
</div>
</details>