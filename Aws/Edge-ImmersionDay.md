# Edge Immersion Day 

## 엣지 서비스 종류
- CF (CDN ,캐시가능, HTTP-HTTPS 워크플로우 가속 가능)
- WAF,Shield (Edge 에서부터 시작됨)
- Global Accelerater (캐시 불가능,가속은 가능,TCP-UDP 워크플로우 가속 가능)

## CloudFront 
  ### CF 란 무엇인가
        
- 낮은 대기시간과 높은 전송속도로 데이터 비디오 애플리케이션 APi 를 전ㄴ 세계 고객에게 안전하게 제공 
- CF 는 글로벌 인프라스트럭쳐와 긴밀하게 연결되어 손쉽게 다른 다양한 AWS 서비스 들과 통합할수 있다.
- 410개의 POP 으로 구성된 글로벌 네트워크를 갖추고 있다.

 ### 사용사례

- 미디어 스트리밍
- 정적 웹 콘텐츠
- 대용량 파일 다운로드
- 전체 웹 사이트
- 모바일 앱 (API)

    정적인 서비스들을 가속하는것 뿐만 아니라 동적인 서비스 또한 가능하다.

## CF Global Edge Network
### POPs (Points is Presence)
- 48개국 90개가 넘는 도시에 걸쳐있다.
- 미드티어 캐시 계층 을 두어 요청이 실패하더라도 요청의 대한 정보가 사라지지 않는다.
- 사용자에서 가까운곳에서 자료가 넘어갈수 있도록 할수있다.
- 한국엔 6개의 로케이션을 가지고 있으며 하나의 미드티어 캐시 를 가지고 있다.

### 이점
- Network Hop 을 최소화
    
     사용자는 한국에 있을때 오리진서버가 미국에 있을시 거리가 멀어져 패킷로스가 일어날수 밖에 없다. CF 를 사용시 로컬 ISP 의 엣지 네트워크 에서 캐시가 되어있는 곳에서 뷰어에게 내려준다.

- Global Network

     다중화된 100GBE 네트워크, 중국을 제외한 AWS 리전과 private Network 로 연결 
     타 CDN 은 퍼블릭으로 글로벌 하게 요청이 가능하지만, AWS 는 Private 한 요청으로 할수 있다.

- Network congestion 최소화
- 분산 방어로 분산 공격에 대응 
  - 각 POP 은 수백 GBPS의 대역폭으로 연결
  - 허용된 포트의 트래픽만 허용
    - CF 는 HTTP, HTTPS 의 트래픽만 허용하게 된다.
  - 들어오는 패킷을 인라인으로 검사하여 악성으로 판명되면 차단
    - 인프라 보호 차원

### CF 동작 원리
- HTML 페이지는 어떻게 서버로부터 전달되는가?
  - 브라우저에서 도메인으로 접속시 DNS resolver 로 IP 를 받게 된다. IP 어드레스 를 얻기 위해서 ROOT NS 와 Toplevel NS 에 요청을 보내서 NS서버의 정보를 받고 이를 통해서 Authoritative name server 에게 요청을 통해서 IP 어드레스를 받는다. 이를 통해 브라우저는 IP 를 통해 Origin 서버로 전송하게 되어 서버는 관련 HTML 을 전송하게 된다.
- CF 는 어떻게 HTML 페이지를 전달 하는가?
  - NS 에 요청을 보내는것 까지는 같지만, Authoritative 네임서버에서 CNAME 을 통해서 질의 를 하게 된다. 이를 통해서 CF 에 CNAME 을 통해서 IP 를 받게 되며,이를 통해서 브라우저가 요청을 보내게 된다.CF nameserver 에서 받는 CNAME 은 클라우드 프론트 엣지 서버 의 IP 주소로 요청을 보내게 되고 이는 WEB 서버와 연결하여 요청을 주고 받게 된다.
  - 트러블 슈팅시 DNS TTL 을 통해서 빠르게 적용될수 있도록 수정해서 트러블 슈팅하기

- DNS 기반 라우팅 
    - Performance , POP Health , Server Capacity , Network Capacity , Traffic Charatacteristics 를 를 통해서 DNS 기반으로 라우팅 하게 된다.
    - 금액 적인 혜택 을 누릴수 있기 위해 특정 리전으로만 엣지 로케이션으로 선택할수 있다.
    - DNS TTL =/ CACHE TTL

- 사용사례 - Cache Miss
    - 사용자가 엣지로케이션으로의 요청을 보냈을때 맞는 캐시 자료가 없다면, 요청을 오리진 서버로 보내며, 이를 다시 엣지 로케이션으로 캐시 설정을 확인하며 저장하고, 이를 다시 사용자에게 전달된다.

- 사용사례 - Cache Hit
  - 사용자가 엣지 로케이션으로의 요청을 보낼시 엣지로케이션에서 일치되는 distribution 이 있다면 이를 바로 사용자에게 전달된다.

- 사용사례 - Refresh Hit
  - 사용자가 엣지로케이션으로의 요청을 보낼시 엣지로케이션에서 일치되는 distribution 의 캐시 가 expired 됬다면, 엣지 로케이션은 컨텐츠가 언제 갱신됬는지 의 대한     ***if-modified-since*** 헤더
 같이 오리진에 요청시 보낸다.컨텐츠가 갱신된 시점이 다르다면, 아까 캐시 미스처럼 요청이 가게 된다. 하지만 컨텐츠가 갱신되었지 않았다면, 똑같이 오리진으로 요청을 보낼시 304 Not Found 를 반환하면서, 같은 캐시를 사용하도록 하게 된다.
   
- Cache 계층 구조

    엣지 로케이션 -> Regional Edge Cache -> Origin Shield(optional) -> Origin 

- Connection Collapsing & Byte streaming
  - Connection Collapsing : 동일하 객체의 대한 복수개의 동시 요청은 캐시 계층을 거치면서 축소
  - Byte streaming : 각 캐시 계층은 첫번쨰 바이트가 도착하는 동시에 다음 계층으로 바로 전송을 시작
    
    두 기능을 통해서 오리진 서버의 대한 부화를 줄일 수 있다.

    대용량 파일을 보낼때도 Byte Streaming 을 통해서 지연시간을 줄일수 있다.
### 보안 이점
- CF 기본 보호 기능
  - 관리형 서비스이다.
  - 알려진 모든 인프라 ( Layer 3 , Layer4) DDOS 공격으로부터 보호할수 있다.
    - 올바른 형식의 HTTP/HTTPS 트래픽만 허용
    - SYN Proxy
    - 모든 패킷을 실시간으로 검사하여 공격탐지시 즉시 완화
    - 엣지 네트워크 를 통해서 활용한 대규모 DDOS 완화 용량
- HTTPS 전송중 암호화
  - Default domain 지원
  - Alternate Domain - ACM 은 추가 비용없이 TLS 인증서를 제공
  - TLS 보안 정책 제어 가능
  - HTTP 를 HTTPS 로 자동 redirection 가능
  - Server Name Indication (SNI) on/off
    - SNI Enable(Default) - TLS 헨드셰이크 중에 서버 이름이 제공
    - SNI Disable - TLS 인증서 전용 IP 필요
- Viewer access control
  - signed URL / signed Cookie 를 이용하여 승인된 사용자만 다운로드 허용
    - GEO - Based allow / deny 
    - AWS WAF 및 Shield Advanced 와의 통합

- Origin Access control
  - S3 오리진
    - S3 대한 공개 엑세스 차단
    - OAI 혹은 OAC(2012 이후 리전 및 기존 리전에 모두 동작 할수 있는 OAI, KMS 암호화 지원 , S3 메소드 PUT / DELET 제공) 를 사용하여 CF 만 엑세스 허용
  - Custom Origin 
    - ***managed prefix list*** 활용
    - 사전에 정의된 ***custom header*** 를 기반으로 origin 에서 엑세스 제어

- Field Level Encryption (FLE)
  - POST 요청시에, 민감한 파라미터는 고객이 제공한 공개키를 사용하여 CF 에서 암호화 할수 있으며 개인 키를 통해서만 복호화 할수 있음

### 가용성 이점

- 다중화된 POP 을 기반으로 한 고 가용성
- 캐싱
  - 오리진 접근 실패시
    - 캐시된 컨텐츠를 활용하게된다.
  - CF benefit
    - TTL 기반의 콘텐츠 캐싱 
    - 요청을 원본으로 전달하지 않고 응답 
    - TTL 만료 이후, State 컨텐츠 응답 가능 

- origin failover
  -  오리진 접근 실패시 ( 캐시된 객체가 존재하지 않거나, 동적 컨텐츠 요청)
     -  세컨더리 오리진으로 자동 Failover

- Customize Error Page
  - 전체 오리진 그룹 접근 불가시
    - 사용자 친화적인 오류 페이지 제공
  - 사용자 정의 오류 페이지, 오류 메시지 캐시 , Lambda@Edge 를 사용하여 추가적인 커스터마이징 가능

### 성능 효율성 이점
- 캐시 최적화 - Cache 서버 내의 계층화
  - 엣지 로케이션에 계층화된 캐시 구성
    - L1 : Connection Termination, hot object 캐싱
    - ***L2 : 매인 캐시 계층 , Hash 를 적용한 캐시 볼륨 최적화***
    - L3 : 오리진과 Connection 관리, 컨텐츠 압축
  - 레이어 선택은 동적이며 트래픽 유형에 맞게 조정 ( 캐시 에딕션 )

- Regional Edge Cache
  - 뷰어가 엣지로 가고 , 엣지가 로케이션 엣지 캐시 로 가며 , REC 오리진 실드 에서 오리진으로 요청을 보내며 티어를 나눠준다.
  - AWS Global Network 를 이용한 가속
    - 빈번하게 혼잡이 발생하는 퍼블릭 인터넷이 아닌, 안정적이고 빠른 성능을 제공하는 AWS Global Network 기반으로 고속 전송
    - 원본이 AWS 리전에 존재하는경우, First mile Network 구간에서 AWS Global Network 기반으로 퍼블릭 인터넷에서 발생하는 혼잡을 배제시킴

- Origin persistent connection 
  - TCP / TLS 핸드셰이크 오버헤드 최소화
    - 확장된 TCP congestion window 유지
  - 캐시가 불가능하거나 짧은 캐시 TTL 을 기반으로 동작하는 API 성능을 개선
  - 오리진에서 TCP/TLS 관련 connection 부하를 절감

- Last-mile network (엔드유저)
  - Viewer 에서 가장 가까운 엣지 로케이션에서 TCP/TLS connection termination 을 수행하여 public internet 구간을 최소화
  - HTTP/2 & HTTP/3 지원
  - TCP 혼잡제어 알고리즘중 하나인 BBR 을 지원함
  - Gzip, Brotli 압축

### 비용 이점
- 비용이 발생하는것 
  - Data Transfer OUT
  - Data Transfer to AWS region (POST/PUT,WebSocket)
  - 캐시 무효화(>1,000)
  - Custom SSl for Dedicated IP
  - Field Level Encrytion
  - CFRC? SSB -> CF 와 WAF 를 붙혀서 패키징. SSB 와 CFRC 는 같이 할인 받을수 없다.

- Data Transfer OUT 비용면제
  - 유저가 ALB 에서 갈떈 비용이 발생하지만 유저와 ALB 사이에 CF 를 두어 사용한다면, CF 와 ALB 까지는 비용이 무료이다. 이를통해서 비용을 절감 할수 있다.

### 운영 우수성 이점
- CF 가시성
  - Cloud Watch Metrics 를 통해서 Alarm 구성 가능
  - Access Log 를 실시간으로 Kinesis Data stream 을 통해서 KDF ,KDA, Open Search 를 통해서 실시간 로그 분석을 가능하다.
  - Access Log 를 일반적으로 s3 버킷으로 로그를 업로드 한후에 이를 Athena 와 Quick Sight 로 분석이 가능하다.