-- In and not out
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) UNIQUE NOT NULL,
    name varchar(255),
    country ENUM('US', 'CO', 'TN')
);
