# Table

- `<table></table>` 태그를 사용하여 테이블을 만든다.
- `<thead></thead>`, `<tbody></tbody>`, `<tfoot></tfoot>` 태그를 사용한다.
- 각각의 행은 `<tr></tr>` 태그를 사용한다.
- 상위 태그에 따라서 `<tr></tr>` 태그 안에 `<th></th>`, `<td></td>` 태그를 사용한다.
- 열을 합칠 때는 `colspan`을 사용한다.

```html
<table>
    <thead>
      <th>ID</th>
      <th>Name</th>
      <th>Major</th>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>홍길동</td>
        <td>Computer Science</td>
      </tr>
      <tr>
        <td>2</td>
        <td>김철수</td>
        <td>Business</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td>총계</td>
        <td colspan="2">2명</td>
      </tr>
    </tfoot>
    <caption>1반 학생 명단</caption>
  </table>
```

