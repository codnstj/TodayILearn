# Configing Nat Instance in AWS
- ## Nat 서버를 사용하는 이유
  > private 서브넷 에 접근 하기 위해 가장 안전 한 방법중 가장 저렴 한 방법으로 Nat 서버 를 만들어서 이를 Open VPn 으로 접근 한다면 비용 자체도 무료지만 vpn 파일 및 키페어가 없다면 아무나 접근 하지 못하므로 안전하다.

- ## 구성 요소
  - ### Docker
  - ### OpenVPn 
  - ### Nat GateWay
  - ### Nat Service

- ## Docker
  - Nat 인스턴스 내에서 OpenVpn 이 설치 되어있는 컨테이너를 가져오기 때문에 도커를 사용해야만 한다. 일단 리눅스로 만 구성 하는 방법보다 훨씬 빠르고 편한것 같다.

  <br>

  1. ### ssh 를 사용하여  Nat 인스턴스 에 접속한다.
  2. ### 인스턴스에 서맃한 패키지 및 패키지 캐시를 업데이트 한다.
      <pre><code>sudo yum update -y</pre></code> 
  3. ### 최신 도커 엔진 패키지를 설치한다.

       - Amazon Linux 2
       <pre><code>sudo amazon-linux-extras install docker</code></pre>
       - Amazon Linux
       <pre><code>sudo yum install docker</code></pre>
  4. ### 도커 서비스 시작
      <pre><code>sudo service docker start</code></pre>
  5. ### ec2-user를 사용하지 않고도 도커 명령을 실행할 수 있도록 docker 그룹에 sudo.를 추가합니다
      <pre><code>sudo usermod -a -G docker ec2-user</code></pre>
- ## Open VPN
  - Nat 인스턴스 내의 OpenVPn 같은경우 리눅스 내에서 Docker 를 통해 설치를 해주어야 한다.<br> 리눅스 로만 설치 하고 구성 하는 방법은 비효율적이고 어렵다고 나는 생각이 든다.<br>~~주변의 리눅스만 하던 사람도 포기 했다고~~


  
