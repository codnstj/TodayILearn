# CICD 관련 계획

## Jenkins 와 CodeDeploy 를 이용해서 CICD 구축 해보장 ^^ ~

- 구축 시나리오
  - `개발자가 소스코드를 깃허브 에 업로드 한다면`
  - `깃허브를 WEB Hook 으로 젠킨스를 도커로 설치한 인스턴스랑 연결된다.` `
  - `젠킨스 가 설치되어있는 인스턴스에서 업로드한 어플리케이션을 테스트 후 S3 로 삘드한다.`
  - `인스턴스에서 Code Deploy 로 배포 요청 한다.`
  - `Code Deploy 에서 Load Balancer 로 배포 시작한다. Load Balancer 에 연결되어있는 두 인스턴스에 배포가 시작 된다.`
  - `배포가 완료되면 소스를 다운로드 하고 스크립트를 실행한다.`

### Log 위치

```Shell
    /opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log
```

```Shell
   less /var/log/aws/codedeploy-agent/codedeploy-agent.log
```
