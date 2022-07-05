# Git 기초

## 기본 특징

### 1. git은 분산 버전 관리 시스템이다. ![Screen Shot 2022-07-05 at 4.39.00 PM](/Users/KIMSEONGYO1/Library/Application Support/typora-user-images/Screen Shot 2022-07-05 at 4.39.00 PM.png)

### 2. git은 세 공간으로 나뉜다.

- Working Directory
- Staging Area
- Repository

## 기본 설정

- git config --global user.name “username”

- git config --global user.email “my@email.com”

## 기본 명령어

### init

- git init : 로컬 저장소 생성.

### add

- git add <파일명>: 1통을 2통으로 옮긴다.
  - git add . : 모든 파일 추가.


### commit

- git commit -m '<커밋메시지>' : 2통을 커밋으로 옮긴다.

### status

- git status : 현재 상태를 알려준다. (1통, 2통)

### log

- git log : 현재 상태를 알려준다. (서밋)
  - git log -1 : 가장 최근 버전을 보여달라.
  - git log --oneline : 한 줄로 표시해달라.
  - git log -2 --oneline: 가장 최근 버전 두 개까지 한 줄로 보여달라.

