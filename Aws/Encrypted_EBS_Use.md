# 암호화된 EBS 사용

일반적으로 고객관리형 키로 암호화 된 EBS 볼륨을 해독하려면 권한이 있어야합니다.해당 볼륨을 사용하려 한다면, 해당 키의 대한 권한이 있어야 하므로 해당 키의 사용자로 등록해 야 하는 과정이 있어야 합니다.

EC2 를 생성할시 사용할 볼륨을 암호화 하는 과정 에서 EC2 를 생성하게 되는 주체인 IAM User 와 Role 에 `kms:ListAliases` 권한이 없다면 Kms 키를 나열할 수 없게 되며, 암호화 하지 못합니다. 하지만 중지된 인스턴스 를 복구 하는 과정에서는 해당 권한이 필요 없습니다.

Auto Scailing Group 에서 Scale OUT 을 할 시 사용되는 권한은 , `aws-service-role`의 `AWSServiceRoleForAutoScailing` 입니다. 해당 Role 은 사용자가 만들어 주는것이 아닌 AWS 서비스에서 공급 해주는것이기 때문에 해당 Role 의 권한을 바탕으로 Scale OUT 해주는것입니다.

그렇기 때문에 암호화된 볼륨을 가진 EC2 인스턴스 의 시작 템플릿으로  Auto Scailing Group 을 구성 할 시 해당 인스턴스의 EBS 볼륨을 암호화한 키 정책에서 AutoScailing Group 의 Role 을 해당 고객관리형 키의 사용자로 등록해주어야 합니다.

![Screenshot 2023-01-09 at 4 29 48 PM copy](https://user-images.githubusercontent.com/69895368/211265274-7c640654-7e42-457c-90b9-d6f5f3f80490.png)

그렇게 되면 해당 역할이 Scale Out 작업시 오류가 발생하지 않게 됩니다.

정리하자면,

1. KMS 고객 관리형 키를 이용해서 암호화 한 EBS 볼륨 을 사용하는 EC2 를 생성할시, KMS 키 를 지정하기 위해 IAM 유저 또는 Role 에 `kms:ListAliases` 필요합니다.

2. KMS 고객 관리형 키를 이용해서 암호화 한 EBS 볼륨 을 사용하는 EC2 의 스냅샷을 생성할 경우 별다른 권한이 부여 될 필요가 없습니다.

3. KMS 고객 관리형 키를 이용해서 암호화 한 EBS 볼륨 을 사용하는 EC2 의 스냅샷을 복원 하는 경우 복원하는 주체 (IAM role , IAM user) 에 KMS 권한 이 없다면 생성되자마자 바로 EC2 가 종료되어 권한이 필요합니다.
스냅샷에 이미 볼륨 암호화의 대한 키가 등록되어 있으므로 Restore 시 별도로 키를 지정해 줄 필요 가 없습니다.

1. KMS 고객 관리형 키를 이용해서 암호화 한 EBS 볼륨 을 사용하는 EC2 의 Auto Scailing Group 을 구성하기 위해선 Auto Scailing Group Role 을 KMS 키 정책에 추가해야 합니다. **AutoScailing Group 에서 EC2 를 생성시 Ec2 를 생성하는 주체가 사용자가 아니고 Auto Scailing Group 이기 때문에 IAM 유저가 아닌 `aws-service-role` 의 `AWSServiceRoleForAutoScailing` 을 통해서 EC2 를 생성 합니다.**

    > 해당 role 은 따로 생성해 주어야하는것이 아닌, AWS 에서 제공해주는 역할이므로 따로 생성할 필요 없이 KMS 키 정책에 등록해주기만 하면 됩니다.
