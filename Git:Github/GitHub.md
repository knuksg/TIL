# 🅖🅗 GitHub

## 1. 개요

- 깃헙은 네트워크를 활용한 원격저장소이다.

## 2. 특징

- 깃헙은 'https://github.com/유저이름/저장소이름'의 주소를 갖는다.

## 3. 명령어

### - 기본 설정을 위한 명령어

- git remote add origin <원격저장소 주소>: 원격저장소(github) 정보를 로컬 저장소에 추가
- 깃아~ 원격저장소에 추가해줘~ 오리진이라는 이름으로 주소를~! 
  - 확인: git remote -v
  - 삭제: git remote rm <원격저장소이름>

### - push: 원격저장소에 로컬저장소 변경사항을 올린다.

- git push <원격저장소이름> <브랜치이름>
- e.g.: git push origin master
  - push 실패 시 - 로컬과 원격 저장소 간 커밋 충돌이 일어난 것이다. 
  - 해결법: 원격저장소 pull 먼저 하고 로컬에서 통합한 후 push할 것.


### - pull: 로컬저장소로 원격저장소 변경사항을 가져온다.

- git push <원격저장소이름> <브랜치이름>
- git push origin master

### - 예외 처리를 위한 명령어

- Touch .gitignore 명령어를 실행한 후, .gitignore 안에 예외 처리할 파일, 폴더, 확장자(<*.확장자>로 표시)를 추가한다.
  - 이미 커밋된 작업은 예외 처리 불가.
  - [Gitignore.io](https://www.toptal.com/developers/gitignore/): 예외 처리 파일을 만들어주는 사이트.
