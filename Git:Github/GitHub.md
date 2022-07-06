# Github 정리

## 1. 특징

## 2. 명령어

### 기본 설정을 위한 명령어

- Git remote add origin <원격저장소 주소>: 원격저장소(github) 정보를 로컬 저장소에 추가
- 깃아~ 원격저장소에 추가해줘~ 오리진이라는 이름에 주소를~! 
  - 확인: git remote -v
  - 삭제: git remote remove origin



### push

- git push <원격저장소이름> <브랜치이름>
- ==git push origin master
  - Push 실패 시 - 로컬과 원격 저장소 간 커밋 충돌이 일어난 것이다. 
  - 해결법: 원격저장소 pull 먼저 하고 로컬에서 통합한 후 push할 것.




### pull

- git push <원격저장소이름> <브랜치이름>
- ==git push origin master



### 예외 처리를 위한 명령어

- Touch .gitignore 명령어를 실행한 후, .gitignore 안에 예외 처리할 파일, 폴더, 확장자(<*.확장자>로 표시)를 추가한다.
  - 이미 커밋된 작업은 예외 처리 불가.
  - [Gitignore.io](https://www.toptal.com/developers/gitignore/): 예외 처리 파일을 만들어주는 사이트.
