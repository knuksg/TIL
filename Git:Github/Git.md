# Git 정리

## 1.  특징

### 1. git은 분산 버전 관리 시스템이다. 

### 2. git은 세 공간으로 나뉜다.

- Working Directory
- Staging Area
- Repository



## 2. 명령어

### 기본 설정을 위한 명령어

- git config --global user.name “username”
- git config --global user.email “my@email.com”



### init

- git init: 로컬 저장소 생성.



### add

- git add <파일명>: Working Directory에서 Staging Area로 옮긴다.
  - git add .: 모든 파일 추가.



### commit

- git commit -m '<커밋메시지>': Working Directory에서 Repository로 옮긴다.
  - git commit: 좀 더 긴 메시지를 담을 수 있는 작업을 실행한다.

### status

- git status: 현재 상태를 알려준다. (Working Directory, Staging Area)



### log

- git log : 현재 상태를 알려준다. (Repository)
  - git log -1: 가장 최근 버전을 보여달라.
  - git log --oneline: 한 줄로 표시해달라.
  - git log -2 --oneline: 가장 최근 버전 두 개까지 한 줄로 보여달라.

