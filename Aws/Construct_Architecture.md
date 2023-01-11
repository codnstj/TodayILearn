# AWS 아키텍쳐 구축 유의사항

구축순서
1. VPC
2. 스토리지 서비스 (RDS , EFS , Elastic Cache)
3. EC2 , ALB 와 같은 어플리케이션 서비스 및 Auto Scailing Group


1. VPC
	- VPC 는 대부분 /16 대역으로 대부분 구성하게 된다. 더작게 구성해도 되지만 혹시 IP 가 부족할 상황에 대비해서 크게 잡는데 , 더작은 범위로 구성할 수 있다. 
	- AZ 같은경우는 예싱서는 3개를 사용한다. 3개의 AZ 중 2개는 리소스를 구성하는데 사용하며, 나머지 하나의 가용영역은 재해복구 상황시 사용된다.
	- Nat 인스턴스 혹은 Nat Gateway 를 구성시 단일 가용영역에 구성할지 , 아니면, 다중 가용영역에 구성할지 잘 봐야한다.

2. Storage Service
	- RDS 는 이름을 바꿀시 EndPoint 도 바뀌기 떄문에 구성 전에 미리 확인해야한다.
	- 스토리지 유형을 바꿀시 ( IOPS , GP2 ,GP3) IOPS 와 같은경우는 비용이 꽤 나가기 떄문에 확인해야한다. 별다른 요청이 없다면 범용 SSD를 사용하는것이 맞다
	- 마이너 업그레이는 비활성화 해야한다. 이는 업그레이드 시 롤링으로 배포되기 때문에 이를 비활성화 하지 않는다면 RDS 가 중지되며 업그레이드 가 진행된다. 때문에 유지관리 기간 을 설정 하거나 비활성화 하는것이 좋다. 참고로 유지 관리 기간 은 UTC 기준이기 떄문에 한국시간에 맞춰 설정해야한다.
 	- 암호화 관련해서 대부분 암호화를 하는것이 좋지만, 이는 담당 SA 에게 물어볼것
	- 파라미터 그룹 , 보안그룹 , 옵션그룹 , 서브넷 그룹 은 RDS 를 구성하면서 같이 구성하는것이 아닌 미리 구성하는것이 좋다
	- EFS 는 돈이 많이 나간다. 왜냐하면 기본 3AZ 구성이며, 이외에 백업까지 있기 때문에 요금이 비싸다.
	- RDS 클러스터링 같은 경우는 용도에 따라 진행하게 된다.
	- Master & Slave 구조에서, Master 는 Write 를 처리하며, Slave 는 Read 를 처리한다. 
	- Active & Standby 구조의 Active 는 평상시 Request 를 받아 처리할수 있는 시스템이며, Standby 는 Passive , Backup 이라고 불리며, Active 시스템의 장애시 Request 를 처리할수 있는 시스템이다.


보안그룹을 설정할 시 해당 규칙의 대한 설명을 써주는것이 좋다.

3. Application Service
	- ALB 와 CF 간의 보안그룹 을 설정시 CF 는 관리형 접두사를 써야한다.
	- 보안그룹 이름 너무 길게 설정하지 말것, 다른서비스에서 보안그룹을 검색할시에 ,보안그룹의 이름이 잘려나와 검색할 수 없음 그렇기 때문에 간결하게 지어야한다.
	- 리소스의 네이밍 규칙이 제공되지 않는다면 대부분 알아서 짜야하지만 , 이는 SA 에게 문의 해서 알아봐야하는 요소이다.
	- EC2 및 다른 서비스에 IAM 역할 을 구성해야하는 경우 이는 구성하기 전에 IAM 역할을 만들어서 미리미리 attatch 하도록 하자.
