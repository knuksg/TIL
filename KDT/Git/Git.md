

# ๐ Git

## 1.  ๊ฐ์

- ๊น์ 2005๋ ๋ฆฌ๋์ค ํ ๋ฅด๋ฐ์ค๊ฐ ๊ฐ๋ฐํ ๋ถ์ฐ ๋ฒ์  ๊ด๋ฆฌ ์์คํ์ด๋ค.

## 2. ํน์ง

 - ๊น์ ์ปดํจํฐ ํ์ผ์ ๋ณ๊ฒฝ ์ฌํญ์ ์ถ์ ํ๋ค.
 - ๊น์ ์ฌ์ฉ์๋ค ๊ฐ์ ์์์ ์กฐ์จํ๋ค.

- ๊น์ ์ธ ๊ณต๊ฐ์ผ๋ก ๊ตฌ์ฑ๋๋ค.

  - Working Directory

  - Staging Area

  - Repository


## 3. ๋ช๋ น์ด

![Screen Shot 2022-07-09 at 7.21.26 PM](Git.assets/Screen Shot 2022-07-09 at 7.21.26 PM.png)

> git --help๋ฅผ ์๋ ฅํ์ ๋ ๋์ค๋ ํ๋ฉด. ๋ชจ๋  ๋ช๋ น์ด๋ฅผ ํ์ธํ๋ ค๋ฉด git help -a๋ฅผ ์๋ ฅํ  ๊ฒ.



### 3.1. ๊ธฐ๋ณธ ์ค์ ์ ์ํ ๋ช๋ น์ด

> git ์ ์ฅ์๋ฅผ ์ต์ด ์ค์ ํ  ๋ ์ด๋ฆ๊ณผ ์ด๋ฉ์ผ์ ๋ฑ๋กํด์ผ ํ๋ค.

- ์ด๋ฆ ์ค์ 

```zsh
git config --global user.name โusernameโ
```


- ์ด๋ฆ ์ค์  ํ์ธ

```zsh
git config user.name
```



- ์ด๋ฉ์ผ ์ค์ 

```zsh
git config --global user.email โmy@email.comโ
```



- ์ด๋ฉ์ผ ์ค์  ํ์ธ

```zsh
git config --global -l
```



- ์ ์ฒด ํ์ธ

```zsh
git config -l
```



### 3.2. Start a working area

- ์๊ฒฉ์ ์ฅ์๋ฅผ ๋ณต์ ํด, ์๋ก์ด ์ ์ฅ์๋ฅผ ๋ง๋ ๋ค.

```zsh
git clone
```



- ์๋ก์ด ์ ์ฅ์๋ฅผ ๋ง๋ ๋ค.

```zsh
git init
```



### 3.3. Work on the current change

- Working Directory์์ Staging Area๋ก ์ฎ๊ธด๋ค.
  - git add .: ๋ชจ๋  ํ์ผ ์ถ๊ฐ.

```zsh
git add <ํ์ผ๋ช>
```



### 3.4. Examine the history and state 

- ํ์ฌ ์ํ๋ฅผ ์๋ ค์ค๋ค. (Working Directory, Staging Area)

```zsh
git status
```



- ํ์ฌ ๋ฒ์ ์ ์๋ ค์ค๋ค. (Repository)

  - git log -1: ๊ฐ์ฅ ์ต๊ทผ ๋ฒ์ ์ ๋ณด์ฌ๋ฌ๋ผ.

  - git log --oneline: ํ ์ค๋ก ํ์ํด๋ฌ๋ผ.

  - git log -2 --oneline: ๊ฐ์ฅ ์ต๊ทผ ๋ฒ์  ๋ ๊ฐ๊น์ง ํ ์ค๋ก ๋ณด์ฌ๋ฌ๋ผ.

```zsh
git log
```



### 3.5. Grow, mark and tweak you common history

- Working Directory์์ Repository๋ก ์ฎ๊ธฐ๊ณ  ์ปค๋ฐ๋ฉ์์ง๋ฅผ ์ถ๊ฐํ๋ค.
  - git commit: ์ข ๋ ๊ธด ๋ฉ์์ง๋ฅผ ๋ด์ ์ ์๋ ์์์ ์คํํ๋ค.

```zsh
git commit -m '<์ปค๋ฐ๋ฉ์์ง>'
```



### 3.6. Collaborate

- ์๊ฒฉ์ ์ฅ์์์ ๋ก์ปฌ์ ์ฅ์๋ก ์ปค๋ฐ์ ์ฎ๊ธด๋ค.

```zsh
git pull origin master
```



- ๋ก์ปฌ์ ์ฅ์์์ ์๊ฒฉ์ ์ฅ์๋ก ์ปค๋ฐ์ ์ฎ๊ธด๋ค.

```zsh
git push origin master
```



## 4. ๊ด๋ จ ์๋ฃ

[Pro_Git](https://git-scm.com/book/ko/v2)

