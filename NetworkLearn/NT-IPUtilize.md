#IP Utilize
>review
```
info : PC의 수는 약 90 대, 스위치 2대 , 라우터 1대 
앞으로 학장되어 3년 이내에 PC가 약 200대로 늘어날 예정.
```
**Q1 | 이사이트에 어떤 클래스 의 IP를 배정 하는것이 가장 적절할까?**
***
정답 : 클래스 C

*클래스 C에 배정할수 있는 클래스 수가 254개로 현재상황에 가장 맞다. 클래스 A나 B가 안되는 것은 아니지만 낭비되는 IP주소가 많을뿌남ㄴ 아니라 이렇게 큰 주소는 배정해 주지도 않습니다.*

**Q2 | 배정받은 IP 주소가 203.240.100.0 네트워크 입니다. 그렇다면 그림에서 네트워크 가 속하지 않는곳은?**
![ex_screenshot](/images/screenshot.jpg)
정답 : 1️⃣(시리얼 인터페이스)

*라우터를 넘어가게 된다면 네트워크는 바뀌게 된다. 따라서 2,3,4,5,6번은 하나의 네트워크 , 즉 하나의 브로드캐스트 도메인 이어서 라우터 없이도 통신이 가능하지만 1️⃣은 반드시 라우터를 거쳐야지만 가능하다.*

**Q3 | 다음중 1번의 IP주소로 적당한것을모두 골라주시기 바랍니다.(참고로 인터넷쪽에서 이 라우터와 연결된 상대편 라우터의 IP 주소는 210.11.2.1입니다)**
```
1️⃣210.1.2.12️⃣210.11.2.23️⃣210.100.1.14️⃣150.10.1.1
5️⃣210.11.2.1256️⃣210.11.100.27️⃣123.11.2.1
8️⃣210.11.2.2559️⃣210.11.2.0
```
정답 2,5

*1️⃣은 상대편 시리얼 과 같은 주소라서 IP충돌이 발생합니다.*

*3️⃣은 서로 다른네트워크 이지만 양쪽 라우터는 서로 같은 네트워크에 속해야 합니다.그러므로 CLASS C 에 속하는 네트워크 이기 때문에 최소하 210.11.2 까지 같아야합니다. 하지만 이는 해당 하지 않습니다.*

*4️⃣역시 서로 다른 네트워크 여서 불가능 합니다. 4️⃣는 CLASS B 라서 클래스도 완전히 다른 네트워크 주소 입니다.*

*6️⃣,7️⃣ 도 다른 네트워크 에 속한 IP주소 입니다.*

*8️⃣ 은 같은 네트워크 에 속하느번호이기는 하지만, 호스트에 부여하는 번호가 아니고 브로드 캐스트용 번호입니다. 라우터의 인터페이스에 부여하는 번호가 아닙니다.*

*9️⃣는 호스트 주소가 아니고 네트워크 그 자체를 표시하는 주소 입니다. 네트워크 주소는 호스트부분을 '0'으로 쓴다는 것 말입니다.*
