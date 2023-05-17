# 영우정님 CKA 강의 - 실습 정리할것들.

## installation 
- **Google Kubernetes Engine (GKE)** -> 가장 호환성이 좋으며, 가장 처음 나온 툴
- **Minikube** -> 하나의 컨테이너 안에 K8s 에 필요한 것들이 모두 들어있어 로컬에서 사용가능
- **Kubespray** -> EKS 를 사용하지 않고 AWS 에서 K8s 를 사용하기위해 사용
- **Kubernetes Operations (kops)** -> 온프레미스에 구축시 필요한 Ansible Playbook
- MicroK8s 
- Both need kubectl
- kubeadm newer tool -> kubeadm 컨테이너를 통해 셋팅 가능 , 이걸 자동화 하는것이 kubespray -> 가장 일반적인 방법, 모든 리눅스에서 가능 but windows 불가능
- kuberntes the hard way -> Kubernetes 를 어렵게 구성, 직접 모든 것을 다 구성해야하는것.

### Kubectl
-  AWS CLI 와 같은 존재 구성파일이 존재하여 이를 통해 추가적인 옵션 추가 가능 ex) Endpoint, SSL Keys, contexts

EKS = 다운그레이드 가 불가능하다. 그렇기 때문에 신중하게 업그레이드 해야한다.

API-Server -> 고가용성 때문에 갯수가 상관이 없다.

### 마스터 노드 갯수 = 홀수여야한다? 이건 맞지만 이유는?

마스터 노드 (API-Server,Controller-manager,Scheduler 로 구성되어있음)
모든 노드 (kublet, kybe-proxy)
ETCD 노드 (데이터 베이스) -> 리더/팔로워

if ETCD 3개 존재시 하나 가 리더, 나머지는 팔로워 이다.

ETCD 노드들은 서로 살아있는지 체크

체크가 안된다면 election 진행 -> 과반수가 참석해야 진행이 가능

그렇기에 짝수도 되지만, 홀수 도 된다. failure tolerance 가 짝수일때 비 효율적이기 떄문에 홀수가 권장된다.

if ETCD 모든 팔로워 가 디지면, 클러스터는 작동하지 않습니다.
왜? -> 쓰기 요청을 했을시 쓰기 복제본이 없기 때문에 

마스터 노드를 만들시 ETCD를 포함시키는것이 대부분이다. 마스터 노드가 많을 시 API - SErver 는 로드밸런서에 의해 분산 된다. Controller-manager와 Scheduler 는 Active/Stanby 형식으로 하게 된다.

### EKS 업데이트
1. API 서버 업데이트 -> API Server등 구성요소 업데이트
2. 노드그룹 -> kublet

버전 호환성 체크, 없어지는 API가 있는지 체크, EKS 업데이트 되는 부분 체크.   

VPC 는 EKS CNI 를 지원하지 않는다. 서드파티 사용해야함