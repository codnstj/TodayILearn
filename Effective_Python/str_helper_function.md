# 복잡한 식을 쓰는 대신에 도우미 함수를 작성하라
예를 들어 URL 의 Query String  을 구문 분하고 싶다고 하자. 여기서 각 Qurey String 은 정수 값을 포현한다.
```python
from urllib.parse import parse_qs

my_value = parse_qs('빨강=5&파랑=0&초록=',keep_blank_values=True)
print(repr(my_values))

>>>
{'빨강':['5'],'파랑':['0'],'초록':['']}
```

파라미터 가 없거나 비어있을경우 0이 디폴트 값으로 대입되면 좋을것 같서 이 로직을 처리하기 위해 완전한 if 문 을 쓰는것 보다 if 식을 사용 하는것이 좋을것이다.

```python
red = my_values.get('RED',[''])[0] or 0
green = my_values.get('GREEN',[''])[0] or 0
opacity = my_values.get('투명도',[''])[0] or 0

print(f'{red!r}')
print(f'{green!r}')
print(f'{opacity!r}')
```
 