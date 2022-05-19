# unpacking 을 통한 대입    
파이썬에는 불변의 값으로 순서쌍을 만들어낼수 있는 `tuple` 내장 타입이 있다.
```python
snack_caloriees = {
    'photato':140,
    'popcorn':80,
    'peanuts':190,
}
items = tuple(snack_calories.items())
print(items)

>>>
(('popcorn',140),('photato',80),('peanuts',190))
```

튜플에 있는 값은 숫자 인덱스를 사용해 접근할 수 있다. -> items[0]

튜플이 만들어진다면 인덱스를 통해 새 값을 대입해서 튜플을 변경할 수는 없다.

