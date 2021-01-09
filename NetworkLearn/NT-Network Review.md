# 네트워크 기본 개념

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

