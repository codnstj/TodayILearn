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
formatted = '{:<10} 앞에서 부터 열칸 ,  {:.2f} = format(value,".2f")'.format(key,value)
print(formatted)

>>>
hello     , 1,23 = format(value,".2f")
```

C 스타일에서 % 를 사용하고 싶으면 -> %%

str.format 에서 {} 를 사용하고 싶으면 -> {{}}

format 메서드 에 전달된 인자의 순서를 정할수 있다.

format 에 넘기는 인자의 값을 바꾸지 않아도 형식화 문자열을 통해 출력 순서를 바꿀수 있다.
```python
formatted  = '{1} = {0}'.format(key,value)
print(formatted)
>>>
1.23 = hello
```
이를 통해 같은 위치의 인덱스를 여러번 사용할수 도 있다.

>**!** 하지만 이를 str.format 을 사용한다해도 딕셔너리보다 작은 따옴표를 덜 쓰고 형식 지정자를 덜쓰는것 빼고는 코드의 가독성 문제가 완전히 해결되지 않으므로 `interpolation 문자열` 을 사용하자.(f-문자열 이라고도 부름)