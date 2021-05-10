# 피터전의 랜스위칭 I 
> 피터전이 랜스위칭 을 읽고 정리합니다.

   
## 스위치 기본 설정 모드



- 이용자 모드 (User mode)
    

    콘솔이나 텔넷으로 스위치에 접속하면 이용자 모드로 들어간다. <br>
    User Mode 에서는 스위칙 관리를 위한 기본적인 명령어만 사용할수 있다.

_이용자 모드 프롬프트_
```
Switch > 
```

- 관리자 모드( privileage Mode)

    관리자모드는 이용자 모드에서 enable 명령어를 사용하면 들어갈수 있다.   
    관리자 모드에서는 스위치의 관한 모든일을 할수 있따.

 _관리자 모드 프롬프트_
```
Switch > enable
Switch#
```

- 설정 모드 ( Configuration Mode )

     설정 모드는 관리자 모드에서 configure terminal (줄여서 conf t) 명령어를 사용하면 들어갈수 있다.   
     이 모드에서 관리자용 패스워드 설정 ,스위치 이름 부여 등 스위치 전체와 관련된 설정 작업을 많이 하며 다른 설정 모드 와 구분하여 전체 설정 모드 (global configuration mode) 라고 한다.

_전체 설정모드 들어가기_
  ```
  Switch# conf t
  Enter configuration commands, one pre line. End with  CNTRL/Z.
  Switch(Config)#
  ```