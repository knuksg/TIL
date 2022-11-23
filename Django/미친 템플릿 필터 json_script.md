# 미친 템플릿 필터 json_script

```
{{ profile_dict | json_script:"dict-id"}}   # 파이썬 객체를 템플릿 필터로 가져옴.
=>

# 스크립트 태그로 감싼 형태로 나타나게 됨.
<script id="dict-id" type="application/json">{"name1": "\uac15\ubbfc\uc131", "name2": "\ud64d\uae38\ub3d9"}</script>

# js에서 선택해서 텍스트 콘텐트로 받아오면 원래 형태대로 가져올 수 있음.
var profile = document.getElementById("dict-id").textContent;
=>
// {"name1": "\uac15\ubbfc\uc131", "name2": "\ud64d\uae38\ub3d9"}

# josn 파싱해주면 끝.
var profileJson = JSON.parse(profile);
=>
profileJson['name1'] // 강민성
```