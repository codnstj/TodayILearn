# Closure

Scope : 변수에 접근할수 있는 범위

Lexical Scope : 함수 내부에서 외부의 위치하는 변수는 접근하는것

ex_1

```js
function foo(){
	var x = ‘hello’
	console.log(x) //hello
}
console.log(x) // reference error
```

ex_2

```js
var x = 1;
if (true) {
  var x = 2;
}
console.log(x); //2
```

Block : 중괄호 로 둘러 싸인 부분
Var 는 Block Scoping 의 대상이 아니다. Var 는 Block 을 무시한다.

( 그러나 let 과 const 는 Block Scoping 대상이다)

Closure : 함수 + 환경

- 함수가 하나 생길때 마다 하나씩 생긴다.
- 환경은 함수 자신을 둘러싼 , 접근할수 있는 모든 스코프 들을 뜻한

Ex1)

```js
Function and(x){
	return function print(y){
		return x + ‘and’ + y
	}
}
Const saltAnd = and(‘salt’);
saltAnd(’peper’) // salt and peper
saltAnd(‘sugar’) // salt and. sugar
```

Ex2)

```js
Function and(x){
	return fuction print(y){
		return x + ‘and’ + y
	}
}
Const salstAnd = and(‘salt’);
saltAnd(‘pepper’) // salt and peper
saltAnd(‘sugar’) // salt and sugar

Const waterAnd = and(‘water’);
waterAnd(‘juice’) // water and juice
```

SalterAnd 와 waterAnd 모두 함수는 같은 print 이지만 , 각각 주어진 변수가 다릅니다.
saltAnd 는 “salt”, waterAnd 는 “water” 로 바인딩 되어있습니다.
즉, 둘은 서로 다른 closure 를 형성 하고 있습니다.

Ex3) 이 상황에서 만들어진 closure 는 몇개?

```js

Function foo(){
	function bar(){
	}
	function baz(){
	}
}
foo()
foo()
```

bar baz 는 처음 foo 함수가 호출 될때 만들어진 함수처럼 생각되지만 bar baz 는 각각 새로 생성 된다. 그러므로 총 5개
ex4)

```js
function getCounter() {
  var result = {
    count: count,
    total: 0,
  };
  function count() {
    result.total += 1;
  }
  return result;
}

var counter = getCounter();
counter.count();
counter.count();
console.log(counter.total);
```

counter.count 함수가 호출 될때마다 total 이 증가하여 콘솔에 표시되는 수는 2이다.
ex5)

```js
function getCounter() {
  tempcount += 1;
  var result = {
    count: count,
    total: 0,
  };
  function count() {
    result.total += 1;
  }
  return result;
}

var counter1 = getCounter();
counter.count();
counter.count();
var counter2 = getCounter();
counter.count();
console.log(counter1.total, counter2.total, getCounter.tempcount);
```

getCounter 함수가 호출된 횟수는 2회
counter1.count 가 호출된 횟수는 2회
counter2.count 가 호출된 횟수는 1회
이므로 출력되는 수는 2,1,2 이다.
