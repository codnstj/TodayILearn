# 복잡한 식을 쓰는 대신에 도우미 함수를 작성하라
예를 들어 URL 의 Query String  을 구문 분하고 싶다고 하자. 여기서 각 Qurey String 은 정수 값을 포현한다.
```python
from urllib.parse import parse_qs

my_value = parse_qs('빨강=5&파랑=0&초록=',keep_blank_values=True)
print(repr(my_values))

>>>
{'빨강':['5'],'파랑':['0'],'초록':['']}
```

이를 get 함수로 받게된다면 값이 없는 경우 는 none 으로 반환 되어 나타나게 되고
만약 값은 있지만 값의 상태가 null 이라면 [' '] 으로 나타나게 된다.

파라미터 가 없거나 비어있을경우 0이 디폴트 값으로 대입되면 좋을것 같서 이 로직을 처리하기 위해 완전한 if 문 을 쓰는것 보다 if 식을 사용 하는것이 좋을것이다.

```python
red = my_values.get('RED',[''])[0] or 0
green = my_values.get('GREEN',[''])[0] or 0
opacity = my_values.get('투명도',[''])[0] or 0

print(f'{red!r}')
print(f'{green!r}')
print(f'{opacity!r}')

>>>
빨강 : 5
초록 : 0
투명도 : 0 
```

if 식을 사용했을때 get 함수가 작동하게 된다. get 함수가 키의 해당하는 값이 list 에 유일한 값으로 존재하게 된다면 true 로 반환 되고 list 의 있는 값을 변수에 받게 된다.


여기서 만약 list 에 빈문자열이 유일한 원소로 들어있게 된다면 이는 암묵적으로  False 로 평가되고 0이 반환되게 된다.

또한 딕셔너리 키에 해당하는 값이 없다면 , get 메서드는 딕혀너리 안에 키가 없을때 두번째 인자를 반환한다. 딕셔너리에서 해당하는 키르 찾지 못하면 이코드는 빈 문자열 이 유일한 원소로 있는 경우와 같은 동작을 하게 된다.

```python
red = int(my_values.get('hello',[''])[0] or 0)
```
현재 이코드는 익기 너무 어렵고 시각적 잡음 이 너무 많다. 즉 코드를 이해하기 쉽지 않으므로 코드를 새로 읽는 사람이 이 시이 실제로 어떤 일을 하는지 이해하기 위해 너무 많은 시간을 투자하게 된다. 

파이썬 에서 코드를 간결하게 유지 하면서 이를 명확하게 표현할수 있는  if/else 식이 잇다.

```python
hello_str = my_values.get('hello',[''])
red = int(red_str[0]) if red_str[0] else 0
```
이코드 가 훨 보기 편하나 , if/else 문을 여러줄ㅇ 쓰는 경우보다는 덜 명확하다. 

```python
hello_ster = my_values.get('hello',[''])
if hello_str[0]:
    hello = int(hello_str[0])
else:
    hello = 0
```
하지만 이 로직을 반복 적용 하게 된다면 꼭 Helper Function 을 이용해야한다.(2~3 회 반복 할지라도.)

```python
def = get_first_int(values,key,default=0):
    found = values.get(key,[''])
    if found[0]:
        return int(found[0])
    return default
```

***아무리 코드를 짧게 쓰는것을 좋아 할지라도 가독성을 해칠만큼 코드를 짧게 줄여쓰는것은 좋지 않다 오히려 조금 길이가 늘어난다해도 코드의 가독성을 좋게 하는것이 더 가치있다.***