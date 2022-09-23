SELECT last_name, COUNT(last_name) FROM users GROUP BY last_name;

CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번내용');

ALTER TABLE article RENAME TO news;

ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';