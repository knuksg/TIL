# CSS 속성

## 기본 속성

### 색

- 색상 이름으로 표현

```css
<style>
    .blue { color: blue; }
    .green { color: green; }
    .silver { color: silver; }
</style>
```

- RGB 색상값으로 표현

```css
<style>
    .blue { color: rgb(0,0,255); }
    .green { color: rgb(0,128,0); }
    .silver { color: rgb(192,192,192); }
</style>
```

- 16진수 색상값으로 표현

```css
<style>
    .blue { color: #0000FF; }
    .green { color: #008000; }
    .silver { color: #C0C0C0; }
</style>
```

### 배경

- background-color 속성

```css
<style>
    body { background-color: lightblue; }
    h1 { background-color: rgb(255,128,0); }
    p { background-color: #FFFFCC; }
</style>
```

- background-image 속성

```css
/* HTML 요소 전체에 걸쳐 반복되어 나타난다 */
<style>
    body { background-image: url("/examples/images/img_background_good.png"); }
</style>
```

- background-repeat 속성

```css
/*배경 이미지 수평 반복*/
<style>
    body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-x; }
</style>

/*배경 이미지 수직 반복*/
<style>
    body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-y; }
</style>

/*배경 이미지 반복 X*/
<style>
    body { background-image: url("/examples/images/img_man.png"); background-repeat: no-repeat; }
</style>
```

- background-position 속성

```css
<style>
    body {
        background-image: url("/examples/images/img_man.png");
        background-repeat: no-repeat;
        background-position: top right;
    }
</style>

/* 조합할 수 있는 키워드
1. left top
2. left center
3. left bottom
4. right top
5. right center
6. right bottom
7. center top
8. center center
9. center bottom */

/* 퍼센트나 픽셀을 사용해서 상대 위치 직접 명시 가능 */
<style>
    body {
        background-image: url("/examples/images/img_man.png");
        background-repeat: no-repeat;
        background-position: 100px 200px;
    }
</style>
```

- background-attachment 속성

```css
/* 스크롤해도 이미지의 위치가 변하지 않는다 */
<style>
    body {
        background-image: url("/examples/images/img_man.png");
        background-repeat: no-repeat;
        background-position: left bottom;
        background-attachment: fixed;
    }
</style>
```

- background 속성 한 번에 적용하기

```css
<style>
    body { background: #FFCCCC url("/examples/images/img_man.png") no-repeat left bottom fixed; }
</style>
```

- 16진수 색상값으로 표현

```css
<style>
    .blue { color: #0000FF; }
    .green { color: #008000; }
    .silver { color: #C0C0C0; }
</style>
```

## 참고 사이트

- http://www.tcpschool.com/css/