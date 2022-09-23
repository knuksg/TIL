# CSS 기초

## CSS 기본 구조

- `선택자(selector)`: rule set의 맨 앞에 있는 HTML 요소 이름. 이것은 꾸밀 요소를 선택합니다.
- `선언`: `color: red`와 같은 단일 규칙. 꾸미기 원하는 요소의 속성을 명시합니다.
- `속성(property)`: 주어진 HTML 요소를 꾸밀 수 있는 방법입니다.
- `속성 값`: 속성의 오른쪽에, 콜론 뒤에, 주어진 속성을 위한 많은 가능한 결과중 하나를 선택하기 위해 속성 값을 갖습니다
- 각각의 rule set (셀렉터로 구분) 은 반드시 (`{}`) 로 감싸져야 합니다.
- 각각의 선언 안에, 각 속성을 해당 값과 구분하기 위해 콜론 (`:`)을 사용해야만 합니다.
- 각각의 rule set 안에, 각 선언을 그 다음 선언으로부터 구분하기 위해 세미콜론 (`;`)을 사용해야만 합니다.

```css
/*선택자*/ p /*선언 시작*/{
  /*속성명*/ color: /*속성값*/ red; /*선언 구분자*/
  width: 500px;
  border: 1px solid black;
} /*선언 끝*/
```

- 여러 요소 선택하기

```css
p,li,h1 {
  color: red;
}
```

- 클래스(class) 선택자

```html
<!DOCTYPE html>
<html lang="ko">

<head>
	<meta charset="UTF-8">
	<title>CSS Syntax</title>
	<style>
		.headings {
			color: lime;
			text-decoration: overline;
		}
	</style>
</head>

<body>

	<h1>클래스 선택자를 이용한 선택</h1>
	<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>
	<p>클래스 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>
	<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>

</body>

</html>
```

## 참고 사이트

- https://developer.mozilla.org/ko/docs/Web/CSS/Reference
- http://www.tcpschool.com/css/