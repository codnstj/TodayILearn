# Shield Immersion Day

## DDOS 란 무엇인가

### DDOS 란?
- 합법적인 사용자의 서비스 엑세스 거부 (Dos)
- 효율성을 높이기 위해 여러 소스에서 공격

### DDOS 공격 유형
- 인프라 계층 공격
  - 볼륨기반
    - 대상 의 대역폭 포화를 목표로 합니다
      - UDP/ICMP floods
      - Reflection/amplification
  - 프로토콜 기반
    - 타겟 서버 혹은 타겟 경로상에 있는 네트워크 장치 ( 라우터, 방화벽 , 로드밸런서) 의 리소스 고갈을 목표로 함
      - SYN floods
      - Fragmentation attacks
- 어플리케이션 계층 공격
  - 자원 고갈 및 웹 또는 어플리케이션 서버의 다운을 목표로 함
    - HTTP GET/POST floods
    - Slow read/post attacks

### 일반적인 DDOS 완화 기술
- 볼륨기반
  - BPS and PPS rate limits
  - Network ACL
  - Large bandwidth
  - Traffic engineering
- 프로토콜 기반
    - Protocol Validation
    - Protocol Specific PPS rate limits
    - Protocol specific techniques (SYN Cookies, Bad DNS resolvers, etc...)
    - Service scale up/out
  - 어플리케이션 계층
    - Application level rate limiting (e.g. HTTP rate limit)
    - 원하지 않는 동작을 차단하는 웹 어플리케이션 방화벽 또는 네트워크 방화벽 (IPS)
    - 경계에서 소스 인증 (signed cookies, tokens, bot control)
    - Application scale up/out

## DDOS 공격을 차단하는 방법
- DDOS 공격에 복원력 있는 아키텍쳐를 구성 하는것.
  - WAF를 이용해서 복원력을 키우기
  - AWS Edge Location 을 활용
    - CF : 완전한 인라인 DDOS 완화 시스템 : 탐지 지연 없이 자주 사용되는 인프라 계층 DDOS 공격으로부터 어플리케이션 보호
    - STN Proxy: SYN proxy 기능은 새로운 연결 시도의 대하여 SYN cookie 기반의 인증을 수행하여 합법적인 최종 사용자에게만 서비스를 제공
    - 오류 격리 : 공격 볼륨으로 인해 AWS 에 인접해 있는 업스트림 네트워크 구간에서 정체가 발생하는 경우, 정체 구간이 소스에 더 가깝게 격리되고 합법적인 최종 사용자에게 미치는 영향이 최소화
    - 전 세계적으로 분산된 네트워크 : AWS EDGE LOCATION 은 Shield 의 DDOS 완화 기능에 대한 광범위한 액세스 제공
  - 공격 표면 최소화 하기 
    - NACL 및 인프라 아키텍쳐를 최소환의 범위로 AWS 아키텍쳐를 공개 하기.

## AWS Shield
### AWS Shield vs Shield Advanced
- 스탠다드 같은 경우는 AWS 고객이 추가비용 없이 사용할수 없으며 네트워크 규모를 활용해 가장 일반적인 인프라 공격으로부터 자동으로 보호
- 스탠다드 어드밴스드 는 12개월 약정의 프리미엄 유로서비스 (3000불)
- 스탠다드 티어에서 제공 하는것 이외에도 많은것들을 제공    
  - 중앙집중식 관리를 위한 방화벽 관리자 를 제공한다.
  - 인프라 및 어플리케이션 보호 (l3 ~ l7)
  - WAF 를 통한 어플리케이션 공격 탐지 및 자동 완화 
  - 실시간에 가까운 이벤트 가시성 및 알람
  - 상태 기반 감지 및 선제적 이벤트 대응
  - 24/7 쉴드 리스폰스 팀 지원
  - 공격중에 발생한 확장에 대한 비용 보호

### AWS Shield 인프라 계층 보호
- AWS 쉴드 디도스 완화 시스템은 AWS 네트워크 경계와 엣지 위치함
  - 쉴드 엣지 리소스 와 보더 로컬 리소스는 지원되는 부분이 다르다.

### 어플리케이션 트래픽 이상 감지
- AWS 쉴드 레이어 7 리소스 (CF , ALB) 의 대한 트래픽 베이스 라인이 설정
- 베이스 라인은 최대 30일치의 데이터를 참고하게 되며.
- 베이스라인으로부터 상당한 편차 ( 볼륨 또는 엔트로피 변화) 가 발생하면 DDOS 이벤트로 보고됨
- 라우트 53 의 헬스체크 상태는 공격탐지 및 완화 수행에 도움을 줌

## 어플리케이션 계층 DDOS 자동 완화
### 완화 시간 단축 및 어플리케이션 가용성 위협에 즉시 대응
- 감지된 디도스 이벤트를 완화 하기 위해 WAF 규칙이 자동으로 생성
- 오탐을 최소화 하기 위해 정상 트래픽에 대해 와프 규칙을 테스트 
- 와프 규칙은 차단 모드를 배포하기 전에 효과를 관찰하기 위해 카운트 모드에서 생성할수 있음
- 이벤트가 가라앉으면 와프규칙이 자동으로 제거
- 수동 개입 불필요

## SRT 지원 
SRT 팀은 DDOS 공격으로부터 AWS 및 고객을 보호하는데 전념하는 고도로 숙련된 엔지니어로 구성되어있으며, 다음과 같은 지원을 제공
  - 자동으로 완화되지 않는 DDos 공격으로부터 어플리케이션이 손상된 경우 해당공격을 완화할 수 있도록 공격 진행 상황에서 바로 지원
  - 연중 무휴 24 시간 선제적 이벤트 대응을 제공
  - 이벤트중 WAF 규칙 생성 지원

요구 조건
- 지원 혜택을 받으려면 shield acvanced 에 가입하고 인터넷 연결 리소스를 보호 자원으로 등록해야함
- SRT 에 연락하려면 엔터프라이즈 서포트 플랜 이 필요 (또는 비즈니스 서포트 플랜)

## 가격책정 의 대해 기억해야할것
- 쉴드 어드밴스드 가입시 1년 약정이다.
- 쉴드 어드밴스드 의 비용으 ㄴ월간 구독료 3000불 + 각 보호 리소스에서 발생하는 데이터 전송 사용료(GB당) 을 기반으로 함
- 3k/월 구독료는 AWS 오가니제이션 단위로 적용이 가능
  - 여러개의 어카운트가 하낭의 오가니제이션으로 묶여있는경우 오가니제이션 레벨에서 한번만 월 구독료 청구
  - 회사에 여러 오가니제이션이 있는 경우 , 연락하여 지불을 통합하고 회사전체에 대해 하나의 구독료만 지불할 수 있음
  - 오가니제이션에 연결되어 있는 어떤 어카운트 에서도 쉴드 어드밴스드를 구독할수 있다.