# CF 몰랐던점 정리

## 캐싱이 되는 방법

CF 에서 캐싱을 하는 방법으로는 캐시키를 확인하고, 캐시 키가 적중(cache key hit) 하게 되면 캐싱 리소스를 전달하고 캐시키가 미적중(cache miss) 하게 된다면 오리진으로 해당 경로의 객체를 가져오게 됩니다.

## CF에서는 OPTION 메서드 로 오는 트래픽 만 캐싱이 가능할까?

CF 를 사용하여 캐싱하게 된다면 `GET`, `HEAD` 메서드 로 오는 트래픽은 필수적으로 캐싱 해야합니다.

따로 `GET`,`HEAD` 허용 항목에 `OPTION` 메서드를 추가하여, 캐싱 할수 있지만, OPTION 만 지정해서 캐싱 하는것은 불가능 합니다.

￼
![CF 콘솔에서 OPTION 메서드를 허용 해주는 방법](https://user-images.githubusercontent.com/69895368/211985516-5835a3e8-3af9-4eda-83d7-f5718b735849.png)


## 캐싱을 하는 시간 과 Cache Policy 에서 지정한 Maximum TTL 값 만큼 저장 될까?

Maximum TTL 값 만큼 캐싱 되지 않습니다.

캐싱 시간의 원본 헤더의 `Cache Control Max Age`에 따라 달라지며, Cache Control Max Age, Min TTL, MAX TTL 설정에 따라 저장 기간이 정해집니다.
￼
![CF TTL 설정 ](https://user-images.githubusercontent.com/69895368/211985553-d170fdb9-0561-4f87-b08e-2fe29d2e00bb.png)`Cache Control Max Age` 헤더가 없다면 기본 TTL로 설정한 시간만큼 캐싱되며, `Cache Control Max Age` 헤더 값이 최대 TTL 시간 을 초과 한다면 최대 TTL 시간 만큼 캐싱 됩니다.

## managed response policy의 `CORS-with-preflight-and-SecurityHeadersPolicy`를 사용하면 CORS를 처리하는 주체 가 주체가 어딜까

해당 Response Policy 를 설정하는 것은 CF 에서 CORS에 인증에 필요한 헤더를 추가해주는 것이기 때문에, CF 에서만 처리한다고 말씀드리기는 어렵습니다. CF 에서 응답 정책을 통해 처리가 가능할 뿐, CF에서만 처리하지는 않습니다.

`CORS-with-preflight-and-SecurityHeadersPolicy` 설정 했을 때, OPTION가 아닌 다른 메서드들의 응답에는 영향이 있는지
Preflight request (사전 요청)을 진행하는 경우에는 `OPTIONS` 메서드에 대해서 확인하기 때문에 다른 메서드에는 영향이 없습니다.