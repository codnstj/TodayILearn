# CloudFront

## 그게 뭐임

cloudfront 란  Aws 에서 제공하는 CDN 서비스 이다. 캐싱을 통해 사용자에게 좀 더 빠른 전송 속도를 제공함을 목적으로 합니다.

- Origin Server : 원본 데이터를 가지고 있는 서버입니다. 보통 AWS 에서의 Origin Server 는 S3, Ec2 인스턴스 이다.
- Edge Server = Edge Location : Aws 에서 실질적으로 제공하는 전 세계에 퍼져있는 서버입니다. Edge Server 에는 요청받은 데이터에 대해서 같은 요청에 대해서 빠르게 응답해주기 위해 Cache 기능을 제공한다.
- 데이터 전송이 발생하는 과정 
  1. 클라이언트로 Edge 서버로의 요청이 발생한다.
  2. Edge Server 는 요청이 발생한 데이터에 대하여 캐싱 여부를 확인합니다.
  3. (1) 사용자의 근거리에 위치한 Edge Server 중 캐싱 데이터가 존재한다면 사용자의 요청에 맞는 데이터를 응답합니다.
  4. (2) 사용자의 요청에 적합한 데이터가 캐싱되어 있지 않은 경우 Origin Server 로 요청이 포워딩 됩니다.
  5. 요청받은 데이터에 대해 Origin Server에서 획득한 후 Edge Server 에 캐싱 데이터를 생성하고, 클라이언트로 응답이 발생합니다.

## 설정값

- 캐시 키 및 원본 요청 
  - 캐시 정책 및 출처 요청 정책
    - 캐시 정책
      - Caching Optimized
        - CF 가 캐시 키에 포함된 값을 최소화 하여 캐시 효율성을  최적화 하도록 설계되었습니다. CF는 캐시 키에 쿼리 문자열이나 쿠키를 포함하지 않으며 정규화된 `Accept-Encoding` 헤더만 포함합니다. 이렇게 하면 오리진에서 객체를 반환하거나 CloudFront 엣지 압축이 활성화된 경우 CloudFront 에서 Gzip 및 Brotli 압축 형식의 객체를 별도로 캐시 가능하다.
      (`Accept-Encoding` 헤더만 포함 / 쿠키 X / 쿼리 스트링 X)
      - Caching Disabled
        - 캐싱을 비활성화 합니다. 이 정책은 동적 콘텐츠 및 캐시할수 없는 요청에 유용합니다.
    - 원본 요청 정책
      - origin access policy