# Form

- `<form>`은 데이터를 서버에 제출하기 위해 사용하는 태그이다.

```html
<form action="/my-handling-form-page" method="post">

</form>
```

- `<form>`의 기본 속성
  - action : form을 처리할 서버의 URL(데이터를 보낼 곳)
  - method : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  - enctype : method가 post인 경우 데이터의 유형

- `<input>`은 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공된다.
- `<input>`의 기본 속성
  - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
  - value : form control에 적용되는 값 (이름/값 페어로 전송됨)
  - required, readonly, autofocus, autocomplete, disabled 등
- input label: label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있다.
  - `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킨다.

```html
<label for="agreement">개인정보 수집에 동의합니다.</label> 
<input type="checkbox" name="agreement" id="agreement">
```

- `<label>`, `<input>`, `<textarea>` 예제
  - `<input>`은 자동 닫힘 태그이지만, `<textarea>`는 닫는 태그가 필요하다.

```html
<form action="/my-handling-form-page" method="post">
    <div>
        <label for="name">Name:</label>
        <input type="text" id="name" />
    </div>
    <div>
        <label for="mail">E-mail:</label>
        <input type="email" id="mail" />
    </div>
    <div>
        <label for="msg">Message:</label>
        <textarea id="msg">기본값을 정의하고 싶다면 이곳에 입력한다.</textarea>
    </div>
</form>
```

- `<input>` 유형 - 일반
  -  text: 일반텍스트입력
  - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email: 이메일 형식이 아닌 경우 form 제출 불가
  - number: min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file: accept 속성을 활용하여 파일 타입 지정 가능



- `<input>` 유형 - 항목 중 선택
- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성한다.
- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 한다.
  - checkbox : 다중 선택
  - radio : 단일 선택

```html
<div>
  <p>checkbox</p>
  <input id="html" type="checkbox" name="language" value="html"> <label for="html">HTML</label>
  <input id="python" type="checkbox" name="language" value="python"> <label for="python">파이썬</label>
  <input id="python" type="checkbox" name="language" value="java"> <label for="java">자바</label>
  <hr>
  <p>radio button</p>
  <input id="행복" type="radio" name="language" value="행복"> <label for="행복">행복</label>
  <input id="기쁨" type="radio" name="language" value="기쁨"> <label for="기쁨">기쁨</label>
  <input id="즐거움" type="radio" name="language" value="즐거움"> <label for="즐거움">즐거움</label>
</div>
```



- `<input>` 유형 - 기타
- 다양한 종류의 input을 위한 picker를 제공한다.
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정한다.
  - hidden : 사용자에게 보이지 않는 input
