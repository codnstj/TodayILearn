# Storage 관련 문제 풀이

- Co-Location 에서 S3 로 이동 -> SnowBall 사용
- S3 에서 다른 S3 로의 데이터 이동 -> S3 교차리전 구성
- 정적 콘텐츠의 제공 부분의 대한 성능개선 -> Cloud Front
- TCP,UDP 기반 광범위한 어플리케이션의 성능개선 -> Global Accelerate
- RDS Single AZ 에서 Multi AZ 로 변경할땐 실시간으로 변경이 가능하여 다운타임이 줄어듬
- S3 Standard -> 3개의 가용영역에 저장 (자주 엑세스 하는 파일)
- S3 Standard IA -> 3개의 가용영역에 저장 (자주 엑세스 하지 않는 파일)
- S3 ONE-ZONE IA -> 1개의 가용영역에 저장 (자주 엑세스 하지 않음)
- S3 Intelligence-Tiering (지능형 계층화) -> 알아서 안쓰는 파일을 저렴한 엑세스 계층으로 이동
- S3 IA 는 ACCESS 할시에 비용 부과
- S3 Glacier 는 검색시간이 오래걸림
- 스토리지 중 최고성능 -> instance Store
- 데이터 베이스 저장용 스토리지 서비스 -> Instance Store, EBS
- EBS 는 공유 개념이 아니기 때문에 자료를 공유해야하는 상황이라면, EFS 를 사용해서 공유 함.
- 버킷 공유시 가장 적은노력이 드는것 -> 교차 계정 엑세스 허용
- 
