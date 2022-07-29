# 🅖🅗 GitHub

## 1. 개요

- 깃헙은 네트워크를 활용한 원격저장소이다.

## 2. 특징

- 깃헙은 'https://github.com/유저이름/저장소이름'라는 주소로 구성된다.

## 3. 명령어

### 3.1. 기본 설정을 위한 명령어

- 원격저장소(github) 정보를 로컬 저장소에 추가
- (깃아~ 원격저장소에 추가해줘~ 오리진이라는 이름으로 주소를~! )

```zsh
git remote add origin <원격저장소 주소>
```



- 확인

```zsh
git remote -v
```


- 삭제

```zsh
git remote rm <원격저장소이름>
```



### 3.2. 버전 복제 & 이동을 위한 명령어

- 원격저장소로 로컬저장소 변경사항을 옮긴다.
- e.g.: git push origin master
  - push 실패 시 - 로컬과 원격 저장소 간 커밋 충돌이 일어난 것이다. 
  - 해결법: 원격저장소 pull 먼저 하고 로컬에서 통합한 후 push할 것.

```zsh
git push <원격저장소이름> <브랜치이름>
```




- 로컬저장소로 원격저장소 변경사항을 옮긴다.
- e.g.: git pull origin master

```zsh
git pull <원격저장소이름> <브랜치이름>
```



- 원격저장소를 복제하여 로컬저장소로 가져온다.

```zsh
git clone <원격저장소 주소>
```



### 3.3. 예외 처리를 위한 명령어

- touch .gitignore로 .gitignore 파일을 생성.
- .gitignore 안에 예외 처리할 파일, 폴더, 확장자(<*.확장자>로 표시)를 추가한다.
  - 이미 커밋된 작업은 예외 처리 불가.
  - [Gitignore.io](https://www.toptal.com/developers/gitignore/): 예외 처리 파일을 만들어주는 사이트.

```zsh
touch .gitignore
```

