# 네트워크 복습 1

**네트워크**는 정보공유를 목적으로 PC와 PC들이 모여서 구성된 망입니다.
이러한 정보들, 데이터들을  보내기 위한 도구들을 **프로토콜**이라고 합니다.

- **프로토콜** : TCP,IP,Ethernet

*이런 프로토콜 드을 추가하는것이 <u>인캡슐레이션</u>,확인하려 빼내는 게 <u>디캡슐레이션</u>*

  
- **LEN** : 로컬 네트워크.Ethernet 사용 

*버스 토폴로지(네트워크 형태?) , 스타 토폴로지 등이 있는데, 권장은 스타토폴로지+이중화 장비 -> 확장성,이중성,가중성 확보되며 안정성 보장*

- **WAN** : 외부 네트워크. ISP 업체로부터 회선을 임대해 사용

*이러한 네트워크를 통해 데이터를 전송하는데, 전송방식에 따라 호칭하는 이름이 다릅니다.*

- **OSI 7Layer** : 데이터 생성과 전송 과정을 7계층으로 제시한 모댈

    Layer 7 Application(응용 계층)

    Layer 6 Presentation(표현 계층)

    Layer 5 Session(세션 계층)

    Layer 4 TransPort(전송 계층) : Tcp/Udp

    Layer 3 Network : IP

    Layer 2 DataLink : Ethernet

    Layer 1 Physical : 전기신호 처리

> Part 5

- 라우터에서 의 IP 주소

![a.png](/images/a.png)
  - 이더넷 인터페이스 : 네부 네트워크 와 연결되는 라우터의 포트 
     
     이더넷 용 IP주소 에는 우리가 내부에서 사용하기 위해 부여받은 IP 주소 중 하나를 배정해야 함.

  - 시리얼 인터페이스 : 외부 (즉 인터넷) 로 연결 되는 인터페이스 
  
     상대편 라우터의 시리얼 인터페이스와 IP 주소를 서로 맞추어야 한다.
     
- IP = 네트워크 부분 + 호스트 부분
 
    (네트워크 : 하나의 브로드 캐스트 영역 , 라우터 를 거치지 않고도 데이터를 주고 받을수 있는 영역)
  
  - 하나의 네트워크 에서는 네트워크 부분은 모두 같아야 하고, 호스트 부분은 모두 달라야 통신이 가능
  - 네트워크 부분만이 라우터가 라우팅할때 참고함.

- IP 주소의 Class 
    - 하나의 클래스  몇 개의 호스트를 가질 수 있느냐 에 따라 
![d.png](/images/d.png)
    (사진에서 동그라미는 2진수 8자리를 나타냄)
    - 호스트 부분이 모두 0 인 경우는 네트워크 자체를 , 모두 1인경우는 브로드캐스트 주소를 의미하기 때문에 주소로 사용하지 않음 !!(Host 수에 -2 가 돼 있는게 바로 이 이유 때문)

    - Class A : Network 부분 8bit , Host 부분 24bit 
      - 주소 맨 앞자리가 0 으로 시작.
    - Class B : Network 부분 16bit , Host 부분 16bit
      - 주소 맨 앞자리가 10으로 시작
      - 주소는 10000000.0.0.0 ~ 10111111.255.255.255.255 까지 사용 가능 하다
    - Class C : Network 부분 32 bit , Host 부분 8 bit 
      - 주소는 맨 앞자리가 110 으로 시작
      - 즈소는 11000000.0.0.0 ~ 11000000.255.255.255 까지 사용 가능 
- 서브넷 마스크 
  - 주어진 IP 주소를 네트워크 환경에 맞게 나누어 주기 위해서 씌워주는 이진수 조합
  1. 브로드캐스트 영역을 나누기 위해서 사용됨
  2. IP 주소를 아끼기 위해서 사용됨
  3. IP 주소를 가지고 어디까지가 네트워크 이고, 어디까지가 호스트 부분인가를 나타내는 역할
- 디폴트 서브넷 마스크 
  - IP 주소를 나누어 쓰지 않고 그대로 사용해도 서브넷 마스크가 따라 다님
    - Class A Default Subnet Mask : 255.0.0.0
    - Class B Default Subnet Mask : 255.255.0.0
    - Class C Default Subnet Mask : 255.255.255.0

- 서브넷 마스크 의 성질
  - **서브넷은 하나의 네트워크 이기 때문에 서로 나뉘어진 서브넷끼리는 라우터를 통해서만 통신가능**
  - **서브넷마스크는 이진수로 썻을때 1이 연속적으로 나와야한다.**