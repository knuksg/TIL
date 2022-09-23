SELECT * 
FROM albums
ORDER BY Title DESC
LIMIT 5;

SELECT COUNT(*) '고객 수'
FROM customers;

SELECT FirstName '이름', LastName '성'
FROM customers
WHERE Country = 'USA'
ORDER BY FirstName DESC
LIMIT 5;

SELECT COUNT(*) '송장수'
FROM invoices
WHERE BillingPostalCode != 'NULL';

SELECT *
FROM invoices
WHERE BillingState ISNULL
ORDER BY InvoiceDate DESC
LIMIT 5;

SELECT COUNT(*)
FROM invoices
WHERE strftime("%Y", "InvoiceDate") = '2013';

SELECT COUNT(*)
FROM invoices
WHERE InvoiceDate = '2013';

SELECT CustomerId '고객ID', FirstName '이름', LastName '성'
FROM customers
WHERE FirstName LIKE 'L%'
ORDER BY "고객ID";

SELECT 
  COUNT(*) '고객 수',
  Country '나라'
FROM customers
GROUP BY Country
ORDER BY "고객 수" DESC
LIMIT 5;

SELECT 
  ArtistId,
  COUNT(*)
FROM albums
GROUP BY ArtistId
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT 
  ArtistId,
  COUNT(*)
FROM albums
GROUP BY ArtistId
HAVING COUNT(*) >= 10
ORDER BY COUNT(*) DESC;

SELECT 
  COUNT(*) '고객 수',
  Country '나라',
  State
FROM customers
WHERE State != 'NULL'
GROUP BY Country, State
ORDER BY "고객 수" DESC, "나라" DESC
LIMIT 5;

SELECT 
  CustomerId,
  CASE 
    WHEN Fax ISNULL THEN 'X'
    ELSE 'O'
  END
  AS "Fax 유/무"
FROM customers
ORDER BY CustomerId
LIMIT 5;

SELECT 
  LastName,
  FirstName,
  date("now") - strftime("%Y-%m-%d","BirthDate") + 1
  AS "나이"
FROM employees
ORDER BY EmployeeId;

SELECT Name
FROM artists
WHERE 
  ArtistId = 
  (SELECT ArtistId
    FROM albums
    GROUP BY ArtistId
    ORDER BY COUNT(*) DESC
    LIMIT 1
  );

SELECT Name
FROM genres
WHERE 
  GenreId = 
  (SELECT GenreId
    FROM tracks
    GROUP BY GenreId
    ORDER BY COUNT(*)
    LIMIT 1
  );

SELECT GenreId, COUNT(*)
    FROM tracks
    GROUP BY GenreId
    ORDER BY COUNT(*);

SELECT Name
FROM media_types
WHERE MediaTypeId = 
  (SELECT MediaTypeId
    FROM tracks
    GROUP BY MediaTypeId
    ORDER BY COUNT(*) DESC
    LIMIT 1
  );

SELECT Name
FROM media_types
WHERE MediaTypeId = 
  (SELECT MediaTypeId
    FROM tracks
    GROUP BY MediaTypeId
    ORDER BY COUNT(*) DESC
    LIMIT 1
  );

  SELECT GenreId
  FROM tracks
  GROUP BY GenreId
  ORDER BY COUNT(*) DESC
  LIMIT 1;

  SELECT MediaTypeId
  FROM tracks
  WHERE GenreId = 
  (SELECT GenreId
    FROM tracks
    GROUP BY GenreId
    ORDER BY COUNT(*) DESC
    LIMIT 1)
  GROUP BY MediaTypeId
  ORDER BY COUNT(*)
  LIMIT 1;

SELECT Name
FROM media_types
WHERE MediaTypeId = 
(  SELECT MediaTypeId
    FROM tracks
    WHERE GenreId = 
    (SELECT GenreId
      FROM tracks
      GROUP BY GenreId
      ORDER BY COUNT(*) DESC
      LIMIT 1)
    GROUP BY MediaTypeId
    ORDER BY COUNT(*)
    LIMIT 1);

SELECT BillingPostalCode, length(BillingPostalCode)
FROM invoices
WHERE not BillingPostalCode
ORDER BY length(BillingPostalCode);

WHERE BillingPostalCode ISNULL;

2층 1  4  10
1층 1  3  6
0층 1  2  3
   1호 2호 3호