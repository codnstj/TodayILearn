# 내장함수 format 과 str.format
파이썬 3 부터는 C Style Formatting 보다 표현력이 좋은 `고급 문자열 형식화` 기능이 도입됬다. 이 기능은 모든 파이썬값에 format 내장 함수를 통해 사용 가능하다.
```python
a = 1234.5678
a_formatted = format(a,',.2f') # 천단위 구분 을 , 로 사용한다.

b = 'hello'
b_formatted = format(b,'^20s') # ^ 는 중앙의 값을 표시한다.

print(a_formatted)
print('*',b_formatted,'*')

>>>
1,234.57 
*        hello        *
```

str 타입에 추가된 format 메소드를 호출 하면 여러값에 대해 한꺼번에이 기능을 적용할 수 있다. %d 같은 C style 형식 지정자 를 사용 하는 대신 위치 지정자 {} 를 사용 할수 있다. 기본적으로 형식화 문자열의 위치 지정자는 format 메소드에 전달된 인자중 순서상 같은 위치에 있는 인자를 가리킨다.
```python
key = 'hello'
value = '1.234'

formatted = '{} = {}'.format(key,value)
print(formatted)

>>>
hello = 1.234
```

각 위치의 지정자에는 콜론 뒤에 형식 지정자를 붙여 넣어 문자열에 값을 넣을 때 어떤 형식으로 변환할지 정할수 있다.(모든 형식 지정자에 대한 정보를 보고 싶으면 help('FORMATTING') 참고)

```python
formatted = '{:<10} = {:.2f}'.format(key,value)
print(formatted)

>>>
hello   =1.23
```