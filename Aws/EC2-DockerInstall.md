# Installing Docker in EC2

//도커 설치
[ec2-user@ip---]$ sudo yum install docker.io
//도커 리스트 확인
[ec2-user@ip---]$ docker ps -a

Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

**해결 : 도커 의 프로그램의 권한 설정이 SUDO 로 되어있기 때문에 이 권한을 일반 유저의 권한으로 내려주어야 Sudo 를 사용하지 않고 Docker를 조금더 편하게 사용할수 있다.**

```
[ec2-user@ip---]$ sudo systemctl start docker

[ec2-user@ip---]$ docker ps -a

Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http:// %2Fvar%2Frun%2Fdocker.sock/v1.40/containers/json?all=1: dial unix /var/run/docker.sock: connect: permission denied

[ec2-user@ip---]$ sudo setfacl -m user:ec2-user:rw /var/run/docker.sock
```

# Installing Jira in EC2 using Docker

// 기존 지라 도커 컨테이너 삭제
[ec2-user@ip---]$ docker rm --volumes --force "jira-container"

// 지라 도커 컨테이너 설치
[ec2-user@ip---]$ docker pull cptactionhank/atlassian-jira-software:latest

// 지라 도커 컨테이너 생성
[ec2-user@ip---]$ docker create --restart=no --name "jira-container"\
 --publish "8080:8080"\
 --volume "hostpath:/var/atlassian/jira"\
 --env "CATALINA_OPTS= -Xms1024m -Xmx1024m -Datlassian.plugins.enable.wait=300"\
 cptactionhank/atlassian-jira-software:latest

                    or

[ec2-user@ip---]$ docker create --restart=no --name "jira-container" --publish "8080:8080" --volume "hostpath:/var/atlassian/jira" --env "CATALINA_OPTS= -Xms1024m -Xmx1024m -Datlassian.plugins.enable.wait=300" cptactionhank/atlassian-jira-software:latest

//지라 도커 컨테이너 실행
[ec2-user@ip---]$ docker start --attach "jira-container"
