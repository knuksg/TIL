-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- 모든 사람의 수 찾기
SELECT COUNT(*) FROM healthcare;

-- 10살 미만인 사람의 수 찾기
SELECT COUNT(*) FROM healthcare WHERE age<10;

-- 젠더 1인 사람의 수 찾기
SELECT COUNT(*) FROM healthcare WHERE gender=1;

-- 스모킹 3, 드링킹 1인 사람의 수 찾기
SELECT COUNT(*) FROM healthcare WHERE smoking=3 AND is_drinking=1;

-- 양쪽 시력 2.0 이상인 사람의 수 찾기
SELECT COUNT(*) FROM healthcare WHERE va_left>=2.0 AND va_right>=2.0;

-- 중복 없이 모든 sido 찾기
SELECT DISTINCT sido FROM healthcare;

-- waist 100 이상이고 blood_pressure 150 이상인 사람의 수 찾기
SELECT COUNT(*) FROM healthcare WHERE waist>=100 AND blood_pressure>=150;