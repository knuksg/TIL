# JSON으로 작업하기

JavaScript Object Notation (JSON)은 Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷입니다. 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용합니다(서버에서 클라이언트로 데이터를 전송하여 표현하려거나 반대의 경우). 여기저기서 자주 보았을테니 여기선 JSON을 파싱, 데이터에 접근하고 JSON을 생성하는 등 Javascript로 JSON을 다루는 법에 대해 알아봅시다.

### [JSON 구조](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON#json_구조)

위에서 설명했듯이 JSON은 Javascript 객체 리터럴 문법을 따르는 문자열입니다. JSON 안에는 마찬가지로 Javascript의 기본 데이터 타입인 문자열, 숫자, 배열, 불리언 그리고 다른 객체를 포함할 수 있습니다. 이런 방식으로 여러분은 데이터 계층을 구축할 수 있습니다, 아래 처럼요.

```
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```

이 객체를 Javascript 프로그램에서 로드하고, 예를 들어 `superHeroes`라는 이름의 변수에 파싱하면 [JavaScript object basics](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/Basics) 문서에서 보았던 것처럼 점/브라켓 표현법을 통해 객체 내 데이터에 접근할 수 있게 됩니다. 아래와 같이요:

```
superHeroes.homeTown
superHeroes['active']
```

하위 계층의 데이터에 접근하려면, 간단하게 프로퍼티 이름과 배열 인덱스의 체인을 통해 접근하면 됩니다. 예를 들어 superHeroes의 두 번째 member의 세 번째 power에 접근하려면 아래와 같이 하면 됩니다.

```
superHeroes['members'][1]['powers'][2]
```

1. 우선 변수 이름은 — `superHeroes`입니다.
2. `members` 프로퍼티에 접근하려면, `["members"]`를 입력합니다.
3. `members`는 객체로 구성된 배열입니다. 두 번째 객체에 접근할 것이므로 `[1]`를 입력합니다.
4. 이 객체에서 `powers` 프로퍼티에 접근하려면 `["powers"]`를 입력합니다.
5. `powers` 프로퍼티 안에는 위에서 선택한 hero의 superpower들이 있습니다. 세 번째 것을 선택해야 하므로 `[2]`.

### [Other notes](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON#other_notes)

- JSON은 순수히 데이터 포맷입니다. 오직 프로퍼티만 담을 수 있습니다. 메서드는 담을 수 없습니다.
- JSON은 문자열과 프로퍼티의 이름 작성시 큰 따옴표만을 사용해야 합니다. 작은 따옴표는 사용불가합니다.
- 콤마나 콜론을 잘못 배치하는 사소한 실수로 인해 JSON파일이 잘못되어 작동하지 않을 수 있습니다. [JSONLint](http://jsonlint.com/)같은 어플리케이션을 사용해 JSON 유효성 검사를 할 수 있습니다.
- JSON은 JSON내부에 포함할 수 있는 모든 형태의 데이터 타입을 취할 수 있습니다. 즉, 배열이나 오브젝트 외에도 단일 문자열이나 숫자또한 유효한 JSON 오브젝트가 됩니다.
- 자바스크립트에서 오브젝트 프로퍼티가 따옴표로 묶이지 않을 수도 있는 것과는 달리, JSON에서는 따옴표로 묶인 문자열만이 프로퍼티로 사용될 수 있습니다.
