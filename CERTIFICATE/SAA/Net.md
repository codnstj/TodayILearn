# Network 관련 문제 풀이

- NLB 에서 Application 으로 전송 과정중 보안 -> TLS 
- NLB 에서 사용하는 프로토콜 -> TCP,UDP,TLS
- TCP,UDP 기반의 워크로드의 가용성 높이는 것 -> NLB 를 각각의 가용영역에 배치
- 특정 IP 주소와만 통신할수 있게 만들어주는 ELB -> NLB
- 특정 URL 주소와만 통신할수 있게 만들어주는 ELB -> ALB
- TCP 트래픽 분산  -> NLB