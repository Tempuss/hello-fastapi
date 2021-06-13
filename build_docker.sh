#!/bin/bash

SERVICE="hello-fastapi"
DOCKER_ACCESS_ID=""
DOCKER_PASSWORD=""
SERVICE_TYPE=""
VERSION=""
DOCKER_URL="tempus3787"


# 도커 빌드, 푸시할 타입 설정
function set_build_type()
{
  read -p "version : " VERSION
}

#docker hub 계정 정보 입력
function set_docker_credential()
{
    printf "Docker ACCESS_ID : "
    read -s DOCKER_ACCESS_ID
    echo ""

    printf "Docker Password : "
    read -s DOCKER_PASSWORD
    echo ""
}


# 도커 빌드
function build_docker()
{
    # 도커 빌드
    docker build \
    --tag $DOCKER_URL/$SERVICE:$VERSION \
    --no-cache \
    .

    docker image tag $DOCKER_URL/$SERVICE:$VERSION $DOCKER_URL/$SERVICE:latest

}

# 도커 푸시
function push_docker()
{
    # Docker Private Hub Login
    docker login -u="$DOCKER_ACCESS_ID" -p="$DOCKER_PASSWORD"


    # Docker Private Hub에 Push
    docker push $DOCKER_URL/$SERVICE:$VERSION
    docker push $DOCKER_URL/$SERVICE:latest

}

# 추가 파라미터에 따른 build, push 분기
if [ "$1" = "build" ]; then
    set_build_type
    build_docker
elif [ "$1" = "push"  ]; then
   set_build_type
    set_docker_credential
    push_docker
fi

