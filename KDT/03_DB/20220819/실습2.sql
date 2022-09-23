SELECT * 
FROM playlist_track A
ORDER BY PlaylistID DESC
LIMIT 5;

SELECT * 
FROM tracks B
ORDER BY TrackId ASC
LIMIT 5;

SELECT PlaylistId, Name
FROM playlist_track
  JOIN tracks
    ON playlist_track.TrackId = tracks.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;

SELECT PlaylistId, Name
FROM playlist_track
  JOIN tracks
    ON playlist_track.TrackId = tracks.TrackId
WHERE PlaylistId = 10
ORDER BY Name DESC
LIMIT 5;

SELECT COUNT(*)
FROM tracks
  INNER JOIN artists
    ON tracks.Composer = artists.Name;

SELECT COUNT(*)
FROM tracks
  LEFT JOIN artists
    ON tracks.Composer = artists.Name;

SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId ASC
LIMIT 5;

SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId ASC
LIMIT 5;

SELECT InvoiceLineId, I.InvoiceId
FROM invoice_items I
  JOIN invoices
    ON I.InvoiceId = invoices.InvoiceId
ORDER BY I.InvoiceId DESC
LIMIT 5;

SELECT A.InvoiceId, A.CustomerId
FROM invoices A
  JOIN customers B
    ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;

SELECT B.InvoiceLineId, A.InvoiceId, A.CustomerId
FROM invoices A
  JOIN invoice_items B
    ON A.InvoiceId = B.InvoiceId
  JOIN customers C
    ON A.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;

SELECT C.InvoiceLineId, A.CustomerId
FROM customers A
  JOIN invoices B
    ON A.CustomerId = B.CustomerId
  JOIN invoice_items C
    ON B.InvoiceId = C.InvoiceId

ORDER BY A.CustomerId ASC;
LIMIT 5;

SELECT *
FROM invoices
ORDER BY CustomerId;