# Django 개발 환경 설정 가이드

- 가상환경 생성 / 실행
- Django LTS 버전 설치
- Django 프로젝트 생성
- Django 실행

## 01. 프로젝트 폴더 생성하기

터미널이나 GUI에서 개발 환경을 설정할 폴더를 생성한다.

## 02. 가상환경 생성/실행

생성한 폴더에서 터미널이나 VSCode를 연다.

`python -m venv [가상환경 이름(ex: test-venv)]`

폴더 안에 가상환경 이름으로 폴더가 만들어졌다.

`source [폴더이름]/bin/[가상환경 이름]/activate`

가상환경이 실행되었다.

## 03. Django LTS 버전 설치

Certain feature releases will be designated as **long-term support (LTS) releases**. These releases will get security and data loss fixes applied for a guaranteed period of time, typically three years.  - https://www.djangoproject.com/download/

LTS 버전은 최신 버전이 아니다. 가장 길게 보안과 유지 보수를 보장받는 버전이다.

`pip3 install django==3.2.12` (2022.09.21. 기준 LTS 버전)

## 04. Django 프로젝트 생성

`django-admin startproject [프로젝트 이름] [생성 위치]` (현재 위치일 경우 `.`)

폴더 안에 프로젝트 이름으로 폴더가 만들어졌다.

## 05. Django 실행

`python managy.py runserver`

Django가 실행되었다.

`localhost:8000` 혹은 VSCode에서 보여주는 주소로 접속하면 로켓이 발사되는 화면이 성공적으로 나온다.