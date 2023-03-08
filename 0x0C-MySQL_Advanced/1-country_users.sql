-- In and not out
CREATE TABLE IF NOT EXISTS users (
    id int PRIMARY KEY AUTOINCREMENT NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    name varchar(255)
);
