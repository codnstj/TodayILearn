# interpolation 을 통한 형식 문자열
## interpolation 문자열이란?
문자열 앞에 f 를 붙힘으로써 형식화 식안에서 현재 파이썬영역 에서 사용할수 있는 모든 이름을 자유롭게 참조할수 있도록 혀용함으로써 간결함을 제공한다.
```python
key = 'hello'
value = '1.234'
formatted = f'{key} , {value}'
print(formatted)

>>>
hello , 1,234
```
f-문자열을 사용하는 형식화는 C style formatting 문자열에 % 을 사용하는 경우나 str.format 을 사용하는 경우보다 항상 더 짧다.

값을 약간 변경하고 싶을때도 {} 안에서 참조된 값에 식을 이용하면 된다.

파이썬 식을 형식 지정자 옵션에 넣을수도 있다.
```python
places =3 
number = 1.23456
print(f'{number:.{places}f')
>>>
1.235
```
> 문자열을 형식화 해야한다면 되도록이면 f-문자열 을 이용하도록 하자!