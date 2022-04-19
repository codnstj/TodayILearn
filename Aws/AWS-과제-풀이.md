1. Java Spring Boot(backend), Aurora MySQL, S3 Static(frontend), Cloudfront기반으로 서비스를 하려고 합니다. 서비스를 하기 위한 Architecture를 작성하고 간단한 설명을 작성해주세요. 

   - 1번 아키텍쳐에선  “고가용성” 을 중점적으로 구축 하였습니다. 개발자들은 각 가용영역의 Public 서브넷의 Bastion 서버를 통해서 각 가용영역의 Private 서브넷 내부의 오토 스케일링 그룹에 접근 할수있습니다. DB 는 프라이빗 서브넷에 같이 있으며 Auto Scailing Group 에서 Private A 서브넷에 있는 Active DB 에 접근 합니다. 그리고 혹시나 모를 상황을 대비해 다른 가용영역에 StandBy DB 를 구축하여 현재 가용영역 A 에 있는 DB 에 장애가 생기더라도 StandBy DB 에 접근할수 있도록 연결 해놓고 , Active DB 는 자동으로 동기식 복제를 통해서 Slave 가 Master 로 승격되어 접근 가능할수 있도록 구성합니다. S3 는 CloudFront 를 사용해서 글로벌 Accellerater 를 통해서 전세계에서도 접근 가능하도록 구성하였습니다. 마지막으로 서버 의 AutoScailing Group 을 ALB 로 연결하여 Route53 의 도메인 영역에서 접근 가능 할수 있도록 구성하였고 , Cloud Front 에서 나온 CDN URL 도 Route53 을 통해서 접근 가능할수 있도록 했습니다. User 들은 Route53 의 도메인 영역을 통해서 내부 서버 및 정적 페이지에 접근 할수 있도록 아키텍쳐를 구성하였습니다.

2. AWS Account를 개발환경과 운영환경 두개로 운영중입니다. 신규 개발된 Application을 테스트를 하기 위해 개발환경에 운영 데이터가 필요하게 되었습니다. 운영환경 RDS(Aurora MySQL)을 개발환경에서 사용하려면 어떻게 해야 할까요? 해당되는 방법과 절차를 작성해주세요.

   - 기존의 운영환경의 데이터베이스 의 스냅샷을 복제하여 이를 공유하여 다시 구축 하는것보다 훨씬 리소스 및 구성시간 이 단축 되기때문에 교차 계정 복제를 사용하는것이 좋을것 같습니다.
   - 먼저 RDS 에 가서 복제할 데이터베이스를 선택 한뒤 연결 및 보안 탭에가서 다른 AWS 계정과 DB 클러스터 공유 섹션에서 클러스터를 복제할수 있도록 계정 ID 를 입력합니다. 그뒤 다른 계정에 가서 공유 초대를 수락하고 DB 클러스터를 복제합니다.

