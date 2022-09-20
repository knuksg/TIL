# Array

## 설명

배열은 리스트와 비슷한 객체로서 순회와 변형 작업을 수행하는 메서드를 갖습니다. JavaScript 배열은 길이도, 각 요소의 자료형도 고정되어 있지 않습니다. 배열의 길이가 언제든지 늘어나거나 줄어들 수 있고 데이터를 연속적이지 않은 곳에 저장할 수 있으므로, JavaScript 배열은 밀집성을 보장하지 않습니다. 보통 이런 성질들은 편리하지만, 사용하려는 목적에 맞지 않으면 형식화 배열(typed array)을 사용하는 것을 고려해보세요.

배열은 ([연관 배열](https://ko.wikipedia.org/wiki/연관_배열)과 달리) 요소 인덱스로 문자열을 사용할 수 없으며 무조건 정수만 허용합니다. [대괄호 구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Working_with_Objects#객체와_속성) 또는 [속성 접근자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Property_Accessors)를 사용해 정수가 아닌 키에 접근할 경우 배열의 요소가 아니라 배열의 [객체 속성 컬렉션](https://developer.mozilla.org/ko/docs/Web/JavaScript/Data_structures#속성)에 연결된 변수를 바라보게 됩니다. [순회 및 변형 작업](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Indexed_collections#배열_객체의_메서드) 또한 이런 속성에 적용할 수 없습니다.

### 자주 사용하는 연산

**배열 만들기**

```
let fruits = ['사과', '바나나']

console.log(fruits.length)
// 2
```

**인덱스로 배열의 항목에 접근하기**

```
let first = fruits[0]
// 사과

let last = fruits[fruits.length - 1]
// 바나나
```

**배열의 항목들을 순환하며 처리하기**

```
fruits.forEach(function (item, index, array) {
  console.log(item, index)
})
// 사과 0
// 바나나 1
```

**배열 끝에 항목 추가하기**

```
let newLength = fruits.push('오렌지')
// ["사과", "바나나", "오렌지"]
```

**배열 끝에서부터 항목 제거하기**

```
let last = fruits.pop() // 끝에있던 '오렌지'를 제거
// ["사과", "바나나"]
```

**배열 앞에서부터 항목 제거하기**

```
let first = fruits.shift() // 제일 앞의 '사과'를 제거
// ["바나나"]
```

**배열 앞에 항목 추가하기**

```
let newLength = fruits.unshift('딸기') // 앞에 추가
// ["딸기", "바나나"]
```

**배열 안 항목의 인덱스 찾기**

```
fruits.push('망고')
// ["딸기", "바나나", "망고"]

let pos = fruits.indexOf("바나나")
// 1
```

**인덱스 위치에 있는 항목 제거하기**

```
let removedItem = fruits.splice(pos, 1) // 항목을 제거하는 방법

// ["딸기", "망고"]
```

**인덱스 위치에서부터 여러개의 항목 제거하기**

```
let vegetables = ['양배추', '순무', '무', '당근']
console.log(vegetables)
// ["양배추", "순무", "무", "당근"]

let pos = 1
let n = 2

let removedItems = vegetables.splice(pos, n)
// 배열에서 항목을 제거하는 방법
// pos 인덱스부터 n개의 항목을 제거함

console.log(vegetables)
// ["양배추", "당근"] (원 배열 vegetables의 값이 변함)

console.log(removedItems)
// ["순무", "무"]
```

**배열 복사하기**

```
let shallowCopySpread = [...fruits]
// ["딸기", "망고"]
```

위 코드는 [전개 구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Spread_syntax)을 사용해 배열의 얕은 복사를 만드는 방법입니다. 배열을 복사하는 다른 방법은 아래의 [배열 복사하기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array#배열_복사하기)에서 논의합니다.

### 배열 요소에 접근하기

JavaScript 배열의 인덱스는 0부터 시작합니다. 즉, 배열 첫 번째 요소의 인덱스는 0이고, 마지막 요소의 인덱스는 배열의 [`length`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/length) 속성에서 1을 뺀 것과 같습니다.

잘못된 인덱스를 사용하면 `undefined`를 반환합니다.

```
let arr = ['첫 번재 요소입니다', '두 번째 요소입니다', '마지막 요소입니다']
console.log(arr[0])              // '첫 번재 요소입니다'를 기록
console.log(arr[1])              // '두 번재 요소입니다'를 기록
console.log(arr[arr.length - 1]) // '마지막 요소입니다'를 기록
```

`toString`이 속성인 것과 마찬가지로 (정확히 하자면, `toString()`은 메서드입니다) 배열의 요소도 속성입니다. 하지만 배열 요소에 아래 코드처럼 접근하려고 하면, 속성 이름이 유효하지 않기 때문에 구문 오류가 발생합니다.

```
console.log(arr.0) // 구문 오류
```

이 현상은 JavaScript 배열과 그 속성에 어떤 특별한 점이 있어서 그런 것이 아닙니다. 모든 JavaScript 속성은 이름이 숫자로 시작할 경우 마침표 표기법으로 접근할 수 없고, 대괄호 표기법을 사용해야 합니다.

### 배열 길이와 숫자형 속성의 관계

JavaScript 배열의 [`length`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/length) 속성과 숫자형 속성은 연결되어 있습니다.

몇몇 배열 내장 메서드([`join`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/join), [`slice`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/slice), [`indexOf`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf) 등)은 호출했을 때 배열의 [`length`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/length) 속성의 값을 참고합니다.

다른 메서드([`push`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/push), [`splice`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/splice) 등) 또한 배열의 [`length`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/length) 속성을 바꾸는 결과를 낳습니다.

```
const fruits = []
fruits.push('바나나', '사과', '복숭아')

console.log(fruits.length) // 3
```

배열 인덱스로 유효한 속성을 JavaScript 배열에 설정할 때, 그 인덱스가 현재 배열의 경계 바깥에 있는 경우, JavaScript 엔진은 배열의 [`length`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/length) 속성을 그에 맞춰 업데이트 합니다.

```
fruits[5] = 'mango'
console.log(fruits[5])           // '망고'
console.log(Object.keys(fruits)) // ['0', '1', '2', '5']
console.log(fruits.length)       // 6
```

[`length`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/length)를 직접 늘려도 요소에 변화는 없습니다.

```
fruits.length = 10
console.log(fruits)              // ['바나나', '사과', '복숭아', 비어 있음 x 2, '망고', 비어 있음 x 4]
console.log(Object.keys(fruits)) // ['0', '1', '2', '5']
console.log(fruits.length)       // 10
console.log(fruits[8])           // undefined
```

하지만, [`length`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/length) 속성을 감소시키면 요소가 지워집니다.

```
fruits.length = 2
console.log(Object.keys(fruits)) // ['0', '1']
console.log(fruits.length)       // 2
```

### 배열 복사하기

배열을 새로운 변수에 할당해도 배열이 복사되지는 않습니다. 새로운 변수에는 원본 배열을 가리키는 참조만 할당되며, 원본 배열의 값을 바꾸면 새 변수에서도 그 변경점이 반영됩니다.

```
let array1 = [1,2,3]
let array1Reference = array1;
array1[1] = 9;
console.log(array1Reference);
// Array [1,9,3] - array1의 변화가 array1Reference에도 나타남 - 복사본이 아님
```

배열의 복사본을 만들기 위해서는 새 배열을 위한 변수를 생성하고, 원본 배열 각각의 원시 요소에 대해서도 새로운 변수를 생성해야 합니다. (변수를 원시 값으로 초기화하면 참조를 할당하지 않고 값을 복사합니다.) JavaScript에서는 이를 위해 다음과 같은 방법을 사용할 수 있습니다.

[전개 구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Spread_syntax):

```
let shallowCopySpread = [...fruits]
// ["Strawberry", "Mango"]
```

[`Array.slice()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/slice):

```
let shallowCopySlice = fruits.slice()
// ["Strawberry", "Mango"]
```

[`Array.from()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from):

```
let shallowCopyFrom = Array.from(fruits)
// ["Strawberry", "Mango"]
```

위의 세 코드는 모두 '얕은 복사'를 생성합니다. 얕은 복사란 배열의 최상위 요소가 원시 값일 경우 복사하지만, 중첩 배열이나 객체 요소일 경우에는 원본 배열의 요소를 참조하게 됩니다.

모든 요소의 '깊은 복사', 즉 중첩 배열과 객체 요소 또한 동일한 형태로 복사하는 방법 중 하나는 [`JSON.stringify()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)를 사용해 배열을 JSON 문자열로 변환한 후, [`JSON.parse()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)로 다시 배열을 구성하는 것입니다.

```
let deepCopy = JSON.parse(JSON.stringify(fruits));
// ["Strawberry", "Mango"]
```

# Array.prototype.map()

**`map()`** 메서드는 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환합니다.

## [구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map#구문)

```
    arr.map(callback(currentValue[, index[, array]])[, thisArg])
```

Copy to Clipboard

### [매개변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map#매개변수)

- `callback`

  새로운 배열 요소를 생성하는 함수. 다음 세 가지 인수를 가집니다.`currentValue`처리할 현재 요소.`index` Optional처리할 현재 요소의 인덱스.`array` Optional`map()`을 호출한 배열.

- `thisArg` Optional

  `callback`을 실행할 때 `this`로 사용되는 값.

### [반환 값](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map#반환_값)

배열의 각 요소에 대해 실행한 `callback`의 결과를 모은 새로운 배열.

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map#설명)

`map`은 `callback` 함수를 **각각의 요소에 대해 한번씩** 순서대로 불러 그 함수의 반환값으로 새로운 배열을 만듭니다. `callback` 함수는 ([`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined)도 포함해서) 배열 값이 들어있는 인덱스에 대해서만 호출됩니다. 즉, 값이 삭제되거나 아직 값이 할당/정의되지 않은 인덱스에 대해서는 호출되지 않습니다.

`callback` 함수는 호출될 때 대상 요소의 값, 그 요소의 인덱스, 그리고 `map`을 호출한 원본 배열 3개의 인수를 전달받습니다.

`thisArg` 매개변수가 `map`에 전달된 경우 `callback` 함수의 `this`값으로 사용됩니다. 그 외의 경우 [`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined)값이 `this` 값으로 사용됩니다. `callback` 함수에서 최종적으로 볼 수 있는 `this` 값은 [함수 내 `this`를 정하는 일반적인 규칙](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this)에 따라 결정됩니다.

`map`은 호출한 배열의 값을 변형하지 않습니다. 단, `callback` 함수에 의해서 변형될 수는 있습니다.

`map`이 처리할 요소의 범위는 첫 `callback`을 호출하기 전에 정해집니다. `map`이 시작한 이후 배열에 추가되는 요소들은 `callback`을 호출하지 않습니다. 배열에 존재하는 요소들의 값이 바뀐 경우 `map`이 방문하는 시점의 값이 `callback`에 전달됩니다. `map`이 시작되고, 방문하기 전에 삭제된 요소들은 방문하지 않습니다.

명세서에 정의된 알고리즘으로 인해 `map`을 호출한 배열의 중간이 비어있는 경우, 결과 배열 또한 동일한 인덱스를 빈 값으로 유지합니다.

# Array.prototype.forEach()

**`forEach()`** 메서드는 주어진 함수를 배열 요소 각각에 대해 실행합니다.

## [구문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#구문)

```
    arr.forEach(callback(currentvalue[, index[, array]])[, thisArg])
```

### [매개변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#매개변수)

- `callback`

  각 요소에 대해 실행할 함수. 다음 세 가지 매개변수를 받습니다.`currentValue`처리할 현재 요소.`index`처리할 현재 요소의 인덱스.<`array``forEach()`를 호출한 배열.

- `thisArg`

  `callback`을 실행할 때 `this`로 사용할 값.

### [반환 값](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#반환_값)

[`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined).

## [설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#설명)

`forEach()`는 주어진 `callback`을 배열에 있는 각 요소에 대해 오름차순으로 한 번씩 실행합니다. 삭제했거나 초기화하지 않은 인덱스 속성에 대해서는 실행하지 않습니다. (예: 희소 배열)

`callback`은 다음 세 인수와 함께 호출됩니다.

- **요소 값**
- **요소 인덱스**
- **순회 중인 배열**

`thisArg` 매개변수를 `forEach()`에 제공한 경우 `callback`을 호출할 때 전달해 `this`의 값으로 쓰입니다. 전달하지 않으면 `undefined`를 사용하며, 최종 `this` 값은 [함수의 `this`를 결정하는 평소 규칙](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this)을 따릅니다.

`forEach()`로 처리할 요소의 범위는 최초 `callback` 호출 전에 설정됩니다. `forEach()` 호출을 시작한 뒤 배열에 추가한 요소는 `callback`이 방문하지 않습니다. 배열의 기존 요소값이 바뀐 경우, `callback`에 전달하는 값은 `forEach()`가 요소를 방문한 시점의 값을 사용합니다. 방문하기 전에 삭제한 요소는 방문하지 않습니다.

`forEach()`는 각 배열 요소에 대해 한 번씩 `callback` 함수를 실행합니다. [`map()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map)과 [`reduce()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)와는 달리 [`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined)를 반환하기 때문에 메서드 체인의 중간에 사용할 수 없습니다. 대표적인 사용처는 메서드 체인 끝에서 부작용(side effect)을 실행하는 겁니다.

`forEach()`는 배열을 변형하지 않습니다. 그러나 `callback`이 변형할 수는 있습니다.
