# CSS 위치&정렬

## 디스플레이

- block: 한 라인을 모두 차지한다.

```css
<div>, <h1>, <p>, <ul>, <ol>, <form>요소는 대표적인 블록(block) 요소입니다.
```
- inline: 해당 HTML 요소의 내용만큼 너비를 차지한다. 새로운 라인에서 시작하지 않는다.

```css
<span>, <a>, <img>요소는 대표적인 인라인(inline) 요소입니다.
```

## 포지션

- static (정적): 기본적인 방식이다.

```css
<style>
    div { position: static; }
</style>
```

- relative (상대): 기본 위치의 공간을 보이지 않게 차지하고, 다른 공간에 있는 것처럼 나타난다.

```css
<style>
    div.relative { position: relative; left: 30px; }
</style>
```

- absolute(절대): static 속성이 아닌 부모 위치를 기준으로 나타난다. 없을 경우, HTML 문서의 body 요소를 기준으로 나타난다. 주로 다른 요소 위에 있어야 하는 요소의 위치를 정할 때 쓴다.

```css
<style>
    div.absolute { position: absolute; top: 50px; right: 0; }
</style>
```

- fixed(고정): 뷰포트를 기준으로 위치를 설정한다. 주로 '위로' 버튼 등에 쓰인다.

```css
<style>
    div.fixed { position: fixed; top: 0; right: 0; }
</style>
```

- sticky: 주로 '상단바' 등에 쓰인다. 기본적으로 static이지만 스크롤하면 fixed로 변한다.

```css
<style>
    div.fixed { position: sticky; top: 0; right: 0; }
</style>
```

## 정렬

- flex container: 정렬할 요소가 담긴 부모 요소에 `flex`를 적용한다.

```css
.container {
  display: flex;
}
```

- flex-direction: 정렬할 방향을 결정한다. 

```css
/*row 정렬*/
.container {
  display: flex;
  flex-direction: row;
}

/*row-reverse 정렬*/
.container {
  display: flex;
  flex-direction: row-reverse;
}

/*column 정렬*/
.container {
  display: flex;
  flex-direction: column;
}

/*column-reverse 정렬*/
.container {
  display: flex;
  flex-direction: column-reverse;
}
```

- justify-content: 요소들을 가로선 상에서 정렬한다.

```css
/*flex-start 정렬*/
.container {
  display: flex;
  justify-content: flex-start(default);
}

/*flex-end 정렬*/
.container {
  display: flex;
  justify-content: flex-end;
}

/*center 정렬*/
.container {
  display: flex;
  justify-content: center;
}

/*space-between 정렬(아이템 사이의 간격을 균일하게 분배한다.)*/
.container {
  display: flex;
  justify-content: space-between;
}
/*space-around 정렬(아이템을 둘러싼 영역을 균일하게 분배한다.)*/
.container {
  display: flex;
  justify-content: space-around;
}
/*space-evenly 정렬(전체 영역에서 아이템 간 간격을 균일하게 분배한다.)*/
.container {
  display: flex;
  justify-content: space-evenly;
}
```

- align-content: 요소들을 세로선 상에서 정렬한다.

```css
/*justify-content와 align-content의 세부 명령어는 동일하다.*/
```

- flex-wrap: 요소들을 컨테이너 영역 내에 배치하도록 설정한다.

```css
/*nowrap 정렬(요소들을 한 줄에 넣는다.)*/
.container {
  display: flex;
  flex-wrap: nowrap(default);
}

/*wrap 정렬(요소들을 여러 줄에 넣는다.)*/
.container {
  display: flex;
  flex-wrap: wrap;
}
```

- flex-flow: flex-direction과 flex-wrap을 합친 기능이다.

```css
.container {
  display: flex;
  flex-flow: row nowrap;
}
```

- align-self: 개별 아이템을 Cross axis 기준으로 정렬한다.

```css
.container {
  display: flex;
  align-self: stretch;
}

.container {
  display: flex;
  align-self: flex-start;
}

.container {
  display: flex;
  align-self: flex-end;
}

.container {
  display: flex;
  align-self: center;
}
```

- flex-grow: 남은 영역을 아이템에 분배한다.

```css
.container {
  display: flex;
}

.box {
  flex-grow: 1;
  border: 3px solid rgba(0,0,0,.2);
}

.box1 {
  flex-grow: 2;
  border: 3px solid rgba(0,0,0,.2);
}
```

- order: 배치 순서를 정한다.

```css
.container {
  display: flex;
}

.box {
  order: 2;
  border: 3px solid rgba(0,0,0,.2);
}

.box1 {
  order: 1;
  border: 3px solid rgba(0,0,0,.2);
}
```

## 참고 사이트

http://www.tcpschool.com/css/css_position_display