# 매개변수 

 ### 위치 매개변수
- 가장 기본적인 매개변수이다.
- 함수를 호출할떄 순서대로 데이터(인자)를 넘겨줘야 한다.
- 다른 매개 변수와 함께 쓸떄는 ***항상 맨앞*** 에 써야한다.
```python
def myfunc(a,b):
	print(a,b)
. . .
myfunc(1,2)
```
	
 ### 기본 매개변수
- 매개변수의 기본적인 값
- 함수를 정의할 때 매개변수의 기본 값을 지정할수 있다.
```python
Def post_info(title , content=‘no content’):
	print(title)
	print(content)
. . . 

>>> post_info(‘title1’)
title1
no content
```

### 키워드 매개변수
- 함수호출 시에 키워드를 붙혀 호출한다.
- 매개변수의 순서를 지키지 않아도 됩니다.
```python
def post_info(title , content):
	print(title)
	print(content)
. . . 

>>> post_info(title=‘title1’,content=‘content’)
title1
content
```


