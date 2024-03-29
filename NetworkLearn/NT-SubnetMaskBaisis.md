# Subnet Mask Basis(important)
>**서브넷 마스크 란?**
 ``` 
 일단 말뜻 그대로 서브, 즉 메인 이 아닌 어떤 가공을 통한 네트워크를 만들기 위해서 씌우는 마스크 --서브넷 마스크 는 주어진 IP주소를 네트워크 환경에 맞게 나누어 주기 위해서 씌워주는 이진수의 조합이다.--
 ```
 예를 들어 클래스 B를 받아서 서브넷을 만들지 않고 그냥 사용하는 경우 브로드 캐스트 도메인이 너무 커져서 브로드 캐스트가 너무 많이 발생하게 되어 정상적인 통신이 불가능 하여 이 네트워크에는 서브넷팅 이 필요합니다.

 * 서브넷 마스크를 사용하게 되면 브로드 캐스트 도메인을 작게 나뉘는 것이다.
 * 원래 디폴트 마스크는 255.255.0.0 이지만 새로운 서브넷 마스크 255.255.255.0 으로 바뀝니다.
 * 각각의 서브넷 간의 통신은 라우터를 통해서만 가능합니다. 
 * 서브넷 마스크는 커다란 네트워크를 잘게 나누기 위해서 필요하다는것이다.


***서브넷 마스크 는 IP주소를 가지고 어디까지가 네트워크 부분이고, 또 어디까지가 호스트 부분인지를 나타내는 역할이다. 따라서 서브넷 마스크를 보면 네트워크 부분과 호스트 부분을 알수 있습니다.***
 <hr/>


>**서브넷 마스크로 네트워크 의 특성 파악하기**

주어진 네트워크 가 210.100.100.1 이고 서브넷 마스크가 255.255.255.0 일때 

255.255.255.0 은 1111 1111.1111 1111.1111 1111.0000 0000 이다.
 
서브넷 마스크는 1인 부분은 네트워크 부분을 그리고 0인 부분을 호스트부분을 나타낸다.

그러므로 앞의 3자리는 모두 1로 구성되어있으니 앞의 3자리는 네트워크 부분을 나타내는 것이고 나머지 한자리가 호스트부분을 나타내는것이다.

그러므로 210.100.100.1 은 클래스 C의 네트워크 이다.

그리고 이러하여 **255.255.255.0은 클래스 C의 디폴트 서브넷 마스크 이다.

>**서브넷 마스킹**

서브넷 마스킹이란 ***IP주소와 디폴트 서브넷 마스크를 AND 연산하여 IP주소의 네트워크 부분을 나타내게 하는 작업입니다.***

서브넷 마스킹을 하게 되면 IP 주소의 네트워크의 크기 및 네트워크 의 클래스를 알수 있습니다.
>**서브넷팅**
이런 서브넷마스킹 을 해줄때 디폴트 서브넷 마스크 가 아닌 다른 크기의 서브넷 마스크를 사용하는것을 서브넷팅이라고 한다. 이를 하게되면 클래스 B 주소를 마치 클래스 C 처럼 사용할수 있게 된다. **즉 하나의 주소를 서브넷 마스크를 씌워서 작은 네트워크로 만드는 것을 서브네팅 이라고 합니다.**

