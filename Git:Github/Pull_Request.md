# Pull_Request

## 1. 개요

- 풀리퀘스트는 서로 다른 브랜치를 로컬저장소 내에서 병합(merge)하지 않고, GitHub을 통해 병합하는 과정이다. 

## 2. 특징

- 원격저장소의 권한 유무에 따라 병합 과정이 달라진다.

## 3. 과정

### 1. 원격저장소의 권한이 있을 경우

1. 자신 혹은 타인이 git push origin <브랜치이름> 명령어로 명령을 내린다.
2. GitHub에서 Pull_Request 과정을 실행한다.
3. Merge 버튼을 누른다.

### 2. 원격저장소의 권한이 없을 경우

1. Fork[^1]할 저장소에서 우측 상단의 Fork버튼을 누른다.
2. 자신의 원격저장소에 저장될 이름을 작성하고 Create fork 한다.
3. 자신의 원격저장소에서 확인한다.
4. Fork 받아온 저장소를 로컬로 clone 한다.
5. branch를 생성하고 이동한다.
6. 작업 완료 후 변경 사항을 add, commit, push 한다.
7. Github에서 Compare & pull request를 생성한다.
   - 이 과정은 6번 이후 생성된 VSCode 내 링크로 대체 가능하다.
8. pull request 내용을 작성한 후 create pull request 한다.



[^1]:권한 없는 저장소를 복제하는 기능이다.