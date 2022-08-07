# Dockerfile 기본 명령어

> 이미지를 만드는데 사용한 Dockerfile 의 기본적인 명령어들 입니다. 

- FROM 
  - 베이스 이미지를 지정합니다 , 반드시 지정해야하며 어떤 이미지도 베이스 이미지가 될수 있습니다. 
  - tag 는 될수 있으면 latest(기본값) 보다 구체적인 버전을 지정하는것이 좋습니다.
    ```docker
    FROM <image>:<tag>
    FROM ubuntu:16.04
    ```

- MAINTAINTER 
  - Dockerfile 을 관리하는 사람의 이름 또는 이메일 정보를 적습니다. 빌드시 영향을 주지 않습니다.
    ```docker
    MAINTAINER <name>
    MAINTAINER chaewoon.me@gmail.com
    ```

- COPY 
  - 파일이나 디렉토리 이미지로 복사합니다. 일반적으로 소스를 복사하는데 사용되곤 합니다.
  - tar or get 디렉토리가 없다면 자동으로 생성합니다.
    ```docker
    COPY <src>... <dest>
    COPY . /usr/src/app
    ```
- ADD 
  - COPY 명령어와 매우 유사하나 몇가지 추가 기능이 있습니다.
  -  SRC 에 파일 대신 URL 을 입력 할수있다. 
  -  src 에 압축파일을 입력하는 경우 자동으로 압축을 해제하면서 복사된다.
    ```docker
    ADD <src>... <dest>
    ADD . /usr/src/app
    ```
- RUN 
  - 가장 많이 사용하는 구문으로, 명령어를 그대로 실행합니다. 
  - 내부적으로 /bin/sh -c 뒤에 명령어를 실행하는 방식입니다.
    ```docker
    RUN <command>
    RUN ["python3","manage.py","runserver"]
    RUN bundle install
    ```


- CMD 
  - 도커 컨테이너가 실행되었을때 실행되는 명령어를 정의 합니다.
  -  빌드할 떄는 실행되지 않으며 여러개의 CMD 가 존재할 경우 가장 마지막 CMD 만 실행됩니다.
  -  한꺼번에 여러 개의 프로그램을 실행하고 싶은 경우에는 run.sh 파이릉ㄹ 작성하여 데몬으로 실행시키거나, supervisord 나 forego 와 같은 여러개의 프로그램을 실행하는 프로그램을 사용합니다.
    ```docker
    CMD ["excutable","param1","param2"]
    CMD command param1 param2
    CMD python3 manage.py runserver
    ```

- WORKDIR 
  - RUN, CMD, ADD, COPY 등이 이루어질 기본 디렉토리를 설정합니다. 
  - 각 명령어의 현재 디렉토리는 한 줄 한 줄마다 초기화되기 떄문에 ` RUN cd  /path `를 하더라도 다음 명령어에선 다시 위치가 초기화됩니다.
  - 같은 디렉토리에서 계속 작업하기 위해서 WORKDIR 을 사용합니다.
    ```docker
    WORKDIR /path/to/workdir
    ```

- EXPOSE 
  - 도커 컨테이너가 실행되었을 때 요청을 기다리고 있는 (Listen) 포트를 지정합니다. 
  - 여러개의 포트를 지정할수 있습니다.
    ```docker
    RUN <command>
    RUN ["python3","manage.py","runserver"]
    RUN bundle install
    ```    

- VOLUME
  - 컨테이너 외부에 파일시스템을 마운트 할 떄 사용합니다. 반드시 지정하지 않아도 마운트 할수 있지만, 기본적으로 지정하는 것이 좋습니다.
    ```docker
    VOLUME["/data"]
    ```

- ENV
  - 컨테이넝에서 사용할 환경변수를 지정합니다. 컨테이너를 실행할 떄 `-e` 옵션을 사용하면 기존 값을 오버라이딩 하게 됩니다.
    ```docker
    ENV <key> <value>
    ENV <key>=<value>
    ENV DB_URL mysql
    ```