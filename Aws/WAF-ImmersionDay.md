# WAF Immersion Day

## WAF 란 무엇인가
- 고도로 설정 가능하고 확장 가능한 클라우드 네이티브 웹 어플리케이션 방화벽
- DDOS 공격, 웹 공격 및 봇 공격으로부터 애플리케이션을 보호
- 맞춤형 보안 : 고객 맞춤형 규칙 사용가능
- 다계층 보안 정교한 ????????

## Aws 자원과 통합
- Aws WAF 적용을 하는 과정에서, TLS 구성, DNS 변경 또는 역방향 프록시가 필요하지 않음

### 온프레미스 어플리케이션 보호
- 와프를 CF 를 붙혀서 사용해서 하는것을 추천 하며, ALB, API gW , APpsync , Cognito 등 또한 사용해서 보호가 가능하다.

## 낮은 운영 오버헤드 
- 기본 제공 규칙을 사용할 준비가 되어있는 완전관리형 서비스
### AWS Managed Rule
- 사전 구성된 규칙 세트
  - 일반적인 공격 벡터 및 위협을 커버
  - Shieild Advanced 위협 연구 티에서 선별 및 유지 관리
  - OWASP 상위 10개 웹 어플리케이션 보안 위험 고려
  - 버전 제어 지원
    - 항상 최신 버전을 사용하거나 특정 버전을 유지 하도록 선택 가능
  - 모든 고객이 추가 비용없이 사용 가능
    - Bot Control / ATP 등 일부 규칙은 추가 비용이 발생한다.
### AWS Managed Rules - 사용가능한 무료 규칙 그룹
- Baseline
  - core rule set
  - Admin Protection
  - Known bad input
- Use-case Specific
  - SQL database
  - Linux/Posix/Windows OS
  - PHP/WordPress application
- IP reputation
  - Amazon IP reputaton list
  - Annonymous IP list

### AWS MarketPlace Rules 
- 타사 보안 공급업체에서 작성, 업데이트 및 관리하는 규칙
- Pay as you go : 장기 약정 없음
- 손쉬운 배포
- 다양한 보호 규칙에서 선택
  - OWASP Top 10 및 기타 웹 악용 대처 규칙
  - 일반적인 취약점 및 노출(CVE)
  - 봇 보호
  - IP 평판 목록
  - CMS 규칙 (Wordpress,Joomla 등)
  - Apache , Nginx 취약점

### Cloud Fomation 템플릿
- 클라우드 포메이션 구조로 손쉽게 배포가 가능하다. Managed Rule 을 적용할수 있따.
- HTTP Flood : 인계치 기반 차단 Rule 이 있지만 CloudFomation 에서 LOG 기반으로 작동 할수 있도록 만들 수 잇다.
- Scanner Probe : 이또한 ALB 에서 모니터링 된 로그를 람다 와 아데나를 사용하여 IP 기반 차단하게 된다.
- Bad Bot: 일반적인 사용자가 사용할수 없는 방법으로 요청한다면, 봇으로 인지하고 차단하게 한다.
- Custom Rule 로 다양하게 만들수도 있다.

## 맞춤형 보안
### 주요 용어
- Web ACL : CF 에선 Distribution 이 모든 설정의 기본 단위 이지만 WAF 에선 WEB ACL 이 기본 단위 이다.
- Sample requset : 룰의 대한 요청을 샘플링 하여 콘솔에서 보여준다.
- Log : 풀 로깅
- Metric : 클라우드 워치에서 사용되는 Metric 이다.

### Web ACL Capacity Unit 
- Web ACL 내에서 규칙을 처리하기 위해 사용되는 운영 리소스 를 표현하기 위한 단위
- 기본적으로 웹 ACL 당 허용되는 최대 WCU 는 1,500
- 룰을 만들때마다 차감이 되며, 1500 한도 내에서 룰을 생성 가능하다.
- 룰마다 WCU 값이 다르다.
- 최대 WCU 는 늘릴수있다.

### Rule Statement 
- match statement
  - geographic match
  - ip set match
  - label match rule statement
  - regex match rule statement
  - regex pattern set
  - size constraint 
  - string match 
  - sqli attack
  - xss scripting
- complex statement
  - Managed rule group
  - rule group
  - rate based
  
  ***중첩 구성 불가***
- Logical rules statements
  - And statement 
  - OR statement
  - Not statement

### 웹 요청 구성 요소
- 검사 대상 항목
  - Single Header
  - uri path
  - all headers
  - Querey String
  - Cookie
  - body
  - Single querey parameter
  - json body
  - all querey
  - HTTP method
- 텍스트 변환
  - Lowercase
  - Url decode
  - Base 64 Decode
  - Compress white space

- 오버사이즈 처리
  -  Body : 8kb
  -  Headers : 8Kb / 200개
  -  Cookie : 8kb / 200개
  -  처리옵션
     -  Continue 
     -  Match
     -  No Match

## Customeer Managed Rule
- 고객 관리형 규칙을 사용하여 고객 환경에 특정한 공격과 일치시킬수 있음
  - GUI 를 이용하여 쉽게 규칙 생성
  - 다양한 매칭 옵션 제공

## WAF 응답 처리방식
- 공격이 감지되면 여러 대응 옵션을 기반으로 조치를 ㅜ치할 수 잇음
- Custom request / Custom response 를 설정할수 있음

## 다계층 보안
### Shield Standard 기반의 기본 보호 기능 내장
- 추가 비용 없이 이용 가능
- 기본 AWS 인프라 보호에 중점
- 의심 기반 채점 을 기반으로 공격을 완화 시켜 정상 트래픽에 영향을 주는 것 최소화
- 모든 AWS 리전의 모든 AWS 리소스 에 대한 L3/L4 계층 DDOS 공격의 대한 자동 방어
- CF 및 R 53 사용할때 알려진 모든 네트워크 기반 제어.

### ATP 
계정 탈취 보호 기능은 규칙 기반 및 동작 탑지를 사용하여 일반적......

### AWS Waf 에서 제공하는 가시성
CloudwWatch metrics , Sample Web Request , Full log

경보를 활용한 알림설정 , WAF 규칙 빠르게 테스트 , 로깅

## WAF 비용정책 
- 요청당 부과 100만건당 0.6 달러
- ATP , Botcontrol 룰 을 사용시 과금
  