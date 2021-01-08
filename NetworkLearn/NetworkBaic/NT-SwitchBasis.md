# 스위치 기본
- 카타리스트 2960 시리즈
  - POE : 데이터와 전원을 같이 보내는 방식의 스위치
  - SFP : 광케이블용 접속방식
  - C:Dual Purpose Uplink : SFP 포트와 10/100/1000 Base T 포트 중에 한가지만 사용해서 할수 있다.

---

  - 시스템 LED : 시스템이 전원을 제대로 받는지 이상 없이 동작여부를 나타낸다
  
    |제목|시스템 상태|
    |:---:|:---:|
    |꺼짐|전원이 공급되고 있지 않은 꺼진 상태|
    |초록색|시스템 정상적으로 작동 중|
    |주황색(노랑색)|전원은 공급되나 비정상적으로 작동 중|
  - --
  - RPS LED : 문정전 전원을 제대로 받는 지 이상 없이 동작 여부 
  
    |제목|시스템 상태|
    |:---:|:---:|
    |꺼짐|RPS가 꺼져있거나 제대로 연결됭 있지 않다|
    |초록색|RPS 가 연결되어있고 정상작동 중이다.|
    |초록색으로 깜빡임|RPS 가 연결되어 있으나 , 현재  다른 스위치에 전원을 공급중이라 현재 스위치에 전원공급이 불가능하다.|
    |주황색(노랑색)|RPS 가 대기모드에 있거나 고장이다.이때 Standby/Active 버튼을 눌러주면 LED 는 녹색으로 변한다.이떄 녹색으로 바뀌지 않는다면 RPS 고장이다.|
    |주황색으로 깜빡임|스위치의 내부 전원 고장으로 , RPS 로 부터 전원을 공급받아 작동 중이다.|

  - --

  - 포트모드    
    |포트모드LED|포트모드|포트상태,LED 표시|
    |:---:|:---:|:---:|
    |STAT|Port Status|각 포트의 상태를 표시(디폴트)|
    |UTIL|Switch  Utilization|스위치의 백플레인 사용률 표시||
    |DUPLX|Port Duplex Mode|각 포트의 DuPlex 모드 표시(Half)|
    |SPEED|Port Speed|각 포트의 스피드(10/100/1000)표시|
---
  - 포트상태 LED

| Port Mode LED | Port Status LED | Port Status LED Mean |
|---|---:|:---|
| <br>STAT<br>(Port Status) | OFF<br>Green<br>Blink green<br>Blink orange & green<br>Orange(yellow) | 링크 연결이 안됨<br>링크 연결됨 <br>링크가 살아있고 데이터 송수신중<br>링크에러 발생<br>포트 비활성화 or Blocking 상태 |
| <br><br>UTIL<br>(Utilization) | Green<br><br>Orange(yellow)<br><br>Blink Green & Orange | 현재 스위치의 백본 사용률<br><br>스위치가 켜진후 지금까지 최대 백본 사용률 도달<br><br>만약 스위치의 LED가 모두 초록색이고 주황색이 하나도 없으면 사용률이 50%를 넘었다는 뜻이고, 가장 오른쪽 LED 가 꺼져 있으면 스위치 사용률이 20~25% 사이라는 것이고, 가장 왼쪽 LED 하나만 초록색일 경우 스우치는 전체 용량의 0.0488%만을 사용하고 있다는 것이다. |
| DUPLX<br>(Duplx) | OFF<br>Green |  |
|  |  |  |
|  |  |  |