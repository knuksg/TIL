SELECT smoking, COUNT(smoking) FROM healthcare GROUP BY smoking;

SELECT is_drinking, COUNT(is_drinking) FROM healthcare GROUP BY is_drinking;

SELECT is_drinking, COUNT(is_drinking) 
FROM healthcare 
WHERE blood_pressure != '' 
GROUP BY is_drinking 
HAVING blood_pressure >= 200;

SELECT sido, COUNT(sido) 
FROM healthcare 
GROUP BY sido
HAVING COUNT(sido)>=50000;

SELECT height, COUNT(height) 
FROM healthcare 
GROUP BY height
ORDER BY COUNT(height) DESC
LIMIT 5;

SELECT weight, height, COUNT(*)
FROM healthcare 
GROUP BY height, weight
ORDER BY COUNT(*) DESC
LIMIT 5;

SELECT is_drinking, AVG(waist), COUNT(*)
FROM healthcare 
GROUP BY is_drinking;

SELECT gender, CEIL(AVG(va_left)) '평균 왼쪽 시력', CEIL(AVG(va_right)) '평균 오른쪽 시력'
FROM healthcare 
GROUP BY gender;

SELECT gender, ceil(va_left)
FROM healthcare 
GROUP BY gender;

SELECT age, AVG(height) AS '평균 키', AVG(weight) AS '평균 몸무게'
FROM healthcare 
GROUP BY age
HAVING "평균 키" >= 160 AND "평균 몸무게" >= 60;

SELECT is_drinking, smoking, AVG(weight/(height*height*0.0001))
FROM healthcare 
WHERE is_drinking != '' AND smoking != ''
GROUP BY is_drinking, smoking;

SELECT is_drinking, COUNT(*)
FROM healthcare 
WHERE blood_pressure >= 200
GROUP BY is_drinking;

SELECT gender, CEIL(AVG(va_left),2) '평균 왼쪽 시력', ROUND(AVG(va_right),2) '평균 오른쪽 시력'
FROM healthcare
GROUP BY gender;

SELECT ROUND(23.333, 2);

SELECT CONVERT(NUMERIC(5,2), 0.155115127323798)

SELECT SUBSTR('23.333', 1, 2);

SELECT 
  gender, 
  SUBSTR(AVG(va_left), 1, 4) '평균 왼쪽 시력', 
  SUBSTR(AVG(va_right), 1, 4) '평균 오른쪽 시력'
FROM healthcare
GROUP BY gender;