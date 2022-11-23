# template와 view에서 자연스러운 시간 사용하기

https://stackoverflow.com/questions/17226779/django-humanize-outside-of-template

in views.py

```py
from django.contrib.humanize.templatetags.humanize import naturalday
natural_day = naturalday(value)
```

in template

```html
{% load humanize %}

{{ value|naturaltime }}
```

in installed_apps

```
"django.contrib.humanize",
```