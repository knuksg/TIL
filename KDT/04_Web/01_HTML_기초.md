# HTML 기초

## HTML 문서의 기본 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <!--이곳에는 메타 데이터가 들어갑니다.-->
    <meta charset="utf-8">
    <title>타이틀이 들어가는 곳입니다.</title>
  </head>
  <body>
    <!--이곳에는 HTML 문서의 본문이 들어갑니다.-->
    <p>본문이 들어가는 곳입니다.</p>
  </body>
</html>
```

## HTML 요소의 구조

- `여는 태그`: 요소의 이름과 열고 닫는 꺽쇠 괄호로 구성된다. 예: `<p>`
- `닫는 태그`: 여는 태그 앞에 슬래시가 존재한다. 예: `</p>`
- `내용`: 요소의 내용, 단순한 텍스트이다.
- `요소`: 여는 태그, 닫는 태그, 내용을 통틀어 요소라고 한다.

```html
<!--포함된 요소-->
<!--요소 안에 또 다른 요소가 들어갈 수 있다.-->
<p>My cat is <strong>very</strong> grumpy.</p>


<!--블럭 레벨 요소 vs 인라인 요소-->
<!--블럭 레벨 요소는 앞 뒤 요소 사이 새로운 줄을 만든다.-->
<!--인라인 요소는 항상 블럭 레벨 요소 내에 포함되어 있다.-->
<em>first</em><em>second</em><em>third</em>
<!--firstsecondthird-->
<p>fourth</p><p>fifth</p><p>sixth</p>
<!--fourth-->

<!--fifth-->

<!--sixth-->


<!--빈 요소-->
<!--닫는 태그가 없는 요소도 있다.-->
<img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png">
```

## 속성

- 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 되고, 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백이 있어야 한다.
- 속성 이름 다음엔 등호(=)가 붙는다.
- 속성 값은 열고 닫는 따옴표로 감싸야 한다.

```html
<p>A link to my <a href="https://www.mozilla.org/" title="The Mozilla homepage" target="_blank">favorite website</a>.</p>
```

## HTML에 CSS와 JavaScript 적용하기

- `<link>`는 항상 문서의 head 부분에 위치한다. 이것은 두 가지 속성을 취하는데, rel="stylesheet", 즉 문서의 스타일 시트임을 나타냄과 동시에 스타일 시트 파일의 경로를 포함하는 href를 내포한다.

```html
<link rel="stylesheet" href="my-css-file.css">
```

- `<script>` 는 head에 들어갈 필요가 없다. `</body>` 태그 바로 앞, 문서 본문의 맨 끝에 넣는 것이 좋으며, JavaScript를 적용하기 전에 모든 HTML 내용을 브라우저에서 읽었는지 확인하는 것이 좋다. 액세스 과정에서 JavaScript가 아직 존재하지 않는 요소라고 판단하며 에러가 날 수 있다.

```html
<script src="my-js-file.js"></script>
```