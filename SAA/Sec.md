# Security 관련 문제 풀이

- WAF -> XSS,SQL Injection 방어의 대한 목적
- Shield,WAF(rate-based-rule) -> DDOS 방어의 대한 목적
- NLB 에서 Application Layer 로 전송과정 에서의 보안 -> TLS 리스너 구성
- Guard Duty -> Aws 계정의 대한 공격 방어 및 모니터링
- Inspector -> 아키텍쳐 냅 취약점을 분석
- Marcie -> 개인 식별 번호 및 중요번호 식별후 경고
- Cognito -> 유저 풀의 대한 보안 
- Single Points of Failure -> 전체시스템중 특정 부분의 대한 문제가 생기면 전체 서비스가 정상적인 작동이 되지 않는 요소
- 3티어 -> Multi AZ WEB SERVER,Multi AZ WAS, Multi AZ RDS
- 2티어 -> Single AZ WEB SERVER, Single AZ WAS, Multi AZ RDS
- 3티어 + SQS 구성에서 지연시간 감소하려면 -> SQS 에서 WAS  가는 부분에서 병목이 일어남, 그렇기 떄문에 WAS 의 대한 EC2 Auto Scailing 이 적용되어야 한다.
-  키사용 기간 측정 -> AWS Config