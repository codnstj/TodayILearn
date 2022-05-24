# range 보다는 enumrate 를 사용하라 # 1

## range 
range 내장함수는 어떤 정수 집합을 이터레이션하는 루프가 필요할떄 유용하다.
```python
from random import randint

random_bits = 0

for i in range(32):
    if(randint(0,1)):
        random_bits|= 1 << i 

print(bin(random_bits))

>>>
0b10101000010101010011010
```

문자열 로 이뤄진 list 처럼 이터레이션 할 대상 데이터 구조가 있으면 이 시퀀스에대해 바로 루프를 돌 수 있다.


```python
num_list = ['one','two','three']
for num in num_list:
    print(f'{num}')

>>>
one
two
three
```

리스트를 이터레이션 하면서 몇번쨰 원소를 처리하는지 알아야할 떄가 있다. 이떄 range 를 사용하는 방법을 보자.

```python
for i in range(len(num_list)):
    num_index = num_list[i]
    print(f'{i+1} : {num_index}')
    
>>>
1 : one
2 : two
3 : three
```

list 나 range 에 대해 이터레이션을 수행하는 다른 예제와 비교해보면 이 코드는 투박하다고 한다.(난 잘 모르겠는데) List 의 길이를 알아야 하며 인덱스를 사용해 배열 원소에 접근해야한다. 이렇게 단계가 여러개이므로 코드를 읽기 어렵다고한다.

이런문제를 해결하기위해 파이썬은 enumrate 내장함수를 제공한다.

```python
it = enumrate(num_list)
print(next(it))
print(next(it))

>>>
(1,'one')
(2,'two')
```

enumrate 가 넘겨주는 각 쌍을 for 문에서 간결하게 언패킹할수 있다.

```python
for i,num in enumrate(num_list):
    print(f'{i+1} : {num}')

>>>
1 : one
2 : two
3 : three
```

enumrate 의 두번째 파라미터 로 어디서부터 수를 세기 시작할지 지정할수 있다.

```python
jumps = enumrate(num_list,1)
```
