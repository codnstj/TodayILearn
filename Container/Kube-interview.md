# Kube Interview
- K8s 의 구성요소
    - Master Node
        1. Kubectl
        
        쿠버네티스 클러스터에 명령을 내리는 커맨드라인 도구 입니다 . 일반적으로 개발자들은 API 서버와 통신하므로 API 서버가 위치한 마스터 노드에 구성된다.
        2. API Server
        
        쿠버네티스 클러스터의 중심역할을 하는 통로이다. RESTAPI 형태로 구성되어있으며 , kubectl 이 명령을 보내면 이를 적절한 위치로 명령을 전달해주는 역할을 합니다.
        3. etcd
        
        구성요소 들의 상태 값이 모두 저장되는 곳 , 서비스들이 위치한 서버의 IP 주소 및 PORT 번호 등이 저장된다. etcd 외의 다른 구성요소는 상태값은 관리하지 않는다. Key-value 형싱의 저장소 이므로 복제해서 여러곳에 저장해두면 하나의 etcd 에서 장애가 나더라도 가용성을 확보할수 있습니다.
        4. c-m( controller Manager )
        
        쿠버네티스 클러스터의 오브젝트 상태를 관리한다.특정 워커 노드가 통신 불능이 된 경우 , 상태 체크와 복구 작업은 컨트롤러 매니저에 속한 노드 컨트롤러에서 이루어진다. 이처럼 다양한 상태값을 관리하는 주체들이 CM 에 소속되어 각자의 역할을 수행한다.
        5. 스케줄러
        
        노드 의 상태와 자원 , 레이블 , 요구 조건등을 고려해 파드를 어떤 워커 노드에 생성할 것인지를 결정하고 할당한다. 파들르 조건에 맞는 워커 노드에 지정하고 , 파드가 워커 노드에 할당되는 일정을 관리하는 역할을 담당한다.
    
    - WorkerNode
        1. kublet
        파드의 구성 내용(PodSpec) 을 받아서 컨테이너 런타임으로 전달하거, 파드안의 컨테이너들이 정상적으로 작동하는지 모니터링 한다.

        2. 컨테이너 런타임 (Container Runtime Interface, CRI)
        파드를 이루는 컨테이너의 실행을 담당한다. 파드안에서 다양한 종류의 컨테이너가 문제없게 작동하게 만드는 표준 인터페이스 이다. 

        3. POD
        한개 이상의 컨테이너로 단일 목적의 일을 하기 위해서 모인 단위 이다.
        즉, 웹 서버 역할을 할 수도 있고 로그나 데이터를 분석할 수도 있다.            

    - `파드가 배포된 이후 개발자 입장에서 배포된 파드에 접속하는 과정이다.`
        - Kube-proxy
        쿠버네티스 클러스터는 파드가 위치한 노드에 kube-proxy 를 통해 파드가 통신할수 있는 네트워크를 설정해준다.
- 핵심 쿠버네티스 컴포넌트
  - Node 와 Pod
    - 여기서의 노드는 하나의 물리 머신 및 가상머신이라고 할수 있다.
    - POD 은 쿠버네티스에서의 가장 기본적이고 심플한 구성요소 이다. 이를 Abstraction over container 이라고 한다.
    - 